<script lang="ts">
	import { Badge } from '#lib/components/ui/badge/index.js';

	let { data } = $props();

	function groupByPart<T extends { part: string | null }>(units: T[]) {
		const groups: { part: string | null; units: T[] }[] = [];
		for (const unit of units) {
			const last = groups.at(-1);
			if (last && last.part === unit.part) last.units.push(unit);
			else groups.push({ part: unit.part, units: [unit] });
		}
		return groups;
	}

	const totals = $derived({
		units: data.books.reduce((n, b) => n + b.units.length, 0),
		ready: data.books.reduce((n, b) => n + b.units.filter((u) => u.hasDossier).length, 0)
	});
</script>

<svelte:head>
	<title>Learn · grbook.ai</title>
</svelte:head>

<main class="px-6 py-10">
	<header class="max-w-3xl">
		<h1 class="font-heading text-3xl font-semibold tracking-tight">Learn</h1>
		<p class="mt-3 text-muted-foreground">
			For now the course is organised by the three textbooks it learns from. Soon it will be organised by ideas, with
			learning paths that start wherever you are. Notes are ready for {totals.ready} of {totals.units} chapters.
		</p>
	</header>

	<div class="mt-10 grid gap-8 2xl:grid-cols-3">
		{#each data.books as book (book.id)}
			<section class="rounded-xl border">
				<div class="border-b p-5">
					<p class="text-xs font-medium tracking-wider text-muted-foreground uppercase">{book.short}</p>
					<h2 class="mt-1 font-heading text-lg font-semibold">{book.title}</h2>
					<p class="text-sm text-muted-foreground">{book.authors.join(', ')} · {book.edition}</p>
				</div>
				<div class="divide-y">
					{#each groupByPart(book.units) as group, gi (gi)}
						<div class="p-3">
							{#if group.part}
								<p class="px-2 pt-1 pb-2 text-xs font-medium text-muted-foreground">{group.part}</p>
							{/if}
							<ul>
								{#each group.units as unit (unit.id)}
									<li>
										<a
											href="/learn/{book.id}/{unit.id}"
											class="flex items-start gap-3 rounded-lg px-2 py-2 transition-colors hover:bg-muted {unit.hasDossier
												? ''
												: 'opacity-60'}"
										>
											<span class="w-8 shrink-0 pt-0.5 text-right font-mono text-xs text-muted-foreground">
												{unit.kind === 'appendix' ? unit.label : Number(unit.label)}
											</span>
											<span class="min-w-0 flex-1">
												<span class="block text-sm font-medium">{unit.title}</span>
												{#if unit.summary}
													<span class="line-clamp-2 block text-xs text-muted-foreground">{unit.summary}</span>
												{/if}
											</span>
											{#if !unit.hasDossier}
												<Badge variant="outline" class="shrink-0">in progress</Badge>
											{/if}
										</a>
									</li>
								{/each}
							</ul>
						</div>
					{/each}
				</div>
			</section>
		{/each}
	</div>
</main>
