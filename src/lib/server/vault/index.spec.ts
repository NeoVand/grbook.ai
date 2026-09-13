import { describe, expect, it } from 'vitest';
import { books, getDossier, getUnit, searchKnowledge } from './index';

describe('vault runtime index', () => {
	it('lists the three source books with their units', () => {
		expect(books.map((b) => b.id).sort()).toEqual(['dinverno', 'gifted-amateur', 'schutz']);
		expect(getUnit('gifted-amateur', 'ch11')?.title).toMatch(/Riemann/);
	});

	it('finds concepts by name', () => {
		const results = searchKnowledge({ query: 'Riemann curvature tensor', kinds: ['concept'], limit: 5 });
		expect(results.length).toBeGreaterThan(0);
		expect(results[0].title.toLowerCase()).toContain('riemann');
	});

	it('filters by book', () => {
		const results = searchKnowledge({ query: 'equivalence principle', book: 'dinverno', limit: 8 });
		expect(results.every((r) => r.book === 'dinverno')).toBe(true);
	});

	it('loads dossiers and rejects malformed ids', async () => {
		expect((await getDossier('gifted-amateur', 'ch11'))?.unit_id).toBe('ch11');
		expect(await getDossier('gifted-amateur', '../secrets')).toBeNull();
		expect(await getDossier('unknown', 'ch01')).toBeNull();
	});
});
