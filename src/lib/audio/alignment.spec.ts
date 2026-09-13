import { describe, expect, it } from 'vitest';
import { wordAt, wordsFromAlignment } from './alignment';

function alignmentFor(text: string, step = 0.1) {
	const characters = [...text];
	return {
		characters,
		character_start_times_seconds: characters.map((_, i) => i * step),
		character_end_times_seconds: characters.map((_, i) => (i + 1) * step)
	};
}

describe('wordsFromAlignment', () => {
	it('groups characters into words with timings and offsets', () => {
		const words = wordsFromAlignment(alignmentFor('Curved  space'));
		expect(words.map((w) => w.text)).toEqual(['Curved', 'space']);
		expect(words[0]).toMatchObject({ charStart: 0, charEnd: 6 });
		expect(words[1].charStart).toBe(8);
		expect(words[1].start).toBeCloseTo(0.8);
		expect(words[1].end).toBeCloseTo(1.3);
	});

	it('applies a time offset for later clips', () => {
		expect(wordsFromAlignment(alignmentFor('hi'), 5)[0].start).toBeCloseTo(5);
	});
});

describe('wordAt', () => {
	it('finds the word being spoken', () => {
		const words = wordsFromAlignment(alignmentFor('one two three'));
		expect(wordAt(words, -1)).toBe(-1);
		expect(wordAt(words, 0.05)).toBe(0);
		expect(wordAt(words, 0.45)).toBe(1);
		expect(wordAt(words, 99)).toBe(2);
	});
});
