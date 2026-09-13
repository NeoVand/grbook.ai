<script lang="ts">
	import { HugeiconsIcon } from '@hugeicons/svelte';
	import { PauseIcon, PlayIcon, StopIcon } from '@hugeicons/core-free-icons';
	import { narrator } from '#lib/audio/narrator.svelte.js';

	let {
		id,
		text,
		enabled,
		class: className = ''
	}: { id: string; text: string; enabled: boolean; class?: string } = $props();

	const words = $derived(text.split(/\s+/).filter(Boolean));
	const mine = $derived(narrator.passageId === id);
</script>

<div class="group flex items-start gap-2 {className}">
	{#if enabled}
		<button
			type="button"
			class="mt-1 grid size-7 shrink-0 place-items-center rounded-full border text-muted-foreground transition-colors hover:bg-muted hover:text-foreground"
			aria-label={mine && narrator.status === 'playing' ? 'Pause narration' : 'Listen'}
			onclick={() => {
				if (mine && narrator.status === 'playing') narrator.pause();
				else if (mine && narrator.status === 'paused') narrator.resume();
				else narrator.play(id, text);
			}}
		>
			{#if mine && narrator.status === 'playing'}
				<HugeiconsIcon icon={PauseIcon} size={14} />
			{:else if mine && narrator.status === 'loading'}
				<span class="size-2 animate-pulse rounded-full bg-current"></span>
			{:else}
				<HugeiconsIcon icon={PlayIcon} size={14} />
			{/if}
		</button>
	{/if}
	<p class="min-w-0 flex-1">
		{#if mine && narrator.words.length}
			{#each words as word, i (i)}<span class={i === narrator.wordIndex ? 'narration-word-active' : ''}>{word}</span>{' '}{/each}
		{:else}
			{text}
		{/if}
	</p>
	{#if mine && (narrator.status === 'playing' || narrator.status === 'paused')}
		<button type="button" class="mt-1 text-muted-foreground hover:text-foreground" aria-label="Stop narration" onclick={() => narrator.stop()}>
			<HugeiconsIcon icon={StopIcon} size={14} />
		</button>
	{/if}
</div>
{#if mine && narrator.error}
	<p class="mt-1 text-xs text-destructive">{narrator.error}</p>
{/if}
