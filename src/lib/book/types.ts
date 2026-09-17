/** Types for the compiled book index (scripts/build-book-index.ts). Shared by the reader pages and the tutor. */

export type Track = 'main' | 'advanced' | 'reference';
export type Depth = 'entry' | 'working' | 'formal' | 'research';

export interface SectionStub {
	id: string;
	title: string;
	track: Track;
	depth: Depth;
	concepts: number;
	written: boolean;
}

export interface ChapterSummary {
	id: string;
	title: string;
	track: Track;
	depth: Depth;
	sections: SectionStub[];
	written: number;
}

export interface PartSummary {
	id: string;
	title: string;
	chapters: ChapterSummary[];
}

export interface VisualSummary {
	id: string;
	title: string;
	kind: string;
	priority: 'flagship' | 'core' | 'supporting';
	status: string;
	rungs: Depth[];
	caption: string;
	makesVisible: string;
	serves: string[];
	counts: { params: number; presets: number; readouts: number; tours: number; tests: number };
	reviewed: boolean;
	accessibility: string | null;
}

export interface SectionPart {
	id: string;
	heading: string;
	teaches: string[];
	text: string;
	takeaway: string;
}

export interface Equation {
	id: string;
	name: string;
	latex: string;
	meaning: string;
	symbols: { symbol: string; meaning: string; say: string }[];
	say_aloud: string;
	justified: 'derived-here' | 'earlier-section' | 'stated';
}

export interface Check {
	id: string;
	format: string;
	question: string;
	question_spoken: string | null;
	answer: string;
	key_points: string[];
	numeric: { quantity: string; value: number; unit: string | null }[] | null;
	targets: string[];
}

export interface Section {
	id: string;
	chapter: string;
	chapterTitle: string;
	partTitle: string;
	title: string;
	track: Track;
	depth: Depth;
	status: string;
	revision: number;
	updated: string;
	words: number;
	teaches: string[];
	teachesTitles: { id: string; title: string; domain: string; tier: string }[];
	builds_on: string[];
	summary: string;
	opening: string;
	parts: SectionPart[];
	key_equations: Equation[];
	worked_examples: {
		id: string;
		problem: string;
		steps: string[];
		answer: string;
		takeaway: string;
	}[];
	checks: Check[];
	misconceptions: { id: string; belief: string; correction: string; diagnosed_by: string[] }[];
	glossary: { id: string; term: string; plain_definition: string; concept: string | null }[];
	visuals: { id: string; role: string; priority: string; catalog: VisualSummary | null }[];
	tutor: {
		opening_question: string;
		common_questions: { id: string; question: string; answer: string }[];
	};
	further: { id: string; topic: string; note: string; references: Record<string, unknown>[] }[];
}

export interface BookTotals {
	parts: number;
	chapters: number;
	sections: number;
	written: number;
	words: number;
	concepts: number;
	checks: number;
	visuals: number;
	visualsReviewed: number;
}

export interface BookIndex {
	totals: BookTotals;
	parts: PartSummary[];
	sections: Section[];
	visuals: VisualSummary[];
}

export const DEPTH_LABEL: Record<Depth, string> = {
	entry: 'From scratch',
	working: 'Undergraduate',
	formal: 'Graduate',
	research: 'Research'
};

export const DEPTH_BLURB: Record<Depth, string> = {
	entry: 'No calculus, no physics background: words, pictures and arithmetic.',
	working: 'Calculus, vectors and matrices, with every algebra step shown.',
	formal: 'Precise definitions, hypotheses and proof sketches.',
	research: 'Modern formulations, open problems and the literature.'
};
