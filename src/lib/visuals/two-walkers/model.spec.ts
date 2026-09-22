import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import {
	DEFAULTS,
	PRESETS,
	readouts,
	visibleReadouts,
	type Readouts,
	type State
} from './model.js';

/**
 * The demo's contract lives in the vault, not here: this runs every numerical test the visual's catalog entry
 * declares. A change to the model that breaks what the book promises fails the build.
 */
const spec = JSON.parse(
	readFileSync('knowledge/visuals/two-walkers-set-off-side-by-side.json', 'utf8')
);

const READOUT_KEY: Record<string, keyof Readouts> = {
	gap: 'gap',
	'gap-change': 'gapChange',
	'gap-share': 'gapShare',
	'extra-share': 'extraShare',
	'along-path-part': 'alongPathPart',
	'string-length': 'stringLength'
};

/** Turns a test's declared state (a preset plus overrides) into the model's state. */
function stateOf(declared: Record<string, unknown>): State {
	const state: State = { ...DEFAULTS, ...(PRESETS[declared.preset as string] ?? {}) };
	if ('world' in declared) state.world = declared.world as State['world'];
	if ('gap-m' in declared) state.gap = declared['gap-m'] as number;
	if ('gap-cm' in declared) state.gap = (declared['gap-cm'] as number) / 100;
	if ('head-start-m' in declared) state.headStart = declared['head-start-m'] as number;
	if ('start-circle' in declared)
		state.startCircle = declared['start-circle'] as State['startCircle'];
	if ('stretches' in declared) state.stretches = declared.stretches as number;
	if ('progress' in declared) state.progress = declared.progress as number;
	return state;
}

describe('two walkers set off side by side', () => {
	const tests = spec.model.tests as {
		id: string;
		state: Record<string, unknown>;
		expect: { readout: string; value: number; abs_tol: number | null; rel_tol: number | null }[];
		expect_hidden: string[];
		note: string;
	}[];

	it('declares tests to run', () => expect(tests.length).toBeGreaterThan(15));

	for (const t of tests) {
		it(t.id, () => {
			const state = stateOf(t.state);
			const values = readouts(state);
			for (const e of t.expect) {
				const key = READOUT_KEY[e.readout];
				expect(key, `unknown readout ${e.readout}`).toBeDefined();
				const got = values[key] as number;
				const tolerance = e.abs_tol ?? Math.abs(e.value * (e.rel_tol ?? 0));
				expect(
					Math.abs(got - e.value),
					`${e.readout}: expected ${e.value}, got ${got}`
				).toBeLessThanOrEqual(tolerance + 1e-12);
			}
			const shown = visibleReadouts(state);
			for (const hidden of t.expect_hidden) expect(shown.has(READOUT_KEY[hidden])).toBe(false);
		});
	}
});
