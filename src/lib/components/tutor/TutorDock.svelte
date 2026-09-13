<script lang="ts">
	import { page } from '$app/state';
	import { HugeiconsIcon } from '@hugeicons/svelte';
	import { CallEnd01Icon, Mic01Icon, MicOff01Icon, SparklesIcon } from '@hugeicons/core-free-icons';
	import { Button } from '#lib/components/ui/button/index.js';
	import { tutor } from '#lib/tutor/live-client.svelte.js';
	import { reading } from '#lib/tutor/reading-context.svelte.js';

	let { signedIn, keys }: { signedIn: boolean; keys: { openai: boolean; elevenlabs: boolean } } = $props();

	let scroller = $state<HTMLDivElement>();

	const suggestions = [
		'Explain the key idea of this chapter in plain words.',
		'Why does someone in free fall feel no gravity?',
		'Quiz me on what I just read.'
	];

	const statusLabel = $derived(
		{ idle: 'Ready', connecting: 'Connecting…', live: tutor.muted ? 'Muted' : 'Listening', closing: 'Ending…', error: 'Stopped' }[tutor.status]
	);

	$effect(() => {
		// Re-send quiet context whenever what the learner is reading changes.
		void reading.current;
		tutor.contextChanged();
	});

	$effect(() => {
		void tutor.captions.length;
		void tutor.captions.at(-1)?.text;
		scroller?.scrollTo({ top: scroller.scrollHeight, behavior: 'smooth' });
	});
</script>

<div class="flex h-full flex-col">
	<div class="border-b px-4 py-3">
		<div class="flex items-center gap-2">
			<HugeiconsIcon icon={SparklesIcon} size={16} />
			<h2 class="font-heading text-sm font-semibold">Tutor</h2>
			<span class="ml-auto flex items-center gap-1.5 text-xs text-muted-foreground">
				<span
					class="size-1.5 rounded-full {tutor.status === 'live'
						? 'bg-emerald-500'
						: tutor.status === 'error'
							? 'bg-destructive'
							: tutor.status === 'idle'
								? 'bg-muted-foreground/40'
								: 'animate-pulse bg-amber-500'}"
				></span>
				{statusLabel}
			</span>
		</div>
		<p class="mt-1 text-xs text-muted-foreground">Talk it through. The tutor can see which page you are on.</p>
	</div>

	<div bind:this={scroller} class="min-h-0 flex-1 space-y-3 overflow-y-auto px-4 py-4" aria-live="polite">
		{#if tutor.captions.length === 0}
			<div class="space-y-2 text-sm text-muted-foreground">
				<p>Things you could say:</p>
				<ul class="space-y-1.5">
					{#each suggestions as suggestion (suggestion)}
						<li class="rounded-lg border border-dashed px-3 py-2">“{suggestion}”</li>
					{/each}
				</ul>
			</div>
		{:else}
			{#each tutor.captions as caption, i (i)}
				<div class={caption.role === 'learner' ? 'ml-8 text-right' : 'mr-4'}>
					<div
						class="inline-block rounded-2xl px-3 py-2 text-sm leading-relaxed {caption.role === 'learner'
							? 'bg-primary text-primary-foreground'
							: 'bg-muted'}"
					>
						{caption.text}
					</div>
				</div>
			{/each}
		{/if}
	</div>

	{#if tutor.activity}
		<p class="px-4 pb-2 text-xs text-muted-foreground"><span class="animate-pulse">●</span> {tutor.activity}</p>
	{/if}
	{#if tutor.error}
		<p class="mx-4 mb-2 rounded-md border border-destructive/40 bg-destructive/10 px-3 py-2 text-xs">{tutor.error}</p>
	{/if}

	<div class="flex items-center gap-2 border-t p-3">
		{#if !signedIn}
			<Button class="w-full" href="/login?redirect={encodeURIComponent(page.url.pathname)}">Sign in to talk with the tutor</Button>
		{:else if !keys.openai}
			<Button class="w-full" variant="secondary" href="/settings">Add your OpenAI key to talk</Button>
		{:else if tutor.status === 'idle' || tutor.status === 'error'}
			<Button class="w-full" onclick={() => tutor.start()}>
				<HugeiconsIcon icon={Mic01Icon} size={16} />
				Start talking
			</Button>
		{:else}
			<Button variant="outline" class="flex-1" disabled={tutor.status !== 'live'} onclick={() => tutor.toggleMute()}>
				<HugeiconsIcon icon={tutor.muted ? MicOff01Icon : Mic01Icon} size={16} />
				{tutor.muted ? 'Unmute' : 'Mute'}
			</Button>
			<Button variant="destructive" class="flex-1" disabled={tutor.status === 'closing'} onclick={() => tutor.stop()}>
				<HugeiconsIcon icon={CallEnd01Icon} size={16} />
				End
			</Button>
		{/if}
	</div>
</div>
