import type { LayoutServerLoad } from './$types';
import { listProviderKeys } from '#lib/server/credentials.js';

export const load: LayoutServerLoad = async ({ locals }) => {
	if (!locals.user) return { keys: { openai: false, elevenlabs: false } };
	const keys = await listProviderKeys(locals.user.id);
	return {
		keys: {
			openai: keys.some((k) => k.provider === 'openai'),
			elevenlabs: keys.some((k) => k.provider === 'elevenlabs')
		}
	};
};
