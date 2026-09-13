import { wordsFromAlignment, type CharacterAlignment, type WordTiming } from '#lib/audio/alignment.js';

/** A premade ElevenLabs voice used until the learner picks one in Settings. */
export const DEFAULT_NARRATION_VOICE = '21m00Tcm4TlvDq8ikWAM';
export const DEFAULT_NARRATION_MODEL = 'eleven_multilingual_v2';

export interface NarrationRequest {
	apiKey: string;
	text: string;
	voiceId?: string | null;
	modelId?: string | null;
	previousText?: string | null;
	nextText?: string | null;
	speed?: number | null;
}

export interface NarrationClip {
	audioBase64: string;
	mimeType: 'audio/mpeg';
	words: WordTiming[];
}

export class NarrationError extends Error {
	constructor(
		message: string,
		readonly status: number
	) {
		super(message);
	}
}

/** Synthesizes one passage with character timings, grouped into words. The key is never logged. */
export async function synthesizeNarration(req: NarrationRequest): Promise<NarrationClip> {
	const voice = encodeURIComponent(req.voiceId || DEFAULT_NARRATION_VOICE);
	const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice}/with-timestamps?output_format=mp3_44100_128`, {
		method: 'POST',
		headers: { 'xi-api-key': req.apiKey, 'content-type': 'application/json', accept: 'application/json' },
		body: JSON.stringify({
			text: req.text,
			model_id: req.modelId || DEFAULT_NARRATION_MODEL,
			previous_text: req.previousText || undefined,
			next_text: req.nextText || undefined,
			voice_settings: req.speed ? { speed: Math.min(Math.max(req.speed, 0.7), 1.2) } : undefined
		})
	});
	if (!response.ok) {
		const reason = response.status === 401 ? 'ElevenLabs rejected the API key' : `ElevenLabs request failed (${response.status})`;
		throw new NarrationError(reason, response.status === 401 ? 401 : 502);
	}
	const body = (await response.json()) as { audio_base64: string; alignment: CharacterAlignment | null };
	return {
		audioBase64: body.audio_base64,
		mimeType: 'audio/mpeg',
		words: body.alignment ? wordsFromAlignment(body.alignment) : []
	};
}
