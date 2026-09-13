import { error, json } from '@sveltejs/kit';
import { and, eq, isNull } from 'drizzle-orm';
import { z } from 'zod';
import type { RequestHandler } from './$types';
import { db } from '#lib/server/db/index.js';
import { tutorSession } from '#lib/server/db/schema.js';

const Body = z.object({
	live_session_id: z.string().min(1).max(200),
	usage_seconds: z.number().int().min(0).max(24 * 3600).nullish(),
	summary: z.string().max(2000).nullish()
});

/** Marks a tutor session as ended, with usage and an optional summary for the next session. */
export const POST: RequestHandler = async ({ request, locals }) => {
	if (!locals.user) error(401, 'Not signed in');
	const parsed = Body.safeParse(await request.json().catch(() => null));
	if (!parsed.success) error(400, 'Invalid session end payload');
	const { live_session_id, usage_seconds, summary } = parsed.data;
	await db
		.update(tutorSession)
		.set({ endedAt: new Date(), usageSeconds: usage_seconds ?? null, summary: summary ?? null })
		.where(and(eq(tutorSession.userId, locals.user.id), eq(tutorSession.liveSessionId, live_session_id), isNull(tutorSession.endedAt)));
	return json({ ok: true });
};
