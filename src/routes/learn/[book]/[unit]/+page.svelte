<script lang="ts">
	import { onMount } from 'svelte';
	import { Badge } from '#lib/components/ui/badge/index.js';
	import { Button } from '#lib/components/ui/button/index.js';
	import Math from '#lib/components/Math.svelte';
	import NarratedText from '#lib/components/audio/NarratedText.svelte';
	import { reading } from '#lib/tutor/reading-context.svelte.js';
	import { formatLocator, type DossierLocator } from '#lib/vault/types.js';

	let { data } = $props();

	const d = $derived(data.dossier);
	const where = (loc: DossierLocator | null | undefined) => formatLocator(data.book.id, loc ?? null);
	const demos = $derived((d?.figures ?? []).filter((f) => f.redesign.form !== 'not-worth-redesigning').sort((a, b) => rank(a.redesign.priority) - rank(b.redesign.priority)));
	const centralEquations = $derived((d?.key_equations ?? []).filter((e) => e.importance !== 'derivation-step'));

	function rank(priority: string) {
		return { high: 0, medium: 1, low: 2 }[priority] ?? 3;
	}

	const nav = $derived(
		[
			{ id: 'overview', label: 'Overview', show: true },
			{ id: 'sections', label: 'Sections', show: true },
			{ id: 'concepts', label: 'Concepts', show: Boolean(d?.concepts.length) },
			{ id: 'equations', label: 'Key equations', show: centralEquations.length > 0 },
			{ id: 'examples', label: 'Worked examples', show: Boolean(d?.worked_examples.length) },
			{ id: 'misconceptions', label: 'Misconceptions', show: Boolean(d?.misconceptions_addressed.length) },
			{ id: 'analogies', label: 'Analogies', show: Boolean(d?.analogies_and_intuitions.length) },
			{ id: 'demos', label: 'Demo ideas', show: demos.length > 0 },
			{ id: 'tutor-notes', label: 'Tutor notes', show: Boolean(d?.tutor_notes.length) }
		].filter((n) => n.show)
	);

	$effect(() => {
		reading.set({ book: data.book.id, bookTitle: data.book.title, unit: data.unit.id, unitTitle: data.unit.title, section: null, selection: null });
	});

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => {
				const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
				const section = visible?.target.getAttribute('data-section');
				if (section) reading.set({ section });
			},
			{ rootMargin: '-20% 0px -60% 0px' }
		);
		for (const el of document.querySelectorAll('[data-section]')) observer.observe(el);

		const onSelection = () => {
			const selection = document.getSelection();
			const text = selection?.toString().trim() ?? '';
			const inside = selection?.anchorNode && document.querySelector('[data-reader]')?.contains(selection.anchorNode);
			reading.set({ selection: inside && text.length > 3 ? text.slice(0, 300) : null });
		};
		document.addEventListener('selectionchange', onSelection);
		return () => {
			observer.disconnect();
			document.removeEventListener('selectionchange', onSelection);
			reading.clear();
		};
	});
</script>

<svelte:head>
	<title>{data.unit.title} · {data.book.short} · grbook.ai</title>
</svelte:head>

<div class="grid gap-10 px-6 py-8 lg:grid-cols-[200px_minmax(0,1fr)]">
	<nav class="sticky top-20 hidden self-start text-sm lg:block" aria-label="On this page">
		<a href="/learn" class="text-xs text-muted-foreground hover:text-foreground">← Library</a>
		<p class="mt-4 mb-2 text-xs font-medium text-muted-foreground">On this page</p>
		<ul class="space-y-1">
			{#each nav as item (item.id)}
				<li><a href="#{item.id}" class="block rounded px-2 py-1 text-muted-foreground hover:bg-muted hover:text-foreground">{item.label}</a></li>
			{/each}
		</ul>
	</nav>

	<article data-reader class="min-w-0 max-w-3xl">
		<header id="overview" class="scroll-mt-20">
			<p class="text-sm text-muted-foreground">
				{data.book.short} · {data.unit.kind === 'appendix' ? `Appendix ${data.unit.label}` : `Chapter ${Number(data.unit.label)}`}
				{#if data.unit.part}· {data.unit.part}{/if}
			</p>
			<h1 class="mt-2 font-heading text-3xl font-semibold tracking-tight text-balance">{data.unit.title}</h1>
			<p class="mt-1 text-sm text-muted-foreground">{data.book.title} · printed pages {data.unit.printedPages[0]}–{data.unit.printedPages[1]}</p>

			{#if d}
				<NarratedText id="summary:{data.book.id}/{data.unit.id}" text={d.one_line_summary} enabled={data.keys.elevenlabs} class="mt-6 text-lg leading-relaxed" />
				<div class="mt-4 flex flex-wrap gap-2">
					<Badge variant="secondary">Math {d.difficulty.math_level}/5</Badge>
					<Badge variant="secondary">Concepts {d.difficulty.conceptual_level}/5</Badge>
					<Badge variant="secondary">Novice-friendly {d.difficulty.novice_friendliness}/5</Badge>
					<Badge variant="outline">{d.verification ? 'Reviewed notes' : 'Notes awaiting review'}</Badge>
				</div>
			{/if}
		</header>

		{#if !d}
			<div class="mt-8 rounded-xl border border-dashed p-6">
				<p class="font-medium">Notes for this chapter are still being written.</p>
				<p class="mt-1 text-sm text-muted-foreground">Here is its outline in the meantime.</p>
				<ul class="mt-4 space-y-1 text-sm">
					{#each data.unit.sections as section (section.number)}
						<li><span class="font-mono text-xs text-muted-foreground">{section.number}</span> {section.title}</li>
					{/each}
				</ul>
			</div>
		{:else}
			<section class="mt-10 space-y-6">
				<div>
					<h2 class="font-heading text-lg font-semibold">Why this chapter is here</h2>
					<p class="mt-2 leading-relaxed text-muted-foreground">{d.role_in_book}</p>
				</div>
				<div>
					<h2 class="font-heading text-lg font-semibold">By the end you can</h2>
					<ul class="mt-2 list-disc space-y-1 pl-5 leading-relaxed">
						{#each d.learning_objectives as objective, i (i)}<li>{objective.replace(/^Reader can /, '')}</li>{/each}
					</ul>
				</div>
				<div>
					<h2 class="font-heading text-lg font-semibold">How the book teaches it</h2>
					<p class="mt-2 leading-relaxed text-muted-foreground">{d.teaching_approach.summary}</p>
					<ol class="mt-3 space-y-2">
						{#each d.teaching_approach.narrative_arc as step, i (i)}
							<li class="flex gap-3 text-sm leading-relaxed">
								<span class="grid size-6 shrink-0 place-items-center rounded-full bg-muted font-mono text-xs">{i + 1}</span>
								<span>{step}</span>
							</li>
						{/each}
					</ol>
				</div>
				{#if d.assumed_background.length}
					<div>
						<h2 class="font-heading text-lg font-semibold">Helpful to know first</h2>
						<ul class="mt-2 flex flex-wrap gap-2">
							{#each d.assumed_background as item, i (i)}<li><Badge variant="outline" class="font-normal">{item.topic}</Badge></li>{/each}
						</ul>
					</div>
				{/if}
			</section>

			<section id="sections" class="mt-14 scroll-mt-20">
				<h2 class="font-heading text-2xl font-semibold">Sections</h2>
				<div class="mt-4 space-y-4">
					{#each d.sections as section, i (i)}
						<div id={section.number ? `section-${section.number}` : undefined} data-section={section.number} class="scroll-mt-20 rounded-xl border p-5">
							<p class="text-xs text-muted-foreground">
								{section.number ? `§${section.number} · ` : ''}p.{section.printed_page ?? '?'}
							</p>
							<h3 class="mt-1 font-medium">{section.title}</h3>
							<p class="mt-2 text-sm leading-relaxed text-muted-foreground">{section.summary}</p>
							{#if section.key_moves.length}
								<ul class="mt-3 list-disc space-y-1 pl-5 text-sm">
									{#each section.key_moves as move, j (j)}<li>{move}</li>{/each}
								</ul>
							{/if}
						</div>
					{/each}
				</div>
			</section>

			{#if d.concepts.length}
				<section id="concepts" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Concepts</h2>
					<div class="mt-4 grid gap-3 md:grid-cols-2">
						{#each d.concepts as concept, i (i)}
							<div class="rounded-xl border p-4">
								<div class="flex items-start gap-2">
									<h3 class="flex-1 font-medium">{concept.name}</h3>
									<Badge variant="secondary" class="shrink-0">{concept.depth}</Badge>
								</div>
								<p class="mt-2 text-sm leading-relaxed">{concept.definition}</p>
								{#each concept.formulas.slice(0, 2) as formula, j (j)}
									<div class="mt-2 text-sm"><Math tex={formula} display /></div>
								{/each}
								<details class="mt-2 text-sm text-muted-foreground">
									<summary class="cursor-pointer select-none">How it is introduced · {where(concept.locators[0])}</summary>
									<p class="mt-2 leading-relaxed">{concept.how_introduced}</p>
								</details>
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if centralEquations.length}
				<section id="equations" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Key equations</h2>
					<div class="mt-4 divide-y rounded-xl border">
						{#each centralEquations as eq, i (i)}
							<div class="p-4">
								<p class="text-xs text-muted-foreground">{[eq.label, eq.name].filter(Boolean).join(' · ')} · {where(eq.locator)}</p>
								<div class="my-2"><Math tex={eq.latex} display /></div>
								<p class="text-sm leading-relaxed text-muted-foreground">{eq.meaning}</p>
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if d.worked_examples.length}
				<section id="examples" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Worked examples</h2>
					<div class="mt-4 space-y-3">
						{#each d.worked_examples as example, i (i)}
							<details class="rounded-xl border p-4">
								<summary class="cursor-pointer select-none">
									<span class="font-medium">{example.label ?? 'Example'}</span>
									<span class="text-sm text-muted-foreground"> · {example.difficulty} · {where(example.locator)}</span>
									<p class="mt-1 text-sm">{example.problem}</p>
								</summary>
								<div class="mt-3 space-y-2 text-sm leading-relaxed">
									<p><span class="font-medium">Method.</span> {example.method}</p>
									<p><span class="font-medium">Key insight.</span> {example.key_insight}</p>
									{#if example.result}<p><span class="font-medium">Result.</span> {example.result}</p>{/if}
								</div>
							</details>
						{/each}
					</div>
				</section>
			{/if}

			{#if d.misconceptions_addressed.length}
				<section id="misconceptions" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Misconceptions to watch for</h2>
					<div class="mt-4 space-y-3">
						{#each d.misconceptions_addressed as item, i (i)}
							<div class="grid gap-3 rounded-xl border p-4 md:grid-cols-2">
								<div>
									<p class="text-xs font-medium text-destructive">Tempting but wrong</p>
									<p class="mt-1 text-sm">{item.misconception}</p>
									<p class="mt-2 text-xs text-muted-foreground">Why it is tempting: {item.why_tempting}</p>
								</div>
								<div>
									<p class="text-xs font-medium" style="color: var(--math-volume)">What is actually true</p>
									<p class="mt-1 text-sm">{item.correction}</p>
								</div>
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if d.analogies_and_intuitions.length}
				<section id="analogies" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Analogies and intuitions</h2>
					<div class="mt-4 grid gap-3 md:grid-cols-2">
						{#each d.analogies_and_intuitions as analogy, i (i)}
							<div class="rounded-xl border p-4">
								<p class="font-medium">{analogy.analogy}</p>
								<p class="text-xs text-muted-foreground">for {analogy.target_concept} · {analogy.effectiveness}</p>
								<p class="mt-2 text-sm leading-relaxed">{analogy.how_used}</p>
								<p class="mt-2 text-xs leading-relaxed text-muted-foreground">Where it breaks down: {analogy.limits}</p>
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if demos.length}
				<section id="demos" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Demo ideas from this chapter</h2>
					<p class="mt-2 text-sm text-muted-foreground">Original interactive designs inspired by the chapter's figures. The first ones are being built.</p>
					<div class="mt-4 grid gap-3 md:grid-cols-2">
						{#each demos as figure, i (i)}
							<div class="rounded-xl border p-4">
								<div class="flex flex-wrap items-center gap-2">
									<Badge variant={figure.redesign.priority === 'high' ? 'default' : 'secondary'}>{figure.redesign.priority}</Badge>
									<Badge variant="outline">{figure.redesign.form}</Badge>
									<span class="text-xs text-muted-foreground">from {figure.label ?? 'a figure'} · {where(figure.locator)}</span>
								</div>
								<p class="mt-2 text-sm leading-relaxed">{figure.redesign.idea}</p>
								<p class="mt-2 text-xs leading-relaxed text-muted-foreground">You would: {figure.redesign.interaction}</p>
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if d.tutor_notes.length}
				<section id="tutor-notes" class="mt-14 scroll-mt-20">
					<h2 class="font-heading text-2xl font-semibold">Notes for the tutor</h2>
					<p class="mt-2 text-sm text-muted-foreground">What the tutor keeps in mind when teaching this chapter.</p>
					<ul class="mt-4 list-disc space-y-2 pl-5 text-sm leading-relaxed">
						{#each d.tutor_notes as note, i (i)}<li>{note}</li>{/each}
					</ul>
				</section>
			{/if}
		{/if}

		<footer class="mt-16 flex flex-wrap justify-between gap-3 border-t pt-6">
			{#if data.prev}
				<Button variant="ghost" href="/learn/{data.book.id}/{data.prev.id}">← {data.prev.title}</Button>
			{:else}<span></span>{/if}
			{#if data.next}
				<Button variant="ghost" href="/learn/{data.book.id}/{data.next.id}">{data.next.title} →</Button>
			{/if}
		</footer>
	</article>
</div>
