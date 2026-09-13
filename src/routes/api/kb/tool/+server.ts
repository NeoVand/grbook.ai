import { error, json } from '@sveltejs/kit';
import { z } from 'zod';
import type { RequestHandler } from './$types';
import { runServerTool } from '#lib/server/tutor/kb-tools.js';

const Body = z.object({
	name: z.string().min(1).max(64),
	arguments: z.union([z.string().max(20_000), z.record(z.string(), z.unknown())]),
	call_id: z.string().max(200).nullish()
});

/** Executes a server-side tutor tool for the signed-in learner. Read-only except learning evidence. */
export const POST: RequestHandler = async ({ request, locals, url }) => {
	if (!locals.user) error(401, 'Not signed in');
	const origin = request.headers.get('origin');
	if (origin && origin !== url.origin) error(403, 'Cross-origin requests are not allowed');

	const parsed = Body.safeParse(await request.json().catch(() => null));
	if (!parsed.success) return json({ ok: false, reason: 'Invalid tool request' }, { status: 400 });

	let args: unknown = parsed.data.arguments;
	if (typeof args === 'string') {
		try {
			args = JSON.parse(args);
		} catch {
			return json({ ok: false, reason: 'Tool arguments are not valid JSON' });
		}
	}

	const result = await runServerTool(parsed.data.name, args, { userId: locals.user.id, callId: parsed.data.call_id ?? null });
	return json(result, { headers: { 'cache-control': 'no-store' } });
};
