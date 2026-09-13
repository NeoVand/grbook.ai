import OpenAI from 'openai';
import { error, json } from '@sveltejs/kit';
import { z } from 'zod';
import type { RequestHandler } from './$types';
import { db } from '#lib/server/db/index.js';
import { tutorSession } from '#lib/server/db/schema.js';
import { getProviderKey } from '#lib/server/credentials.js';
import { getPreferences } from '#lib/server/preferences.js';
import { learnerSummary } from '#lib/server/learner.js';
import { buildTutorSession } from '#lib/server/tutor/session-config.js';

const Body = z.object({
	sdp: z.string().min(1).max(64_000),
	reading_context: z.string().max(2000).nullish()
});

/**
 * Creates a GPT-Live WebRTC session with the signed-in user's stored OpenAI key. The browser sends only its SDP
 * offer; the session configuration is built on the server and the key never leaves it.
 */
export const POST: RequestHandler = async ({ request, locals, url }) => {
	if (!locals.user) error(401, 'Sign in to talk with the tutor');
	const origin = request.headers.get('origin');
	if (origin && origin !== url.origin) error(403, 'Cross-origin requests are not allowed');

	const parsed = Body.safeParse(await request.json().catch(() => null));
	if (!parsed.success) error(400, 'A WebRTC SDP offer is required');

	const apiKey = await getProviderKey(locals.user.id, 'openai');
	if (!apiKey) error(412, 'Add your OpenAI API key in Settings to use the voice tutor');

	const [prefs, summary] = await Promise.all([getPreferences(locals.user.id), learnerSummary(locals.user.id)]);
	const readingContext = parsed.data.reading_context ?? null;

	let result;
	try {
		result = await new OpenAI({ apiKey, maxRetries: 0 }).live.create({
			session: buildTutorSession({ voice: prefs.tutorVoice, learnerSummary: summary, readingContext }),
			transport: { type: 'webrtc', sdp: parsed.data.sdp }
		});
	} catch (e) {
		if (e instanceof OpenAI.APIError) {
			if (e.status === 401) error(401, 'OpenAI rejected the API key');
			if (e.status === 429) error(429, 'OpenAI rate limit or quota reached');
			error(502, 'Could not start a voice session');
		}
		throw e;
	}

	await db.insert(tutorSession).values({ userId: locals.user.id, liveSessionId: result.session.id, context: { readingContext } });
	return json(
		{ session: { id: result.session.id }, transport: { sdp: result.transport.sdp } },
		{ status: 201, headers: { 'cache-control': 'no-store' } }
	);
};
