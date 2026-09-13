import type { PageServerLoad } from './$types';
import { searchKnowledge } from '#lib/server/vault/index.js';
import { ENTRY_KINDS, type EntryKind } from '#lib/vault/types.js';

export const load: PageServerLoad = ({ url }) => {
	const q = (url.searchParams.get('q') ?? '').slice(0, 200);
	const kindParam = url.searchParams.get('kind');
	const kind = (ENTRY_KINDS as readonly string[]).includes(kindParam ?? '') ? (kindParam as EntryKind) : null;
	const results = q.trim().length >= 2 ? searchKnowledge({ query: q, kinds: kind ? [kind] : null, limit: 20 }) : [];
	return { q, kind, results };
};
