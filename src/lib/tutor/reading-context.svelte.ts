import { goto } from '$app/navigation';
import { tick, untrack } from 'svelte';

export interface ReadingContext {
	book: string | null;
	bookTitle: string | null;
	unit: string | null;
	unitTitle: string | null;
	section: string | null;
	selection: string | null;
	lab: { id: string; state: Record<string, unknown> } | null;
}

const EMPTY: ReadingContext = { book: null, bookTitle: null, unit: null, unitTitle: null, section: null, selection: null, lab: null };

/** What the learner is looking at, shared by the reader, labs, and the tutor. Semantic state only, never pixels. */
class ReadingState {
	current = $state<ReadingContext>({ ...EMPTY });

	set(patch: Partial<ReadingContext>) {
		// Read without tracking so callers inside effects do not subscribe to the state they write.
		this.current = { ...untrack(() => this.current), ...patch };
	}

	clear() {
		this.current = { ...EMPTY };
	}

	/** One short sentence for the tutor's quiet context. */
	describe(): string | null {
		const c = this.current;
		if (!c.unit) return c.lab ? `Demo ${c.lab.id} with parameters ${JSON.stringify(c.lab.state)}` : null;
		const parts = [`${c.bookTitle ?? c.book}, ${c.unitTitle ?? c.unit} (${c.book}/${c.unit})`];
		if (c.section) parts.push(`section ${c.section}`);
		if (c.selection) parts.push(`selected text: "${c.selection.slice(0, 200)}"`);
		if (c.lab) parts.push(`demo ${c.lab.id} ${JSON.stringify(c.lab.state)}`);
		return parts.join('; ');
	}

	/** Opens a unit, scrolls to a section, and highlights a phrase. Returns false when the place is not available. */
	async show(target: { book: string; unit_id: string; section: string | null; highlight: string | null }): Promise<boolean> {
		const path = `/learn/${encodeURIComponent(target.book)}/${encodeURIComponent(target.unit_id)}`;
		if (location.pathname !== path) {
			await goto(path);
			await tick();
		}
		const reader = document.querySelector('[data-reader]');
		if (!reader) return false;
		const anchor = target.section ? document.getElementById(`section-${target.section}`) : reader;
		anchor?.scrollIntoView({ behavior: 'smooth', block: 'start' });
		if (target.highlight) highlightPhrase(reader, target.highlight);
		return Boolean(anchor);
	}
}

export const reading = new ReadingState();

/** Highlights the first occurrence of a phrase with the CSS Custom Highlight API, without changing the DOM. */
export function highlightPhrase(root: Element | null, phrase: string): boolean {
	const needle = phrase.trim().toLowerCase();
	if (!root || !needle || typeof CSS === 'undefined' || !('highlights' in CSS)) return false;
	const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
	for (let node = walker.nextNode(); node; node = walker.nextNode()) {
		const index = (node.textContent ?? '').toLowerCase().indexOf(needle);
		if (index >= 0) {
			const range = new Range();
			range.setStart(node, index);
			range.setEnd(node, index + needle.length);
			CSS.highlights.set('tutor', new Highlight(range));
			node.parentElement?.scrollIntoView({ behavior: 'smooth', block: 'center' });
			return true;
		}
	}
	return false;
}
