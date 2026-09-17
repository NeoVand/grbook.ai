import { renderMath } from '#lib/math/render.js';

const escapeHtml = (s: string) =>
	s.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c] as string);

/**
 * Renders the vault's `md` format: paragraphs, `- ` bullets, `*emphasis*`, `$inline$` and `$$display$$` math.
 * Everything that is not math or emphasis is escaped, so section text can never inject markup.
 */
function inline(text: string): string {
	const out: string[] = [];
	const pattern = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$|\*([^*\n]+?)\*/g;
	let last = 0;
	let m: RegExpExecArray | null;
	while ((m = pattern.exec(text))) {
		out.push(escapeHtml(text.slice(last, m.index)));
		if (m[1] !== undefined) out.push(`<span class="math-display">${renderMath(m[1], true)}</span>`);
		else if (m[2] !== undefined) out.push(renderMath(m[2], false));
		else out.push(`<em>${escapeHtml(m[3])}</em>`);
		last = pattern.lastIndex;
	}
	out.push(escapeHtml(text.slice(last)));
	return out.join('');
}

export function renderProse(text: string | null | undefined): string {
	if (!text) return '';
	return text
		.split(/\n\s*\n/)
		.map((block) => {
			const lines = block.split('\n');
			if (lines.every((l) => l.trim().startsWith('- ')))
				return `<ul>${lines.map((l) => `<li>${inline(l.trim().slice(2))}</li>`).join('')}</ul>`;
			return `<p>${inline(block.replace(/\n/g, ' '))}</p>`;
		})
		.join('');
}

/** One line of prose (a takeaway, a definition, a check question): math and emphasis, no paragraphs. */
export function renderLine(text: string | null | undefined): string {
	return text ? inline(text) : '';
}
