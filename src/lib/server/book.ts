import raw from './vault/generated/book.json';
import type { BookIndex, ChapterSummary, Section } from '#lib/book/types.js';

/** The compiled book: the outline of every chapter, the sections written so far, and the visual catalog. Server only. */
const book = raw as unknown as BookIndex;

const sectionById = new Map(book.sections.map((s) => [s.id, s]));
const chapters: ChapterSummary[] = book.parts.flatMap((p) => p.chapters);

export const totals = book.totals;
export const parts = book.parts;
export const visuals = book.visuals;

export function getChapter(id: string): ChapterSummary | null {
	return chapters.find((c) => c.id === id) ?? null;
}

export function getSection(id: string): Section | null {
	return sectionById.get(id) ?? null;
}

/** The section's neighbours in reading order, skipping anything not written yet. */
export function neighbours(id: string): { prev: Section | null; next: Section | null } {
	const order = book.parts.flatMap((p) =>
		p.chapters.flatMap((c) => c.sections.filter((s) => s.written).map((s) => s.id))
	);
	const i = order.indexOf(id);
	return {
		prev: i > 0 ? (sectionById.get(order[i - 1]) ?? null) : null,
		next: i >= 0 && i < order.length - 1 ? (sectionById.get(order[i + 1]) ?? null) : null
	};
}

/** Sections that teach a registry concept, for the tutor and for concept links. */
export function sectionsTeaching(conceptId: string): Section[] {
	return book.sections.filter((s) => s.teaches.includes(conceptId));
}
