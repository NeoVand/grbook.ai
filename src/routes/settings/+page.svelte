<script lang="ts">
	import { enhance } from '$app/forms';
	import { Button } from '#lib/components/ui/button/index.js';
	import { Input } from '#lib/components/ui/input/index.js';
	import { Label } from '#lib/components/ui/label/index.js';
	import { Badge } from '#lib/components/ui/badge/index.js';

	let { data, form } = $props();

	const providers = [
		{
			id: 'openai',
			name: 'OpenAI',
			use: 'Powers the voice tutor (GPT-Live, billed per minute of conversation plus backend tokens).',
			placeholder: 'sk-…',
			link: 'https://platform.openai.com/api-keys'
		},
		{
			id: 'elevenlabs',
			name: 'ElevenLabs',
			use: 'Reads chapters and explanations aloud with word-by-word highlighting.',
			placeholder: 'Your ElevenLabs API key',
			link: 'https://elevenlabs.io/app/settings/api-keys'
		}
	] as const;

	const keyFor = (id: string) => data.keys.find((k) => k.provider === id);
</script>

<svelte:head>
	<title>Settings · grbook.ai</title>
</svelte:head>

<main class="mx-auto max-w-3xl px-6 py-10">
	<div class="flex items-center justify-between gap-4">
		<h1 class="font-heading text-3xl font-semibold tracking-tight">Settings</h1>
		<form method="POST" action="?/signOut" use:enhance>
			<Button variant="ghost" type="submit">Sign out</Button>
		</form>
	</div>

	{#if form?.message}
		<p class="mt-6 rounded-md border px-3 py-2 text-sm">{form.message}</p>
	{/if}

	<section class="mt-8">
		<h2 class="font-heading text-lg font-semibold">Your API keys</h2>
		<p class="mt-1 text-sm text-muted-foreground">
			Keys are encrypted before they are stored and are never sent back to your browser; only the last four characters
			are shown. Usage is billed to your own accounts.
		</p>
		<div class="mt-4 space-y-4">
			{#each providers as p (p.id)}
				{@const saved = keyFor(p.id)}
				<div class="rounded-xl border p-5">
					<div class="flex flex-wrap items-center gap-2">
						<h3 class="font-medium">{p.name}</h3>
						{#if saved}
							<Badge variant="secondary">•••• {saved.last4}</Badge>
						{:else}
							<Badge variant="outline">Not connected</Badge>
						{/if}
						<a href={p.link} target="_blank" rel="noreferrer" class="ml-auto text-xs text-muted-foreground hover:underline">Get a key</a>
					</div>
					<p class="mt-1 text-sm text-muted-foreground">{p.use}</p>
					<form method="POST" action="?/saveKey" use:enhance class="mt-4 flex flex-col gap-2 sm:flex-row">
						<input type="hidden" name="provider" value={p.id} />
						<Label for="key-{p.id}" class="sr-only">{p.name} API key</Label>
						<Input id="key-{p.id}" name="key" type="password" autocomplete="off" placeholder={saved ? 'Replace key' : p.placeholder} required class="flex-1" />
						<Button type="submit">{saved ? 'Replace' : 'Save'}</Button>
					</form>
					{#if saved}
						<form method="POST" action="?/removeKey" use:enhance class="mt-2">
							<input type="hidden" name="provider" value={p.id} />
							<Button type="submit" variant="link" class="h-auto px-0 text-xs text-muted-foreground">Remove key</Button>
						</form>
					{/if}
				</div>
			{/each}
		</div>
	</section>

	<section class="mt-12">
		<h2 class="font-heading text-lg font-semibold">Voices</h2>
		<form method="POST" action="?/savePreferences" use:enhance class="mt-4 grid gap-5 rounded-xl border p-5 sm:grid-cols-2">
			<div class="space-y-1.5">
				<Label for="tutorVoice">Tutor voice</Label>
				<select id="tutorVoice" name="tutorVoice" class="h-9 w-full rounded-md border bg-background px-3 text-sm">
					{#each data.voices as voice (voice)}
						<option value={voice} selected={voice === data.preferences.tutorVoice}>{voice}</option>
					{/each}
				</select>
			</div>
			<div class="space-y-1.5">
				<Label for="narrationModel">Narration model</Label>
				<select id="narrationModel" name="narrationModel" class="h-9 w-full rounded-md border bg-background px-3 text-sm">
					{#each data.narrationModels as model (model)}
						<option value={model} selected={model === data.preferences.narrationModel}>{model}</option>
					{/each}
				</select>
			</div>
			<div class="space-y-1.5">
				<Label for="narrationVoiceId">ElevenLabs voice ID</Label>
				<Input id="narrationVoiceId" name="narrationVoiceId" value={data.preferences.narrationVoiceId} placeholder="Default voice" />
			</div>
			<div class="space-y-1.5">
				<Label for="narrationSpeed">Narration speed</Label>
				<Input id="narrationSpeed" name="narrationSpeed" type="number" min="0.7" max="1.2" step="0.05" value={data.preferences.narrationSpeed} />
			</div>
			<div class="sm:col-span-2">
				<Button type="submit">Save voices</Button>
			</div>
		</form>
	</section>
</main>
