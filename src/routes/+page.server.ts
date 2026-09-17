import { getSection, totals } from '#lib/server/book.js';
import { renderProse } from '#lib/book/prose.js';

/** The home page shows the book's real state and a real paragraph from it, never a mock-up. */
export const load = async () => {
	const opener = getSection('curved-surfaces');
	return {
		totals,
		excerpt: opener
			? {
					href: `/read/${opener.chapter}/${opener.id}`,
					chapter: opener.chapterTitle,
					title: opener.title,
					depth: opener.depth,
					html: renderProse(
						opener.opening
							.split(/\n\s*\n/)
							.slice(0, 2)
							.join('\n\n')
					)
				}
			: null
	};
};
