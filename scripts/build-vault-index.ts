/**
 * Compiles the knowledge vault into a compact runtime index for the app and the tutor's knowledge tools.
 *
 * Reads knowledge/sources/<book>/{toc.json,chapters/*.json} and, when present, knowledge/concepts/<domain>/_registry.json.
 * Writes src/lib/server/vault/generated/index.json. Never reads book-sources/ (copyrighted, never deployed).
 *
 * Run: node scripts/build-vault-index.ts
 */
import { mkdirSync, readdirSync, readFileSync, existsSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const KB = join(ROOT, 'knowledge');
const OUT = join(ROOT, 'src/lib/server/vault/generated/index.json');
const BOOKS = ['schutz', 'gifted-amateur', 'dinverno'] as const;
const SHORT: Record<string, string> = { schutz: 'SCH', 'gifted-amateur': 'GA', dinverno: 'DIV' };

type Json = Record<string, any>;

interface Locator {
	book: string;
	unit: string;
	section: string | null;
	printedPage: number | null;
	pdfPage: number | null;
}

interface Entry {
	id: string;
	kind: 'unit' | 'concept' | 'equation' | 'misconception' | 'analogy' | 'example' | 'figure' | 'registry-concept';
	title: string;
	text: string;
	book: string | null;
	unit: string | null;
	locator: Locator | null;
	extra?: Json;
}

const readJson = (path: string): Json => JSON.parse(readFileSync(path, 'utf8'));

function clip(text: string | null | undefined, max = 420): string {
	const s = (text ?? '').replace(/\s+/g, ' ').trim();
	return s.length <= max ? s : `${s.slice(0, max - 1).trimEnd()}…`;
}

function locator(book: string, unit: string, l: Json | null | undefined): Locator | null {
	if (!l) return null;
	return { book, unit, section: l.section ?? null, printedPage: l.printed_page ?? null, pdfPage: l.pdf_page ?? null };
}

function slug(s: string): string {
	return s
		.toLowerCase()
		.replace(/[^a-z0-9]+/g, '-')
		.replace(/^-|-$/g, '')
		.slice(0, 60);
}

const books: Json[] = [];
const entries: Entry[] = [];

for (const book of BOOKS) {
	const toc = readJson(join(KB, 'sources', book, 'toc.json'));
	const chaptersDir = join(KB, 'sources', book, 'chapters');
	const units: Json[] = [];
	for (const u of toc.units) {
		if (u.kind === 'front-matter' || !u.read) continue;
		const file = join(chaptersDir, `${u.id}.json`);
		const unitInfo: Json = {
			id: u.id,
			label: u.label,
			kind: u.kind,
			title: u.title,
			part: u.part?.title ?? null,
			printedPages: u.printed_pages,
			sections: (u.sections ?? []).map((s: Json) => ({ number: s.number, title: s.title, printedPage: s.printed_page })),
			hasDossier: false,
			verified: false
		};
		if (existsSync(file)) {
			let d: Json;
			try {
				d = readJson(file);
			} catch {
				units.push(unitInfo);
				continue;
			}
			const verdict = d.verification?.verdict ?? null;
			Object.assign(unitInfo, {
				hasDossier: true,
				verified: Boolean(verdict),
				verdict,
				summary: d.one_line_summary,
				difficulty: d.difficulty,
				styleTags: d.teaching_approach?.style_tags ?? [],
				conceptCount: d.concepts?.length ?? 0,
				figureCount: d.figures?.length ?? 0
			});
			const base = `${book}/${u.id}`;
			entries.push({
				id: `unit:${base}`,
				kind: 'unit',
				title: `${SHORT[book]} ${u.id} · ${d.title}`,
				text: clip(`${d.one_line_summary} ${d.role_in_book}`),
				book,
				unit: u.id,
				locator: locator(book, u.id, { pdf_page: d.pdf_pages?.[0], printed_page: d.printed_pages?.[0] })
			});
			for (const c of d.concepts ?? []) {
				entries.push({
					id: `concept:${base}:${slug(c.name)}`,
					kind: 'concept',
					title: c.name,
					text: clip(`${c.definition} ${c.how_introduced}`),
					book,
					unit: u.id,
					locator: locator(book, u.id, c.locators?.[0]),
					extra: { aliases: c.aliases ?? [], depth: c.depth, kind: c.kind }
				});
			}
			(d.key_equations ?? []).forEach((e: Json, i: number) => {
				entries.push({
					id: `equation:${base}:${i}`,
					kind: 'equation',
					title: [e.label, e.name].filter(Boolean).join(' ') || 'Equation',
					text: clip(e.meaning, 300),
					book,
					unit: u.id,
					locator: locator(book, u.id, e.locator),
					extra: { latex: e.latex, symbols: e.symbols ?? null, importance: e.importance }
				});
			});
			(d.misconceptions_addressed ?? []).forEach((m: Json, i: number) => {
				entries.push({
					id: `misconception:${base}:${i}`,
					kind: 'misconception',
					title: clip(m.misconception, 160),
					text: clip(`${m.correction} Why tempting: ${m.why_tempting}`),
					book,
					unit: u.id,
					locator: locator(book, u.id, m.locator),
					extra: { concepts: m.concepts ?? [] }
				});
			});
			(d.analogies_and_intuitions ?? []).forEach((a: Json, i: number) => {
				entries.push({
					id: `analogy:${base}:${i}`,
					kind: 'analogy',
					title: `${a.analogy} → ${a.target_concept}`,
					text: clip(`${a.how_used} Limits: ${a.limits}`),
					book,
					unit: u.id,
					locator: locator(book, u.id, a.locator),
					extra: { effectiveness: a.effectiveness }
				});
			});
			(d.worked_examples ?? []).forEach((x: Json, i: number) => {
				entries.push({
					id: `example:${base}:${i}`,
					kind: 'example',
					title: x.label ? `${x.label}: ${clip(x.problem, 100)}` : clip(x.problem, 120),
					text: clip(`${x.problem} Insight: ${x.key_insight}`),
					book,
					unit: u.id,
					locator: locator(book, u.id, x.locator),
					extra: { difficulty: x.difficulty }
				});
			});
			(d.figures ?? []).forEach((f: Json, i: number) => {
				entries.push({
					id: `figure:${base}:${i}`,
					kind: 'figure',
					title: `${f.label ?? 'Figure'} (${f.figure_type})`,
					text: clip(`${f.what_it_teaches} Demo idea: ${f.redesign?.idea ?? ''}`),
					book,
					unit: u.id,
					locator: locator(book, u.id, f.locator),
					extra: { priority: f.redesign?.priority ?? null, form: f.redesign?.form ?? null }
				});
			});
		}
		units.push(unitInfo);
	}
	books.push({ id: book, short: SHORT[book], title: toc.book.title, authors: toc.book.authors, edition: toc.book.edition, units });
}

const conceptsDir = join(KB, 'concepts');
if (existsSync(conceptsDir)) {
	for (const domain of readdirSync(conceptsDir)) {
		const registry = join(conceptsDir, domain, '_registry.json');
		if (!existsSync(registry)) continue;
		for (const c of readJson(registry).concepts ?? []) {
			entries.push({
				id: `registry:${c.id}`,
				kind: 'registry-concept',
				title: c.title,
				text: clip(c.summary),
				book: null,
				unit: null,
				locator: null,
				extra: { domain, tier: c.tier, aliases: c.aliases ?? [], prerequisites: c.prerequisites ?? [] }
			});
		}
	}
}

mkdirSync(dirname(OUT), { recursive: true });
writeFileSync(OUT, JSON.stringify({ books, entries }));
const dossiers = books.reduce((n, b) => n + b.units.filter((u: Json) => u.hasDossier).length, 0);
console.log(`vault index: ${books.length} books, ${dossiers} dossiers, ${entries.length} entries -> ${OUT}`);
