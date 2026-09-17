/**
 * Compiles the book into a runtime index for the reader and the tutor.
 *
 * Reads knowledge/book/outline.json (every chapter and section, written or not), the sections written so far in
 * knowledge/book/sections/<chapter>/<id>.json, the visual catalog in knowledge/visuals/*.json, and the concept
 * registries for titles. Writes src/lib/server/vault/generated/book.json.
 *
 * Internal fields never reach the runtime: provenance, review records and authoring sketches are dropped here, and
 * the check on that is in src/lib/server/book.spec.ts.
 *
 * Run: node scripts/build-book-index.ts
 */
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const KB = join(ROOT, 'knowledge');
const OUT = join(ROOT, 'src/lib/server/vault/generated/book.json');

type Json = Record<string, any>;
const readJson = (path: string): Json => JSON.parse(readFileSync(path, 'utf8'));

/** Fields that exist only for authors and reviewers. Nothing here is served. */
const DROP = new Set([
	'provenance',
	'review',
	'retired_ids',
	'starting_material',
	'design_rules',
	'sketch',
	'show'
]);

function strip<T>(value: T): T {
	if (Array.isArray(value)) return value.map(strip) as unknown as T;
	if (value && typeof value === 'object') {
		return Object.fromEntries(
			Object.entries(value as Json)
				.filter(([k]) => !DROP.has(k))
				.map(([k, v]) => [k, strip(v)])
		) as T;
	}
	return value;
}

const conceptTitles: Record<string, { title: string; domain: string; tier: string }> = {};
const conceptsDir = join(KB, 'concepts');
if (existsSync(conceptsDir)) {
	for (const domain of readdirSync(conceptsDir)) {
		const registry = join(conceptsDir, domain, '_registry.json');
		if (!existsSync(registry)) continue;
		for (const c of readJson(registry).concepts ?? [])
			conceptTitles[c.id] = { title: c.title, domain, tier: c.tier };
	}
}

/** Visual catalog entries, without the authoring model but with enough to describe the demo to a reader. */
const visuals: Json[] = [];
const visualsDir = join(KB, 'visuals');
if (existsSync(visualsDir)) {
	for (const file of readdirSync(visualsDir)) {
		if (!file.endsWith('.json')) continue;
		const v = readJson(join(visualsDir, file));
		visuals.push({
			id: v.id,
			title: v.title,
			kind: v.kind,
			priority: v.priority,
			status: v.status,
			rungs: v.rungs,
			caption: v.picture?.caption ?? '',
			makesVisible: v.makes_visible ?? '',
			serves: (v.serves ?? []).map((s: Json) => s.concept),
			counts: {
				params: (v.params ?? []).length,
				presets: (v.presets ?? []).length,
				readouts: (v.readouts ?? []).length,
				tours: (v.tours ?? []).length,
				tests: (v.model?.tests ?? []).length
			},
			reviewed: Boolean(v.review?.physics),
			accessibility: v.accessibility?.static_alt ?? null
		});
	}
}
const visualById = new Map(visuals.map((v) => [v.id, v]));

const outline = readJson(join(KB, 'book', 'outline.json'));
const sections: Json[] = [];
const parts: Json[] = [];
let written = 0;
let words = 0;

for (const part of outline.parts) {
	const chapters: Json[] = [];
	for (const chapter of part.chapters) {
		const list: Json[] = [];
		for (const s of chapter.sections) {
			const file = join(KB, 'book', 'sections', chapter.id, `${s.id}.json`);
			const has = existsSync(file);
			if (has) {
				const d = strip(readJson(file)) as Json;
				const prose = [d.opening, ...d.parts.map((p: Json) => `${p.text} ${p.takeaway}`)].join(' ');
				const count = prose.split(/\s+/).filter(Boolean).length;
				words += count;
				written += 1;
				sections.push({
					...d,
					chapterTitle: chapter.title,
					partTitle: part.title,
					words: count,
					teachesTitles: d.teaches.map((c: string) => ({
						id: c,
						...(conceptTitles[c] ?? { title: c, domain: '', tier: '' })
					})),
					visuals: (d.visuals ?? []).map((v: Json) => ({
						...v,
						catalog: visualById.get(v.id) ?? null
					}))
				});
			}
			list.push({
				id: s.id,
				title: s.title,
				track: s.track,
				depth: s.depth,
				concepts: s.concepts.length,
				written: has
			});
		}
		chapters.push({
			id: chapter.id,
			title: chapter.title,
			track: chapter.track,
			depth: chapter.depth,
			sections: list,
			written: list.filter((x) => x.written).length
		});
	}
	parts.push({ id: part.id, title: part.title, chapters });
}

const totals = {
	parts: parts.length,
	chapters: parts.reduce((n, p) => n + p.chapters.length, 0),
	sections: parts.reduce(
		(n, p) => n + p.chapters.reduce((m: number, c: Json) => m + c.sections.length, 0),
		0
	),
	written,
	words,
	concepts: Object.keys(conceptTitles).length,
	checks: sections.reduce((n, s) => n + s.checks.length, 0),
	visuals: visuals.length,
	visualsReviewed: visuals.filter((v) => v.reviewed).length
};

mkdirSync(dirname(OUT), { recursive: true });
writeFileSync(OUT, JSON.stringify({ totals, parts, sections, visuals }));
console.log(
	`book index: ${totals.written} of ${totals.sections} sections (${totals.words.toLocaleString()} words), ${visuals.length} visuals -> ${OUT}`
);
