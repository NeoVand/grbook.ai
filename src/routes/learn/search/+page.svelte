<script lang="ts">
	import { Badge } from '#lib/components/ui/badge/index.js';
	import { Input } from '#lib/components/ui/input/index.js';
	import { Button } from '#lib/components/ui/button/index.js';
	import { formatLocator } from '#lib/vault/types.js';

	let { data } = $props();

	const kinds = [
		{ value: '', label: 'Everything' },
		{ value: 'concept', label: 'Concepts' },
		{ value: 'equation', label: 'Equations' },
		{ value: 'example', label: 'Examples' },
		{ value: 'misconception', label: 'Misconceptions' },
		{ value: 'analogy', label: 'Analogies' },
		{ value: 'figure', label: 'Demo ideas' },
		{ value: 'unit', label: 'Chapters' }
	];
</script>

<svelte:head>
	<title>Search · grbook.ai</title>
</svelte:head>

<main class="max-w-4xl px-6 py-10">
	<h1 class="font-heading text-3xl font-semibold tracking-tight">Search the course</h1>
	<form method="GET" class="mt-6 flex flex-col gap-3 sm:flex-row">
		<Input name="q" value={data.q} placeholder="Try “parallel transport”, “tidal forces”, or “why can't I feel gravity in free fall”" class="flex-1" autofocus />
		<select name="kind" class="h-9 rounded-md border bg-background px-3 text-sm">
			{#each kinds as kind (kind.value)}
				<option value={kind.value} selected={(data.kind ?? '') === kind.value}>{kind.label}</option>
			{/each}
		</select>
		<Button type="submit">Search</Button>
	</form>

	{#if data.q && data.results.length === 0}
		<p class="mt-8 text-muted-foreground">Nothing found for “{data.q}”.</p>
	{/if}

	<ul class="mt-8 space-y-3">
		{#each data.results as result (result.id)}
			<li class="rounded-xl border p-4">
				<div class="flex flex-wrap items-center gap-2">
					<Badge variant="secondary">{result.kind === 'figure' ? 'demo idea' : result.kind}</Badge>
					{#if result.book && result.unit}
						<a href="/learn/{result.book}/{result.unit}" class="text-xs text-muted-foreground hover:text-foreground hover:underline">
							{formatLocator(result.book, result.locator)} · {result.unit}
						</a>
					{/if}
				</div>
				<p class="mt-2 font-medium">{result.title}</p>
				<p class="mt-1 text-sm leading-relaxed text-muted-foreground">{result.text}</p>
			</li>
		{/each}
	</ul>
</main>
