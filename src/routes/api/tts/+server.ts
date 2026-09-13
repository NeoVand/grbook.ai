import { error, json } from '@sveltejs/kit';
import { z } from 'zod';
import type { RequestHandler } from './$types';
import { getProviderKey } from '#lib/server/credentials.js';
import { NarrationError, synthesizeNarration } from '#lib/server/elevenlabs.js';
import { getPreferences } from '#lib/server/preferences.js';

const Body = z.object({
	text: z.string().min(1).max(2500),
	previous_text: z.string().max(2000).nullish(),
	next_text: z.string().max(2000).nullish()
});

/** Narrates one passage with the learner's ElevenLabs key and returns audio plus word timings. */
export const POST: RequestHandler = async ({ request, locals }) => {
	if (!locals.user) error(401, 'Sign in to use narration');
	const parsed = Body.safeParse(await request.json().catch(() => null));
	if (!parsed.success) error(400, 'Text to narrate is required (up to 2,500 characters)');

	const apiKey = await getProviderKey(locals.user.id, 'elevenlabs');
	if (!apiKey) error(412, 'Add your ElevenLabs API key in Settings to use narration');
	const prefs = await getPreferences(locals.user.id);

	try {
		const clip = await synthesizeNarration({
			apiKey,
			text: parsed.data.text,
			previousText: parsed.data.previous_text,
			nextText: parsed.data.next_text,
			voiceId: prefs.narrationVoiceId,
			modelId: prefs.narrationModel,
			speed: prefs.narrationSpeed
		});
		return json(clip, { headers: { 'cache-control': 'no-store' } });
	} catch (e) {
		if (e instanceof NarrationError) error(e.status, e.message);
		throw e;
	}
};
