<script lang="ts">
	import { Button } from '#lib/components/ui/button/index.js';
	import Math from '#lib/components/Math.svelte';
	import { DEPTH_LABEL } from '#lib/book/types.js';

	let { data } = $props();

	const promises = [
		{
			title: 'One book, four depths',
			body: 'A section is written at the depth the book has reached. The opening chapters need no calculus; the closing ones sit at research level. Nothing is dumbed down twice or explained once and abandoned.'
		},
		{
			title: 'A tutor that knows the page',
			body: 'Ask out loud, interrupt, think aloud. The tutor works from the same sections you read, knows which check you just missed, and can open the demo that settles the question.'
		},
		{
			title: 'Geometry you can move',
			body: 'Carry an arrow around a sphere and watch it come back turned. Every demo carries its model, its controls and the numbers it must reproduce, so what you move is the physics, not a cartoon.'
		}
	];
</script>

<svelte:head>
	<title>grbook.ai · General relativity, with a tutor beside you</title>
</svelte:head>

<main>
	<section class="border-b border-border">
		<div
			class="mx-auto grid max-w-6xl gap-10 px-5 py-16 sm:px-8 lg:grid-cols-[1.15fr_1fr] lg:py-24"
		>
			<div class="max-w-2xl">
				<p class="eyebrow">Early preview · written in the open</p>
				<h1
					class="mt-3 font-heading text-4xl leading-[1.04] font-semibold tracking-tight text-balance sm:text-6xl"
				>
					General relativity, with a tutor beside you.
				</h1>
				<p class="mt-6 text-lg leading-relaxed text-pretty text-muted-foreground">
					Start from wherever you are: no calculus, or a physics degree. Read, listen, move the
					geometry with your hands, and talk it through until curved spacetime makes sense.
				</p>
				<div class="mt-8 flex flex-wrap gap-3">
					<Button size="lg" href="/read">Start reading</Button>
					{#if data.user}
						<Button size="lg" variant="outline" href="/settings">Connect your keys</Button>
					{:else}
						<Button size="lg" variant="outline" href="/login">Create an account</Button>
					{/if}
				</div>
				<dl class="mt-10 flex flex-wrap gap-x-10 gap-y-4">
					{#each [{ k: 'Sections written', v: `${data.totals.written} of ${data.totals.sections}` }, { k: 'Words of prose', v: data.totals.words.toLocaleString() }, { k: 'Concepts mapped', v: data.totals.concepts.toLocaleString() }] as stat (stat.k)}
						<div>
							<dt class="eyebrow">{stat.k}</dt>
							<dd class="mt-1 font-mono text-lg tabular-nums">{stat.v}</dd>
						</div>
					{/each}
				</dl>
			</div>

			{#if data.excerpt}
				<aside class="border-l-2 border-border bg-card px-5 py-4 lg:px-7">
					<p class="eyebrow">From {data.excerpt.chapter} · {DEPTH_LABEL[data.excerpt.depth]}</p>
					<h2 class="mt-2 font-heading text-xl font-semibold tracking-tight">
						{data.excerpt.title}
					</h2>
					<div class="reading dropcap mt-3 text-[1rem]">{@html data.excerpt.html}</div>
					<a href={data.excerpt.href} class="mt-2 inline-block text-sm text-primary hover:underline"
						>Read this section →</a
					>
				</aside>
			{/if}
		</div>
	</section>

	<section class="mx-auto max-w-6xl px-5 py-16 sm:px-8">
		<div class="grid gap-8 sm:grid-cols-3">
			{#each promises as promise (promise.title)}
				<div class="border-t border-border pt-4">
					<h2 class="font-heading text-lg font-semibold">{promise.title}</h2>
					<p class="mt-2 text-[0.97rem] leading-relaxed text-muted-foreground">{promise.body}</p>
				</div>
			{/each}
		</div>
	</section>

	<section class="border-y border-border">
		<div class="mx-auto grid max-w-6xl gap-8 px-5 py-14 sm:px-8 md:grid-cols-2">
			<div>
				<p class="eyebrow">Where the book is going</p>
				<p class="mt-3 text-muted-foreground">Matter tells spacetime how to curve,</p>
				<div class="mt-2 text-xl" style="color: var(--math-einstein)">
					<Math
						tex={'G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4}\\, T_{\\mu\\nu}'}
						display
					/>
				</div>
				<p class="mt-3 text-muted-foreground">and curved spacetime tells matter how to move.</p>
				<div class="mt-2 text-xl" style="color: var(--math-connection)">
					<Math
						tex={'\\frac{d^2 x^\\mu}{d\\tau^2} + \\Gamma^\\mu{}_{\\alpha\\beta}\\,\\frac{dx^\\alpha}{d\\tau}\\frac{dx^\\beta}{d\\tau} = 0'}
						display
					/>
				</div>
				<p class="mt-3 text-sm text-muted-foreground">
					You will build both equations yourself, one section at a time.
				</p>
			</div>
			<div class="md:border-l md:border-border md:pl-8">
				<p class="eyebrow">Bring your own keys</p>
				<h2 class="mt-2 font-heading text-xl font-semibold">Reading is free</h2>
				<p class="mt-2 text-[0.97rem] leading-relaxed text-muted-foreground">
					The voice tutor uses your OpenAI account and narration uses your ElevenLabs account. Keys
					are encrypted at rest and never sent back to your browser.
				</p>
				<Button variant="secondary" href="/read" class="mt-5">Browse the chapters</Button>
			</div>
		</div>
	</section>
</main>
