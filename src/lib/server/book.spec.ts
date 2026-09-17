import { describe, expect, it } from 'vitest';
import book from './vault/generated/book.json' with { type: 'json' };

/** The runtime must never serve author-only material, and must never mention the source textbooks. */
describe('compiled book index', () => {
	const json = JSON.stringify(book);

	it('drops internal fields', () => {
		for (const field of [
			'provenance',
			'"review"',
			'starting_material',
			'retired_ids',
			'"sketch"'
		]) {
			expect(json).not.toContain(field);
		}
	});

	it('never names a source book', () => {
		for (const name of [
			'Schutz',
			'Blundell',
			"d'Inverno",
			'Gifted Amateur',
			'dinverno',
			'gifted-amateur'
		]) {
			expect(json.toLowerCase()).not.toContain(name.toLowerCase());
		}
	});

	it('keeps every outline section, written or not', () => {
		const listed = book.parts.flatMap((p) => p.chapters.flatMap((c) => c.sections));
		expect(listed.length).toBe(book.totals.sections);
		expect(listed.filter((s) => s.written).length).toBe(book.totals.written);
		expect(book.sections.length).toBe(book.totals.written);
	});

	it('gives every written section the prose a reader needs', () => {
		for (const s of book.sections) {
			expect(s.summary.length).toBeGreaterThan(40);
			expect(s.parts.length).toBeGreaterThanOrEqual(2);
			expect(s.words).toBeGreaterThan(500);
			for (const p of s.parts) expect(p.text.length).toBeGreaterThan(100);
		}
	});
});
