import { fail, redirect } from '@sveltejs/kit';
import { APIError } from 'better-auth/api';
import type { Actions, PageServerLoad } from './$types';
import { auth } from '#lib/server/auth.js';

/** Only same-site relative paths are allowed as post-login destinations. */
function destination(url: URL): string {
	const target = url.searchParams.get('redirect') ?? '/learn';
	return target.startsWith('/') && !target.startsWith('//') ? target : '/learn';
}

export const load: PageServerLoad = ({ locals, url }) => {
	if (locals.user) redirect(302, destination(url));
	return { redirectTo: destination(url) };
};

export const actions: Actions = {
	signIn: async ({ request, url }) => {
		const form = await request.formData();
		const email = String(form.get('email') ?? '');
		try {
			await auth.api.signInEmail({ body: { email, password: String(form.get('password') ?? '') } });
		} catch (e) {
			return fail(400, { mode: 'signIn', email, message: e instanceof APIError ? e.message || 'Sign in failed' : 'Unexpected error' });
		}
		redirect(302, destination(url));
	},
	signUp: async ({ request, url }) => {
		const form = await request.formData();
		const email = String(form.get('email') ?? '');
		const name = String(form.get('name') ?? '');
		try {
			await auth.api.signUpEmail({ body: { email, name, password: String(form.get('password') ?? '') } });
		} catch (e) {
			return fail(400, { mode: 'signUp', email, name, message: e instanceof APIError ? e.message || 'Could not create the account' : 'Unexpected error' });
		}
		redirect(302, destination(url));
	},
	github: async ({ url }) => {
		const result = await auth.api.signInSocial({ body: { provider: 'github', callbackURL: destination(url) } });
		if (result.url) redirect(302, result.url);
		return fail(400, { mode: 'signIn', message: 'GitHub sign-in is not available' });
	}
};
