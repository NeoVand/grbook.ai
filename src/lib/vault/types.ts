/** Types shared by the server vault loader, the tutor tools, and the study pages. */

export const BOOK_IDS = ['schutz', 'gifted-amateur', 'dinverno'] as const;
export type BookId = (typeof BOOK_IDS)[number];

export const BOOK_SHORT: Record<BookId, string> = { schutz: 'SCH', 'gifted-amateur': 'GA', dinverno: 'DIV' };

export const ENTRY_KINDS = ['unit', 'concept', 'equation', 'misconception', 'analogy', 'example', 'figure', 'registry-concept'] as const;
export type EntryKind = (typeof ENTRY_KINDS)[number];

export interface Locator {
	book: string;
	unit: string;
	section: string | null;
	printedPage: number | null;
	pdfPage: number | null;
}

export interface VaultEntry {
	id: string;
	kind: EntryKind;
	title: string;
	text: string;
	book: string | null;
	unit: string | null;
	locator: Locator | null;
	extra?: Record<string, unknown>;
}

export interface UnitSummary {
	id: string;
	label: string;
	kind: 'chapter' | 'appendix';
	title: string;
	part: string | null;
	printedPages: [number, number];
	sections: { number: string; title: string; printedPage: number }[];
	hasDossier: boolean;
	verified: boolean;
	verdict?: string | null;
	summary?: string;
	difficulty?: { math_level: number; conceptual_level: number; novice_friendliness: number; notes: string };
	styleTags?: string[];
	conceptCount?: number;
	figureCount?: number;
}

export interface BookSummary {
	id: BookId;
	short: string;
	title: string;
	authors: string[];
	edition: string;
	units: UnitSummary[];
}

export interface DossierLocator {
	pdf_page: number;
	printed_page?: number | null;
	section?: string | null;
}

/** The subset of the chapter dossier schema the app renders. See knowledge/_schemas/chapter-dossier.schema.json. */
export interface Dossier {
	book: BookId;
	unit_id: string;
	title: string;
	part?: string | null;
	printed_pages: (number | null)[];
	pdf_pages: number[];
	one_line_summary: string;
	role_in_book: string;
	learning_objectives: string[];
	assumed_background: { topic: string; source: string; where?: string | null }[];
	teaching_approach: { summary: string; style_tags: string[]; narrative_arc: string[]; signature_moves: string[] };
	sections: { number: string | null; title: string; printed_page?: number | null; pdf_page: number; summary: string; concepts: string[]; key_moves: string[] }[];
	concepts: {
		name: string;
		aliases: string[];
		kind: string;
		definition: string;
		how_introduced: string;
		depth: string;
		prerequisites: string[];
		locators: DossierLocator[];
		formulas: string[];
		notes?: string | null;
	}[];
	key_equations: { label: string | null; name?: string | null; latex: string; meaning: string; symbols?: string | null; importance: string; locator: DossierLocator }[];
	figures: {
		label: string | null;
		locator: DossierLocator;
		caption_paraphrase: string;
		visual_description: string;
		what_it_teaches: string;
		figure_type: string;
		concepts: string[];
		redesign: { idea: string; interaction: string; form: string; priority: string };
	}[];
	worked_examples: { label: string | null; locator: DossierLocator; problem: string; method: string; key_insight: string; result?: string | null; concepts: string[]; difficulty: string }[];
	analogies_and_intuitions: { analogy: string; target_concept: string; how_used: string; limits: string; locator: DossierLocator; effectiveness: string; app_idea?: string | null }[];
	misconceptions_addressed: { misconception: string; correction: string; why_tempting: string; locator: DossierLocator; concepts: string[] }[];
	thought_experiments: { name: string; setup: string; lesson: string; locator: DossierLocator; concepts: string[]; visualizable: boolean; app_idea?: string | null }[];
	applications_and_observations: { topic: string; kind: string; details: string; key_numbers?: string | null; locator: DossierLocator }[];
	historical_notes: { people: string[]; year: string | null; event: string; significance: string; locator: DossierLocator }[];
	notation_and_conventions: { item: string; convention: string; notes?: string | null; locator: DossierLocator }[];
	exercises: { count_estimate: number; skills_practiced: string[]; notable: { number: string; summary: string; skills: string[]; difficulty: string; why_notable: string }[] };
	difficulty: { math_level: number; conceptual_level: number; novice_friendliness: number; notes: string };
	teaching_gems: { gem: string; why_effective: string; locator: DossierLocator; app_idea: string }[];
	gaps_and_pitfalls: { issue: string; impact_on_learner: string; suggestion: string }[];
	tutor_notes: string[];
	verification?: { verdict: string; fixes: string[]; residual_concerns: string[] };
}

/** "SCH §5.3 p.125" */
export function formatLocator(book: string, loc: { section?: string | null; printedPage?: number | null; printed_page?: number | null } | null): string {
	const short = BOOK_SHORT[book as BookId] ?? book;
	if (!loc) return short;
	const page = loc.printedPage ?? loc.printed_page;
	return [short, loc.section ? `§${loc.section}` : null, page != null ? `p.${page}` : null].filter(Boolean).join(' ');
}
