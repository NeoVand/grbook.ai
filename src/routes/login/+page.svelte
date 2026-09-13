<script lang="ts">
	import { enhance } from '$app/forms';
	import { page } from '$app/state';
	import { Button } from '#lib/components/ui/button/index.js';
	import { Input } from '#lib/components/ui/input/index.js';
	import { Label } from '#lib/components/ui/label/index.js';

	let { form } = $props();
	let mode = $state<'signIn' | 'signUp'>('signIn');

	$effect(() => {
		if (form?.mode === 'signUp' || form?.mode === 'signIn') mode = form.mode;
	});

	const query = $derived(page.url.search);
</script>

<svelte:head>
	<title>{mode === 'signIn' ? 'Sign in' : 'Create an account'} · grbook.ai</title>
</svelte:head>

<main class="mx-auto flex min-h-[calc(100dvh-3.5rem)] max-w-sm flex-col justify-center px-6 py-10">
	<h1 class="font-heading text-2xl font-semibold tracking-tight">{mode === 'signIn' ? 'Welcome back' : 'Create your account'}</h1>
	<p class="mt-2 text-sm text-muted-foreground">
		{mode === 'signIn' ? 'Sign in to keep your progress and talk with the tutor.' : 'Your account remembers what you have learned and holds your API keys securely.'}
	</p>

	{#if form?.message}
		<p class="mt-4 rounded-md border border-destructive/40 bg-destructive/10 px-3 py-2 text-sm">{form.message}</p>
	{/if}

	<form method="POST" action="?/{mode}{query}" use:enhance class="mt-6 space-y-4">
		{#if mode === 'signUp'}
			<div class="space-y-1.5">
				<Label for="name">Name</Label>
				<Input id="name" name="name" autocomplete="name" value={form?.name ?? ''} required />
			</div>
		{/if}
		<div class="space-y-1.5">
			<Label for="email">Email</Label>
			<Input id="email" name="email" type="email" autocomplete="email" value={form?.email ?? ''} required />
		</div>
		<div class="space-y-1.5">
			<Label for="password">Password</Label>
			<Input id="password" name="password" type="password" autocomplete={mode === 'signIn' ? 'current-password' : 'new-password'} minlength={8} required />
		</div>
		<Button type="submit" class="w-full">{mode === 'signIn' ? 'Sign in' : 'Create account'}</Button>
	</form>

	<form method="POST" action="?/github{query}" use:enhance class="mt-3">
		<Button type="submit" variant="outline" class="w-full">Continue with GitHub</Button>
	</form>

	<button type="button" class="mt-6 text-sm text-muted-foreground hover:text-foreground" onclick={() => (mode = mode === 'signIn' ? 'signUp' : 'signIn')}>
		{mode === 'signIn' ? 'New here? Create an account' : 'Already have an account? Sign in'}
	</button>
</main>
