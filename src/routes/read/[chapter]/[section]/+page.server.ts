import { error } from '@sveltejs/kit';
import { getChapter, getSection, neighbours } from '#lib/server/book.js';
import { renderLine, renderProse } from '#lib/book/prose.js';
import { renderMath } from '#lib/math/render.js';

export const load = async ({ params }) => {
	const section = getSection(params.section);
	if (!section || section.chapter !== params.chapter)
		error(404, 'That section is not written yet.');
	const chapter = getChapter(section.chapter);

	// Math and markdown render on the server: KaTeX ships no client bundle, and the page is readable without JS.
	const html = {
		opening: renderProse(section.opening),
		parts: section.parts.map((p) => ({
			...p,
			text: renderProse(p.text),
			takeaway: renderLine(p.takeaway)
		})),
		equations: section.key_equations.map((e) => ({
			...e,
			meaning: renderLine(e.meaning),
			latexHtml: renderMath(e.latex, true)
		})),
		examples: section.worked_examples.map((x) => ({
			...x,
			problem: renderLine(x.problem),
			steps: x.steps.map(renderLine),
			answer: renderLine(x.answer)
		})),
		checks: section.checks.map((c) => ({
			...c,
			question: renderLine(c.question),
			answer: renderProse(c.answer),
			key_points: c.key_points.map(renderLine)
		})),
		glossary: section.glossary.map((g) => ({
			...g,
			plain_definition: renderLine(g.plain_definition)
		})),
		misconceptions: section.misconceptions.map((m) => ({
			...m,
			correction: renderLine(m.correction)
		})),
		further: section.further.map((f) => ({ ...f, note: renderLine(f.note) }))
	};

	return { section, chapter, html, ...neighbours(params.section) };
};
