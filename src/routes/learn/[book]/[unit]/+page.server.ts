import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { db } from '#lib/server/db/index.js';
import { learningEvent } from '#lib/server/db/schema.js';
import { getBook, getDossier, getUnit } from '#lib/server/vault/index.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	const book = getBook(params.book);
	const unit = book ? getUnit(params.book, params.unit) : null;
	if (!book || !unit) error(404, 'That chapter is not in the course');

	const dossier = await getDossier(book.id, unit.id);
	const index = book.units.findIndex((u) => u.id === unit.id);
	const neighbour = (i: number) => (book.units[i] ? { id: book.units[i].id, title: book.units[i].title } : null);

	if (locals.user) {
		const day = new Date().toISOString().slice(0, 10);
		await db
			.insert(learningEvent)
			.values({
				userId: locals.user.id,
				kind: 'visited',
				subjectType: 'unit',
				subjectId: `${book.id}/${unit.id}`,
				idempotencyKey: `visit:${locals.user.id}:${book.id}/${unit.id}:${day}`
			})
			.onConflictDoNothing();
	}

	return {
		book: { id: book.id, short: book.short, title: book.title, authors: book.authors },
		unit,
		dossier,
		prev: neighbour(index - 1),
		next: neighbour(index + 1)
	};
};
