<script lang="ts">
	import { DEPTH_LABEL } from '#lib/book/types.js';

	let { data } = $props();
	const s = $derived(data.section);
	const number = $derived(
		data.chapter ? data.chapter.sections.findIndex((x) => x.id === s.id) + 1 : 0
	);
</script>

<svelte:head>
	<title>{s.title} · grbook.ai</title>
	<meta name="description" content={s.summary} />
</svelte:head>

<div
	class="mx-auto grid max-w-6xl gap-x-12 px-5 py-8 sm:px-8 lg:grid-cols-[15rem_minmax(0,1fr)] lg:py-12"
>
	<!-- Chapter contents -->
	<nav class="lg:sticky lg:top-20 lg:self-start" aria-label="Chapter contents">
		<a href="/read" class="eyebrow hover:text-primary">← All chapters</a>
		<p class="mt-2 font-heading text-lg leading-tight font-semibold">{s.chapterTitle}</p>
		<p class="mt-1 text-sm text-muted-foreground">{s.partTitle}</p>
		<ol class="mt-4 space-y-0.5 lg:max-h-[60vh] lg:overflow-y-auto">
			{#each data.chapter?.sections ?? [] as item, i (item.id)}
				<li>
					{#if item.written}
						<a
							href="/read/{s.chapter}/{item.id}"
							aria-current={item.id === s.id ? 'page' : undefined}
							class="-mx-2 flex gap-2 rounded px-2 py-1.5 text-sm leading-snug transition-colors {item.id ===
							s.id
								? 'bg-accent font-semibold text-accent-foreground'
								: 'text-muted-foreground hover:bg-accent/60 hover:text-foreground'}"
						>
							<span class="font-mono text-[11px] tabular-nums opacity-70">{i + 1}</span>
							<span>{item.title}</span>
						</a>
					{:else}
						<div class="-mx-2 flex gap-2 px-2 py-1.5 text-sm leading-snug text-muted-foreground/60">
							<span class="font-mono text-[11px] tabular-nums opacity-70">{i + 1}</span>
							<span>{item.title}</span>
						</div>
					{/if}
				</li>
			{/each}
		</ol>
	</nav>

	<main class="max-w-[43rem] min-w-0">
		<header class="border-b-2 border-foreground pb-4">
			<div class="flex flex-wrap items-center gap-x-3 gap-y-1">
				<span class="eyebrow">Section {number}</span>
				<span
					class="rounded-sm border border-primary px-1.5 py-0.5 font-mono text-[11px] tracking-wider text-primary uppercase"
					>{DEPTH_LABEL[s.depth]}</span
				>
				{#if s.track !== 'main'}
					<span
						class="rounded-sm border border-border px-1.5 py-0.5 font-mono text-[11px] tracking-wider text-muted-foreground uppercase"
						>{s.track} track</span
					>
				{/if}
				<span class="eyebrow">{s.words.toLocaleString()} words</span>
			</div>
			<h1
				class="mt-3 font-heading text-4xl leading-[1.08] font-semibold tracking-tight text-balance sm:text-[2.75rem]"
			>
				{s.title}
			</h1>
			<p class="mt-4 font-heading text-lg leading-snug text-muted-foreground">{s.summary}</p>
		</header>

		<div class="reading dropcap mt-8">{@html data.html.opening}</div>

		{#each data.html.parts as part, i (part.id)}
			<section class="mt-10">
				<h2 class="font-heading text-2xl leading-tight font-semibold tracking-tight text-balance">
					<span class="eyebrow block">{number}.{i + 1}</span>
					{part.heading}
				</h2>
				<div class="reading mt-4">{@html part.text}</div>
				<p class="mt-5 border-l-2 border-primary pl-4 font-heading text-[1.05rem] leading-snug">
					{@html part.takeaway}
				</p>
			</section>
		{/each}

		<!-- Apparatus: what the book carries beside its prose -->
		<div class="mt-16 border-t border-border pt-8">
			{#if data.html.equations.length}
				<h2 class="eyebrow">Key equations</h2>
				<div class="mt-4 space-y-6">
					{#each data.html.equations as eq (eq.id)}
						<div class="border-b border-border/70 pb-5 last:border-0">
							<div class="flex flex-wrap items-baseline gap-x-3">
								<h3 class="font-heading text-[1.05rem] font-semibold">{eq.name}</h3>
								<span class="eyebrow">{eq.justified.replace('-', ' ')}</span>
							</div>
							<div class="math-display mt-2 overflow-x-auto">{@html eq.latexHtml ?? ''}</div>
							<p class="mt-2 text-[0.97rem] text-muted-foreground">{@html eq.meaning}</p>
							<p class="mt-2 text-sm text-muted-foreground/80 italic">Spoken: “{eq.say_aloud}”</p>
						</div>
					{/each}
				</div>
			{/if}

			{#if data.html.checks.length}
				<h2 class="eyebrow mt-12">Check yourself</h2>
				<div class="mt-3">
					{#each data.html.checks as check, i (check.id)}
						<details class="border-b border-border/70 py-3">
							<summary class="flex cursor-pointer list-none items-baseline gap-3">
								<span class="shrink-0 font-mono text-[11px] tracking-wider text-primary uppercase"
									>Check {i + 1}</span
								>
								<span class="flex-1">{@html check.question}</span>
							</summary>
							<div class="reading mt-3 text-[0.97rem] text-muted-foreground sm:pl-[5.5rem]">
								{@html check.answer}
								<ul class="mt-2">
									{#each check.key_points as point (point)}<li>{@html point}</li>{/each}
								</ul>
							</div>
						</details>
					{/each}
				</div>
			{/if}

			{#if data.html.misconceptions.length}
				<h2 class="eyebrow mt-12">Where readers go wrong</h2>
				<div class="mt-3 space-y-4">
					{#each data.html.misconceptions as m (m.id)}
						<div>
							<p class="font-heading text-[1.02rem] italic">“{m.belief}”</p>
							<p class="mt-1 text-[0.97rem] text-muted-foreground">{@html m.correction}</p>
						</div>
					{/each}
				</div>
			{/if}

			{#if s.visuals.length}
				<h2 class="eyebrow mt-12">Figures and demos</h2>
				<div class="mt-3 grid gap-3 sm:grid-cols-2">
					{#each s.visuals as v (v.id)}
						<article class="rounded-md border border-border bg-card p-4">
							<div class="flex flex-wrap items-baseline justify-between gap-2">
								<h3 class="font-heading text-[1.02rem] font-semibold">
									{v.catalog?.title ?? v.id.replace(/-/g, ' ')}
								</h3>
								<span
									class="rounded-sm px-1.5 py-0.5 font-mono text-[10px] tracking-wider uppercase {v
										.catalog?.reviewed
										? 'bg-accent text-accent-foreground'
										: 'bg-muted text-muted-foreground'}"
								>
									{v.catalog?.reviewed ? 'Specified' : 'Sketch only'}
								</span>
							</div>
							<p class="mt-2 text-sm leading-snug text-muted-foreground">
								{v.catalog?.caption ?? v.role}
							</p>
							{#if v.catalog}
								<p class="eyebrow mt-3 flex flex-wrap gap-x-3 gap-y-1">
									<span>{v.catalog.kind}</span>
									<span>{v.catalog.counts.params} controls</span>
									<span>{v.catalog.counts.tours} tours</span>
									<span>{v.catalog.counts.tests} tests</span>
								</p>
							{/if}
						</article>
					{/each}
				</div>
				<p class="mt-3 text-sm text-muted-foreground">
					These are written specifications: controls, guided tours and numerical tests. The
					components are not built yet.
				</p>
			{/if}

			{#if data.html.glossary.length}
				<h2 class="eyebrow mt-12">Terms introduced here</h2>
				<dl class="mt-3 space-y-2">
					{#each data.html.glossary as g (g.id)}
						<div class="grid gap-x-4 sm:grid-cols-[10rem_1fr]">
							<dt class="font-semibold">{g.term}</dt>
							<dd class="text-muted-foreground">{@html g.plain_definition}</dd>
						</div>
					{/each}
				</dl>
			{/if}

			<h2 class="eyebrow mt-12">Concepts taught here</h2>
			<p class="mt-2 flex flex-wrap gap-x-2 gap-y-1 text-sm">
				{#each s.teachesTitles as c (c.id)}
					<span class="rounded-sm border border-border px-1.5 py-0.5 text-muted-foreground"
						>{c.title}</span
					>
				{/each}
			</p>
		</div>

		<nav class="mt-12 flex justify-between gap-4 border-t border-border pt-5">
			{#if data.prev}
				<a
					href="/read/{data.prev.chapter}/{data.prev.id}"
					class="max-w-[48%] rounded border border-border p-3 transition-colors hover:border-primary hover:text-primary"
				>
					<span class="eyebrow block">Previous</span>
					<span class="text-[0.97rem]">{data.prev.title}</span>
				</a>
			{:else}
				<span></span>
			{/if}
			{#if data.next}
				<a
					href="/read/{data.next.chapter}/{data.next.id}"
					class="max-w-[48%] rounded border border-border p-3 text-right transition-colors hover:border-primary hover:text-primary"
				>
					<span class="eyebrow block">Next</span>
					<span class="text-[0.97rem]">{data.next.title}</span>
				</a>
			{/if}
		</nav>
	</main>
</div>
