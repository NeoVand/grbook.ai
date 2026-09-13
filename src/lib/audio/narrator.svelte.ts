import { wordAt, type WordTiming } from '#lib/audio/alignment.js';

type NarratorStatus = 'idle' | 'loading' | 'playing' | 'paused' | 'error';

/** Plays ElevenLabs narration for one passage at a time and tracks the word being spoken. */
class Narrator {
	status = $state<NarratorStatus>('idle');
	error = $state<string | null>(null);
	passageId = $state<string | null>(null);
	words = $state<WordTiming[]>([]);
	wordIndex = $state(-1);

	#audio: HTMLAudioElement | null = null;
	#frame = 0;
	#request = 0;

	async play(passageId: string, text: string) {
		this.stop();
		const request = ++this.#request;
		this.passageId = passageId;
		this.status = 'loading';
		this.error = null;
		try {
			const response = await fetch('/api/tts', {
				method: 'POST',
				headers: { 'content-type': 'application/json' },
				body: JSON.stringify({ text })
			});
			if (!response.ok) throw new Error(await messageFrom(response));
			const clip = (await response.json()) as { audioBase64: string; mimeType: string; words: WordTiming[] };
			if (request !== this.#request) return;
			this.words = clip.words;
			const audio = new Audio(`data:${clip.mimeType};base64,${clip.audioBase64}`);
			audio.addEventListener('ended', () => this.stop());
			this.#audio = audio;
			await audio.play();
			this.status = 'playing';
			this.#tick();
		} catch (e) {
			if (request !== this.#request) return;
			this.status = 'error';
			this.error = e instanceof Error ? e.message : 'Narration failed';
		}
	}

	pause() {
		if (this.#audio && this.status === 'playing') {
			this.#audio.pause();
			this.status = 'paused';
			cancelAnimationFrame(this.#frame);
		}
	}

	async resume() {
		if (this.#audio && this.status === 'paused') {
			await this.#audio.play();
			this.status = 'playing';
			this.#tick();
		}
	}

	stop() {
		this.#request++;
		cancelAnimationFrame(this.#frame);
		this.#audio?.pause();
		this.#audio = null;
		this.status = 'idle';
		this.passageId = null;
		this.words = [];
		this.wordIndex = -1;
	}

	#tick = () => {
		if (!this.#audio) return;
		this.wordIndex = wordAt(this.words, this.#audio.currentTime);
		this.#frame = requestAnimationFrame(this.#tick);
	};
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

export const narrator = new Narrator();
