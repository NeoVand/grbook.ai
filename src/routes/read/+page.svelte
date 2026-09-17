<script lang="ts">
	import { DEPTH_BLURB, DEPTH_LABEL, type Depth } from '#lib/book/types.js';

	let { data } = $props();

	const depths: Depth[] = ['entry', 'working', 'formal', 'research'];
	const chapterNumber = (partIndex: number, chapterIndex: number) =>
		data.parts.slice(0, partIndex).reduce((n, p) => n + p.chapters.length, 0) + chapterIndex + 1;
</script>

<svelte:head>
	<title>The book · grbook.ai</title>
	<meta
		name="description"
		content="General relativity from scratch to research, one section at a time."
	/>
</svelte:head>

<main class="mx-auto max-w-5xl px-5 py-10 sm:px-8 sm:py-14">
	<header class="max-w-2xl">
		<p class="eyebrow">In progress</p>
		<h1
			class="mt-2 font-heading text-4xl leading-[1.1] font-semibold tracking-tight text-balance sm:text-5xl"
		>
			General relativity, written once and read at four depths
		</h1>
		<p class="mt-4 text-lg leading-relaxed text-muted-foreground">
			Every section teaches a cluster of ideas at the depth the book has reached, so the book itself
			is the ladder: the early chapters need no calculus, the late ones sit at research level.
		</p>
	</header>

	<dl class="mt-10 grid grid-cols-2 gap-x-6 gap-y-5 border-y border-border py-5 sm:grid-cols-4">
		{#each [{ k: 'Sections written', v: `${data.totals.written} of ${data.totals.sections}` }, { k: 'Words of prose', v: data.totals.words.toLocaleString() }, { k: 'Gradable checks', v: data.totals.checks }, { k: 'Figures specified', v: `${data.totals.visualsReviewed} of ${data.totals.visuals}` }] as stat (stat.k)}
			<div>
				<dt class="eyebrow">{stat.k}</dt>
				<dd class="mt-1 font-mono text-xl tabular-nums">{stat.v}</dd>
			</div>
		{/each}
	</dl>

	<section class="mt-8">
		<h2 class="eyebrow">How deep each section goes</h2>
		<div class="mt-3 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
			{#each depths as depth (depth)}
				<div class="border-l-2 border-border pl-3">
					<p class="font-heading text-[15px] font-semibold">{DEPTH_LABEL[depth]}</p>
					<p class="mt-0.5 text-sm leading-snug text-muted-foreground">{DEPTH_BLURB[depth]}</p>
				</div>
			{/each}
		</div>
	</section>

	<div class="mt-14 space-y-14">
		{#each data.parts as part, partIndex (part.id)}
			<section>
				<h2
					class="border-b border-foreground pb-2 font-heading text-2xl font-semibold tracking-tight"
				>
					{part.title}
				</h2>
				<div class="mt-6 space-y-8">
					{#each part.chapters as chapter, chapterIndex (chapter.id)}
						{@const number = chapterNumber(partIndex, chapterIndex)}
						<article class="grid gap-x-8 gap-y-3 sm:grid-cols-[7rem_1fr]">
							<div>
								<p class="font-mono text-sm text-muted-foreground tabular-nums">Chapter {number}</p>
								{#if chapter.written > 0}
									<p class="mt-1 text-sm text-primary">
										{chapter.written} of {chapter.sections.length} written
									</p>
								{:else}
									<p class="mt-1 text-sm text-muted-foreground">
										{chapter.sections.length} sections planned
									</p>
								{/if}
							</div>
							<div>
								<h3 class="font-heading text-xl font-semibold tracking-tight">{chapter.title}</h3>
								<ul class="mt-3 space-y-1">
									{#each chapter.sections as section (section.id)}
										<li>
											{#if section.written}
												<a
													href="/read/{chapter.id}/{section.id}"
													class="group -mx-2 flex items-baseline gap-3 rounded px-2 py-1.5 transition-colors hover:bg-accent"
												>
													<span class="flex-1 group-hover:text-primary">{section.title}</span>
													<span class="eyebrow shrink-0">{section.depth}</span>
													{#if section.track !== 'main'}<span class="eyebrow shrink-0"
															>{section.track}</span
														>{/if}
												</a>
											{:else}
												<div
													class="-mx-2 flex items-baseline gap-3 px-2 py-1.5 text-muted-foreground"
												>
													<span class="flex-1">{section.title}</span>
													<span class="eyebrow shrink-0">{section.depth}</span>
													<span class="eyebrow shrink-0">not written</span>
												</div>
											{/if}
										</li>
									{/each}
								</ul>
							</div>
						</article>
					{/each}
				</div>
			</section>
		{/each}
	</div>
</main>
