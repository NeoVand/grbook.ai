import { z } from 'zod';
import { BOOK_IDS, ENTRY_KINDS } from '#lib/vault/types.js';

/**
 * The single registry of tutor tools. Each tool's zod schema generates the JSON Schema sent to GPT-Live's
 * Responses backend and validates arguments wherever the tool runs.
 *
 * `client` tools run in the browser (reader and lab state, navigation). `server` tools run through
 * POST /api/kb/tool with the signed-in user and never see a provider key.
 */

const LEARNING_SUBJECTS = ['unit', 'concept', 'lesson', 'lab', 'equation'] as const;
const EVIDENCE_KINDS = ['asked', 'attempted', 'demonstrated', 'misconception'] as const;
const DOSSIER_FIELDS = [
	'one_line_summary',
	'role_in_book',
	'learning_objectives',
	'assumed_background',
	'teaching_approach',
	'sections',
	'concepts',
	'key_equations',
	'worked_examples',
	'analogies_and_intuitions',
	'misconceptions_addressed',
	'thought_experiments',
	'teaching_gems',
	'gaps_and_pitfalls',
	'tutor_notes'
] as const;

export const toolArgs = {
	get_reading_context: z.strictObject({}),
	show_in_reader: z.strictObject({
		book: z.enum(BOOK_IDS).describe('Book id'),
		unit_id: z.string().describe('Unit id such as ch05 or appB'),
		section: z.string().nullable().describe('Section number such as 5.3, or null for the unit start'),
		highlight: z.string().nullable().describe('Short phrase or concept name to highlight, or null')
	}),
	search_knowledge: z.strictObject({
		query: z.string().describe('What to look for, in plain words'),
		kinds: z.array(z.enum(ENTRY_KINDS)).nullable().describe('Restrict to these entry kinds, or null for all'),
		book: z.enum(BOOK_IDS).nullable().describe('Restrict to one book, or null'),
		unit_id: z.string().nullable().describe('Restrict to one unit (requires book), or null'),
		limit: z.number().int().nullable().describe('Maximum results, 1 to 8; null means 5')
	}),
	get_knowledge_entry: z.strictObject({
		id: z.string().describe('An entry id returned by search_knowledge')
	}),
	get_unit_notes: z.strictObject({
		book: z.enum(BOOK_IDS),
		unit_id: z.string().describe('Unit id such as ch05'),
		fields: z.array(z.enum(DOSSIER_FIELDS)).nullable().describe('Fields to return; null returns a compact overview')
	}),
	record_learning_evidence: z.strictObject({
		subject_type: z.enum(LEARNING_SUBJECTS),
		subject_id: z.string().describe('For a unit use "<book>/<unit>", for a concept its name or registry id'),
		kind: z.enum(EVIDENCE_KINDS),
		note: z.string().describe('One sentence describing what the learner did or showed')
	})
} as const;

export type ToolName = keyof typeof toolArgs;
export type ToolArgs<N extends ToolName> = z.infer<(typeof toolArgs)[N]>;

export interface ToolDefinition {
	name: ToolName;
	runner: 'client' | 'server';
	description: string;
}

export const TOOL_DEFINITIONS: ToolDefinition[] = [
	{
		name: 'get_reading_context',
		runner: 'client',
		description:
			'Returns what the learner is looking at right now: book, unit, section, visible equations, selected text, and any open demo with its parameters. Call it before answering about "this", "here", or the current page.'
	},
	{
		name: 'show_in_reader',
		runner: 'client',
		description: 'Opens a unit in the reader, scrolls to a section, and highlights a phrase, so the page follows the conversation.'
	},
	{
		name: 'search_knowledge',
		runner: 'server',
		description:
			'Searches the course knowledge base: original teaching notes on three general relativity textbooks, covering concepts, equations, worked examples, misconceptions, analogies, and figure or demo ideas. Returns short summaries with ids and page locators.'
	},
	{
		name: 'get_knowledge_entry',
		runner: 'server',
		description: 'Returns the full record for one search result id, including LaTeX for equations and aliases for concepts.'
	},
	{
		name: 'get_unit_notes',
		runner: 'server',
		description:
			'Returns selected teaching notes for one textbook unit: learning objectives, teaching approach, concepts, key equations, worked examples, misconceptions, tutor notes, and more.'
	},
	{
		name: 'record_learning_evidence',
		runner: 'server',
		description:
			"Records evidence about the learner's understanding for their learning history: a question they asked, an attempt, a demonstrated understanding, or a misconception you observed. Record only what actually happened."
	}
];

/** JSON Schema for a tool's arguments in the shape GPT-Live function tools expect. */
export function toolParameters(name: ToolName): Record<string, unknown> {
	const schema = z.toJSONSchema(toolArgs[name], { target: 'draft-7' }) as Record<string, unknown>;
	delete schema.$schema;
	return schema;
}

export function liveFunctionTools() {
	return TOOL_DEFINITIONS.map((t) => ({
		type: 'function' as const,
		name: t.name,
		description: t.description,
		parameters: toolParameters(t.name),
		strict: true
	}));
}

export function isToolName(name: string): name is ToolName {
	return Object.hasOwn(toolArgs, name);
}

export type ToolResult = { ok: true; [key: string]: unknown } | { ok: false; reason: string };
