import { describe, expect, it } from 'vitest';
import { TOOL_DEFINITIONS, liveFunctionTools, toolArgs, toolParameters, type ToolName } from './tools';
import { ALLOWED_CLIENT_EVENTS, buildTutorSession } from '#lib/server/tutor/session-config.js';

describe('tutor tool registry', () => {
	it('defines every tool exactly once', () => {
		const names = TOOL_DEFINITIONS.map((t) => t.name);
		expect(new Set(names).size).toBe(names.length);
		expect([...names].sort()).toEqual(Object.keys(toolArgs).sort());
	});

	it('produces strict-mode compatible schemas', () => {
		for (const name of Object.keys(toolArgs) as ToolName[]) {
			const schema = toolParameters(name) as { type: string; properties?: Record<string, unknown>; required?: string[]; additionalProperties?: boolean; $schema?: string };
			expect(schema.type).toBe('object');
			expect(schema.additionalProperties).toBe(false);
			expect(schema.$schema).toBeUndefined();
			expect([...(schema.required ?? [])].sort()).toEqual(Object.keys(schema.properties ?? {}).sort());
		}
	});

	it('validates arguments', () => {
		expect(toolArgs.search_knowledge.safeParse({ query: 'tidal forces', kinds: null, book: null, unit_id: null, limit: 3 }).success).toBe(true);
		expect(toolArgs.search_knowledge.safeParse({ query: 'x', kinds: ['nonsense'], book: null, unit_id: null, limit: 3 }).success).toBe(false);
		expect(toolArgs.get_knowledge_entry.safeParse({ id: 'a', extra: true }).success).toBe(false);
	});
});

describe('tutor session configuration', () => {
	it('delegates to a Responses backend with the registered tools', () => {
		const session = buildTutorSession({ voice: 'cedar', learnerSummary: 'Recently studied: schutz/ch05.', readingContext: null });
		expect(session.model).toBe('gpt-live-1');
		expect(session.store).toBe(false);
		expect(session.audio?.output?.voice).toBe('cedar');
		expect(session.client?.data_channel.allowed_client_events).toEqual(ALLOWED_CLIENT_EVENTS);
		const delegation = session.delegation as { type: string; responses: { tools: unknown[]; parallel_tool_calls: boolean } };
		expect(delegation.type).toBe('responses');
		expect(delegation.responses.tools).toHaveLength(liveFunctionTools().length);
		expect(session.input?.[0]).toMatchObject({ role: 'developer' });
	});

	it('omits startup history when there is nothing to say', () => {
		expect(buildTutorSession({}).input).toBeUndefined();
	});
});
