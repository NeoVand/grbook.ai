import MiniSearch from 'minisearch';
import raw from './generated/index.json';
import { BOOK_IDS, type BookSummary, type Dossier, type EntryKind, type UnitSummary, type VaultEntry } from '#lib/vault/types.js';

/** Runtime view of the knowledge vault, compiled by scripts/build-vault-index.ts. Server only. */
const data = raw as unknown as { books: BookSummary[]; entries: VaultEntry[] };
const entriesById = new Map(data.entries.map((e) => [e.id, e]));
const dossierLoaders = import.meta.glob<Dossier>('/knowledge/sources/*/chapters/*.json', { import: 'default' });

export const UNIT_ID = /^(ch\d{2}|app[A-E])$/;

export const books: BookSummary[] = data.books;

export function getBook(bookId: string): BookSummary | null {
	return books.find((b) => b.id === bookId) ?? null;
}

export function getUnit(bookId: string, unitId: string): UnitSummary | null {
	return getBook(bookId)?.units.find((u) => u.id === unitId) ?? null;
}

export async function getDossier(bookId: string, unitId: string): Promise<Dossier | null> {
	if (!(BOOK_IDS as readonly string[]).includes(bookId) || !UNIT_ID.test(unitId)) return null;
	const load = dossierLoaders[`/knowledge/sources/${bookId}/chapters/${unitId}.json`];
	return load ? load() : null;
}

export function getEntry(id: string): VaultEntry | null {
	return entriesById.get(id) ?? null;
}

let index: MiniSearch<VaultEntry> | null = null;

function searchIndex(): MiniSearch<VaultEntry> {
	if (index) return index;
	index = new MiniSearch<VaultEntry>({
		fields: ['title', 'text', 'aliases'],
		storeFields: ['id'],
		extractField: (doc, field) => {
			if (field === 'aliases') return ((doc.extra?.aliases as string[] | undefined) ?? []).join(' ');
			return (doc as unknown as Record<string, string>)[field];
		},
		searchOptions: { boost: { title: 3, aliases: 2 }, prefix: true, fuzzy: 0.15 }
	});
	index.addAll(data.entries);
	return index;
}

export interface SearchOptions {
	query: string;
	book?: string | null;
	unit?: string | null;
	kinds?: EntryKind[] | null;
	limit?: number | null;
}

export function searchKnowledge({ query, book, unit, kinds, limit }: SearchOptions): VaultEntry[] {
	const q = query.trim();
	if (!q) return [];
	const max = Math.min(Math.max(limit ?? 5, 1), 20);
	const results = searchIndex().search(q, {
		filter: (r) => {
			const e = entriesById.get(r.id);
			return Boolean(e) && (!book || e!.book === book) && (!unit || e!.unit === unit) && (!kinds?.length || kinds.includes(e!.kind));
		}
	});
	return results.slice(0, max).map((r) => entriesById.get(r.id)!);
}
