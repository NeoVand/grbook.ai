import katex from 'katex';

const cache = new Map<string, string>();

/**
 * Renders TeX to HTML with KaTeX. Rendering never throws: malformed input is shown as an error span so a single
 * bad transcription cannot break a page. `trust` stays false, so TeX cannot inject links or scripts.
 */
export function renderMath(tex: string, displayMode = false): string {
	const key = `${displayMode ? 'D' : 'I'}:${tex}`;
	const hit = cache.get(key);
	if (hit !== undefined) return hit;
	const html = katex.renderToString(tex, {
		displayMode,
		throwOnError: false,
		strict: 'ignore',
		trust: false,
		output: 'htmlAndMathml'
	});
	if (cache.size > 2000) cache.clear();
	cache.set(key, html);
	return html;
}
