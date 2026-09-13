import { narrator } from '#lib/audio/narrator.svelte.js';
import { TOOL_DEFINITIONS, toolArgs, type ToolArgs, type ToolResult } from '#lib/tutor/tools.js';
import { reading } from '#lib/tutor/reading-context.svelte.js';

type TutorStatus = 'idle' | 'connecting' | 'live' | 'closing' | 'error';

export interface Caption {
	role: 'learner' | 'tutor';
	text: string;
}

interface FunctionCallItem {
	call_id: string;
	name: string;
	arguments: string;
}

const ACTIVITY: Record<string, string> = {
	get_reading_context: 'Looking at your page',
	show_in_reader: 'Opening the reader',
	search_knowledge: 'Searching the course notes',
	get_knowledge_entry: 'Reading a note',
	get_unit_notes: 'Reading the chapter notes',
	record_learning_evidence: 'Updating your learning record'
};

/**
 * Browser side of the GPT-Live tutor: WebRTC audio, the oai-events data channel, and the function-call loop.
 * Calls are collected from nested `response.output_item.done` events; after `response.completed` every result is
 * returned with `response.item.create`, followed by a single `response.create`.
 */
export class LiveTutor {
	status = $state<TutorStatus>('idle');
	error = $state<string | null>(null);
	muted = $state(false);
	captions = $state<Caption[]>([]);
	activity = $state<string | null>(null);

	#pc: RTCPeerConnection | null = null;
	#channel: RTCDataChannel | null = null;
	#mic: MediaStream | null = null;
	#audio: HTMLAudioElement | null = null;
	#sessionId: string | null = null;
	#usageSeconds: number | null = null;
	#pending = new Map<string, Map<string, FunctionCallItem>>();
	#lastContext: string | null = null;
	#contextTimer: ReturnType<typeof setTimeout> | undefined;
	#closed: (() => void) | null = null;

	get active() {
		return this.status === 'connecting' || this.status === 'live' || this.status === 'closing';
	}

	async start() {
		if (this.active) return;
		narrator.stop();
		this.status = 'connecting';
		this.error = null;
		this.captions = [];
		try {
			const pc = new RTCPeerConnection();
			this.#pc = pc;
			const audio = new Audio();
			audio.autoplay = true;
			this.#audio = audio;
			pc.addEventListener('track', (event) => {
				audio.srcObject = event.streams[0] ?? new MediaStream([event.track]);
			});
			pc.addEventListener('connectionstatechange', () => {
				if (pc.connectionState === 'failed') this.#fail('The voice connection was lost');
			});

			const mic = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true } });
			this.#mic = mic;
			for (const track of mic.getAudioTracks()) pc.addTrack(track, mic);

			const channel = pc.createDataChannel('oai-events');
			this.#channel = channel;
			channel.addEventListener('message', (event) => this.#onMessage(event.data));

			await pc.setLocalDescription(await pc.createOffer());
			await waitForIceGathering(pc, 10_000);

			const response = await fetch('/api/live/session', {
				method: 'POST',
				headers: { 'content-type': 'application/json' },
				body: JSON.stringify({ sdp: pc.localDescription?.sdp, reading_context: reading.describe() })
			});
			if (!response.ok) throw new Error(await messageFrom(response));
			const result = (await response.json()) as { session: { id: string }; transport: { sdp: string } };
			this.#sessionId = result.session.id;
			await pc.setRemoteDescription({ type: 'answer', sdp: result.transport.sdp });
		} catch (e) {
			this.#fail(e instanceof Error ? e.message : 'Could not start the tutor');
		}
	}

	async stop() {
		if (!this.#pc) {
			this.status = 'idle';
			return;
		}
		if (this.#channel?.readyState === 'open') {
			this.status = 'closing';
			const closed = new Promise<void>((resolve) => (this.#closed = resolve));
			this.#send({ type: 'session.close', event_id: crypto.randomUUID() });
			await Promise.race([closed, new Promise((resolve) => setTimeout(resolve, 3000))]);
		}
		await this.#reportEnd();
		this.#teardown();
		this.status = 'idle';
	}

	toggleMute() {
		if (this.status !== 'live') return;
		this.muted = !this.muted;
		this.#send({ type: this.muted ? 'session.input_audio.mute' : 'session.input_audio.unmute', event_id: crypto.randomUUID() });
	}

	/** Sends the reading context as quiet context when it changes (debounced). */
	contextChanged() {
		if (this.status !== 'live') return;
		clearTimeout(this.#contextTimer);
		this.#contextTimer = setTimeout(() => this.#sendContext(), 800);
	}

	#sendContext() {
		const context = reading.describe();
		if (!context || context === this.#lastContext) return;
		this.#lastContext = context;
		this.#send({ type: 'session.thinking.append', delegation_id: null, content: `The learner now has open: ${context}`, event_id: crypto.randomUUID() });
	}

	#onMessage(raw: string) {
		let message: Record<string, any>;
		try {
			message = JSON.parse(raw);
		} catch {
			return;
		}
		switch (message.type) {
			case 'session.started':
				this.status = 'live';
				this.#lastContext = reading.describe();
				break;
			case 'session.input_transcript.delta':
				this.#caption('learner', message.delta);
				break;
			case 'session.output_transcript.delta':
				this.#caption('tutor', message.delta);
				break;
			case 'session.usage.updated':
				this.#usageSeconds = message.usage?.seconds ?? this.#usageSeconds;
				break;
			case 'session.closed':
				this.#usageSeconds = message.usage?.seconds ?? this.#usageSeconds;
				this.#closed?.();
				break;
			case 'error':
				this.error = message.error?.message ?? 'The tutor reported an error';
				break;
			case 'response.event':
				void this.#onResponseEvent(message.delegation_id ?? 'uncorrelated', message.event ?? {});
				break;
		}
	}

	async #onResponseEvent(key: string, event: Record<string, any>) {
		if (event.type === 'response.created') {
			this.#pending.set(key, new Map());
		} else if (event.type === 'response.output_item.done' && event.item?.type === 'function_call') {
			const calls = this.#pending.get(key) ?? new Map<string, FunctionCallItem>();
			calls.set(event.item.call_id, event.item);
			this.#pending.set(key, calls);
		} else if (event.type === 'response.completed' || event.type === 'response.failed' || event.type === 'response.incomplete') {
			const calls = this.#pending.get(key);
			this.#pending.delete(key);
			if (event.type !== 'response.completed' || !calls?.size) return;
			const outputs = await Promise.all(
				[...calls.values()].map(async (call) => ({ call_id: call.call_id, output: JSON.stringify(await this.#runTool(call)) }))
			);
			for (const output of outputs) {
				this.#send({ type: 'response.item.create', event_id: crypto.randomUUID(), item: { type: 'function_call_output', ...output } });
			}
			this.#send({ type: 'response.create', event_id: crypto.randomUUID() });
		}
	}

	async #runTool(call: FunctionCallItem): Promise<ToolResult> {
		const definition = TOOL_DEFINITIONS.find((t) => t.name === call.name);
		if (!definition) return { ok: false, reason: `Unknown tool ${call.name}` };
		this.activity = ACTIVITY[call.name] ?? 'Working';
		try {
			if (definition.runner === 'server') {
				const response = await fetch('/api/kb/tool', {
					method: 'POST',
					headers: { 'content-type': 'application/json' },
					body: JSON.stringify({ name: call.name, arguments: call.arguments || '{}', call_id: call.call_id })
				});
				if (!response.ok) return { ok: false, reason: `Tool request failed (${response.status})` };
				return (await response.json()) as ToolResult;
			}
			let args: unknown;
			try {
				args = JSON.parse(call.arguments || '{}');
			} catch {
				return { ok: false, reason: 'Arguments are not valid JSON' };
			}
			if (definition.name === 'get_reading_context') return { ok: true, context: reading.current };
			if (definition.name === 'show_in_reader') {
				const parsed = toolArgs.show_in_reader.safeParse(args);
				if (!parsed.success) return { ok: false, reason: 'Invalid arguments' };
				const shown = await reading.show(parsed.data as ToolArgs<'show_in_reader'>);
				return shown ? { ok: true, shown: true } : { ok: false, reason: 'That place is not available in the reader' };
			}
			return { ok: false, reason: 'Unhandled client tool' };
		} catch {
			return { ok: false, reason: 'The tool failed' };
		} finally {
			this.activity = null;
		}
	}

	#caption(role: Caption['role'], delta: unknown) {
		if (typeof delta !== 'string' || !delta) return;
		const last = this.captions.at(-1);
		if (last && last.role === role) last.text += delta;
		else this.captions.push({ role, text: delta });
	}

	#send(event: Record<string, unknown>) {
		if (this.#channel?.readyState === 'open') this.#channel.send(JSON.stringify(event));
	}

	#fail(message: string) {
		this.error = message;
		void this.#reportEnd();
		this.#teardown();
		this.status = 'error';
	}

	async #reportEnd() {
		if (!this.#sessionId) return;
		const liveSessionId = this.#sessionId;
		this.#sessionId = null;
		try {
			await fetch('/api/live/session/end', {
				method: 'POST',
				headers: { 'content-type': 'application/json' },
				body: JSON.stringify({ live_session_id: liveSessionId, usage_seconds: this.#usageSeconds == null ? null : Math.round(this.#usageSeconds) })
			});
		} catch {
			/* best effort */
		}
	}

	#teardown() {
		clearTimeout(this.#contextTimer);
		this.#closed = null;
		this.#pending.clear();
		this.#channel?.close();
		this.#pc?.close();
		for (const track of this.#mic?.getTracks() ?? []) track.stop();
		if (this.#audio) this.#audio.srcObject = null;
		this.#channel = null;
		this.#pc = null;
		this.#mic = null;
		this.#audio = null;
		this.muted = false;
		this.activity = null;
		this.#lastContext = null;
	}
}

function waitForIceGathering(pc: RTCPeerConnection, timeoutMs: number): Promise<void> {
	if (pc.iceGatheringState === 'complete') return Promise.resolve();
	return new Promise((resolve) => {
		const done = () => {
			clearTimeout(timer);
			pc.removeEventListener('icegatheringstatechange', check);
			resolve();
		};
		const check = () => {
			if (pc.iceGatheringState === 'complete') done();
		};
		const timer = setTimeout(done, timeoutMs);
		pc.addEventListener('icegatheringstatechange', check);
	});
}

async function messageFrom(response: Response): Promise<string> {
	try {
		const body = await response.json();
		if (typeof body?.message === 'string') return body.message;
	} catch {
		/* not JSON */
	}
	return `Request failed (${response.status})`;
}

export const tutor = new LiveTutor();
