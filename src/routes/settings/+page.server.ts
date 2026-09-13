import { fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';
import { auth } from '#lib/server/auth.js';
import { deleteProviderKey, listProviderKeys, saveProviderKey } from '#lib/server/credentials.js';
import { PROVIDERS, type Provider } from '#lib/server/db/schema.js';
import { getPreferences, savePreferences } from '#lib/server/preferences.js';

const TUTOR_VOICES = ['marin', 'cedar', 'alloy', 'ash', 'ballad', 'beacon', 'bossa', 'cinder', 'coral', 'delta', 'echo', 'gleam', 'meridian'];
const NARRATION_MODELS = ['eleven_multilingual_v2', 'eleven_flash_v2_5', 'eleven_v3'];

export const load: PageServerLoad = async ({ locals }) => {
	if (!locals.user) redirect(302, '/login?redirect=/settings');
	const [keys, preferences] = await Promise.all([listProviderKeys(locals.user.id), getPreferences(locals.user.id)]);
	return {
		keys: keys.map((k) => ({ provider: k.provider, last4: k.last4, updatedAt: k.updatedAt.toISOString() })),
		preferences: {
			tutorVoice: preferences.tutorVoice,
			narrationVoiceId: preferences.narrationVoiceId ?? '',
			narrationModel: preferences.narrationModel,
			narrationSpeed: preferences.narrationSpeed
		},
		voices: TUTOR_VOICES,
		narrationModels: NARRATION_MODELS
	};
};

function provider(value: FormDataEntryValue | null): Provider | null {
	return (PROVIDERS as readonly string[]).includes(String(value)) ? (value as Provider) : null;
}

export const actions: Actions = {
	saveKey: async ({ request, locals }) => {
		if (!locals.user) return fail(401, { message: 'Sign in first' });
		const form = await request.formData();
		const which = provider(form.get('provider'));
		const key = String(form.get('key') ?? '');
		if (!which) return fail(400, { message: 'Unknown provider' });
		try {
			await saveProviderKey(locals.user.id, which, key);
		} catch (e) {
			return fail(400, { provider: which, message: e instanceof Error ? e.message : 'Could not save the key' });
		}
		return { provider: which, message: 'Key saved' };
	},
	removeKey: async ({ request, locals }) => {
		if (!locals.user) return fail(401, { message: 'Sign in first' });
		const which = provider((await request.formData()).get('provider'));
		if (!which) return fail(400, { message: 'Unknown provider' });
		await deleteProviderKey(locals.user.id, which);
		return { provider: which, message: 'Key removed' };
	},
	savePreferences: async ({ request, locals }) => {
		if (!locals.user) return fail(401, { message: 'Sign in first' });
		const form = await request.formData();
		const voice = String(form.get('tutorVoice') ?? 'marin');
		const model = String(form.get('narrationModel') ?? NARRATION_MODELS[0]);
		const speed = Number(form.get('narrationSpeed') ?? 1);
		const voiceId = String(form.get('narrationVoiceId') ?? '').trim();
		if (!TUTOR_VOICES.includes(voice) || !NARRATION_MODELS.includes(model) || !(speed >= 0.7 && speed <= 1.2) || !/^[A-Za-z0-9]{0,40}$/.test(voiceId)) {
			return fail(400, { message: 'Some preferences are not valid' });
		}
		await savePreferences(locals.user.id, { tutorVoice: voice, narrationModel: model, narrationSpeed: speed, narrationVoiceId: voiceId || null });
		return { message: 'Preferences saved' };
	},
	signOut: async ({ request }) => {
		await auth.api.signOut({ headers: request.headers });
		redirect(302, '/');
	}
};
