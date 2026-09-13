import { db } from '#lib/server/db/index.js';
import { learningEvent } from '#lib/server/db/schema.js';
import { getDossier, getEntry, searchKnowledge, UNIT_ID } from '#lib/server/vault/index.js';
import { TOOL_DEFINITIONS, isToolName, toolArgs, type ToolResult } from '#lib/tutor/tools.js';
import { formatLocator } from '#lib/vault/types.js';

export interface ToolContext {
	userId: string;
	callId: string | null;
}

const SERVER_TOOLS = new Set(TOOL_DEFINITIONS.filter((t) => t.runner === 'server').map((t) => t.name));

/** Executes a server-side tutor tool. Never throws for bad input; returns { ok: false, reason } instead. */
export async function runServerTool(name: string, rawArgs: unknown, ctx: ToolContext): Promise<ToolResult> {
	if (!isToolName(name) || !SERVER_TOOLS.has(name)) return { ok: false, reason: `Unknown server tool "${name}"` };
	const parsed = toolArgs[name].safeParse(rawArgs);
	if (!parsed.success) return { ok: false, reason: `Invalid arguments: ${parsed.error.issues.map((i) => i.message).join('; ')}` };
	const args = parsed.data as Record<string, unknown>;

	switch (name) {
		case 'search_knowledge': {
			const query = String(args.query ?? '').slice(0, 200);
			if (query.trim().length < 2) return { ok: false, reason: 'Query is too short' };
			const results = searchKnowledge({
				query,
				kinds: args.kinds as never,
				book: args.book as string | null,
				unit: args.unit_id as string | null,
				limit: Math.min(Math.max(Number(args.limit ?? 5), 1), 8)
			});
			return {
				ok: true,
				results: results.map((e) => ({
					id: e.id,
					kind: e.kind,
					title: e.title,
					summary: e.text,
					where: e.book ? formatLocator(e.book, e.locator) : null
				}))
			};
		}
		case 'get_knowledge_entry': {
			const entry = getEntry(String(args.id));
			if (!entry) return { ok: false, reason: 'No entry with that id' };
			return { ok: true, entry: { ...entry, where: entry.book ? formatLocator(entry.book, entry.locator) : null } };
		}
		case 'get_unit_notes': {
			const unitId = String(args.unit_id);
			if (!UNIT_ID.test(unitId)) return { ok: false, reason: 'Unit ids look like ch05 or appB' };
			const dossier = await getDossier(String(args.book), unitId);
			if (!dossier) return { ok: false, reason: 'No notes for that unit yet' };
			const fields = (args.fields as string[] | null) ?? ['one_line_summary', 'learning_objectives', 'tutor_notes'];
			const picked: Record<string, unknown> = { title: dossier.title, unit: `${dossier.book}/${dossier.unit_id}` };
			for (const f of fields) picked[f] = (dossier as unknown as Record<string, unknown>)[f];
			return { ok: true, notes: picked };
		}
		case 'record_learning_evidence': {
			await db
				.insert(learningEvent)
				.values({
					userId: ctx.userId,
					kind: args.kind as 'asked',
					subjectType: args.subject_type as 'unit',
					subjectId: String(args.subject_id).slice(0, 200),
					payload: { note: String(args.note).slice(0, 500), source: 'tutor' },
					idempotencyKey: ctx.callId ? `tutor:${ctx.callId}` : null
				})
				.onConflictDoNothing();
			return { ok: true, recorded: true };
		}
		default:
			return { ok: false, reason: `Tool "${name}" does not run on the server` };
	}
}
