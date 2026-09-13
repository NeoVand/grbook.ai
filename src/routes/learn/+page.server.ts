import type { PageServerLoad } from './$types';
import { books } from '#lib/server/vault/index.js';

export const load: PageServerLoad = () => ({
	books: books.map((book) => ({
		id: book.id,
		short: book.short,
		title: book.title,
		authors: book.authors,
		edition: book.edition,
		units: book.units.map((u) => ({
			id: u.id,
			label: u.label,
			kind: u.kind,
			title: u.title,
			part: u.part,
			hasDossier: u.hasDossier,
			verified: u.verified,
			summary: u.summary ?? null,
			difficulty: u.difficulty ?? null
		}))
	}))
});
