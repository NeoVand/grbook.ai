<script lang="ts">
	import { Button } from '#lib/components/ui/button/index.js';
	import Math from '#lib/components/Math.svelte';

	let { data } = $props();

	const pillars = [
		{
			title: 'Taught the way great books teach',
			body: 'Every chapter of three celebrated textbooks has been studied for how it teaches: the questions it opens with, the pictures it draws, the mistakes it heads off. The course keeps the best moves from each.'
		},
		{
			title: 'A tutor you can talk to',
			body: 'Ask out loud, interrupt, think aloud. The tutor knows which page you are on, what you have already understood, and where the course explains each idea best.'
		},
		{
			title: 'Geometry you can move',
			body: 'Carry an arrow around a sphere and watch it come back rotated. Release a cloud of particles near a star and watch tides stretch it. Every demo names its model and its limits.'
		}
	];
</script>

<svelte:head>
	<title>grbook.ai · General relativity, with a tutor beside you</title>
</svelte:head>

<main>
	<section class="relative overflow-hidden border-b">
		<div
			aria-hidden="true"
			class="pointer-events-none absolute inset-0 opacity-60 [background:radial-gradient(60rem_30rem_at_70%_-10%,color-mix(in_oklch,var(--math-connection)_22%,transparent),transparent),radial-gradient(40rem_24rem_at_10%_110%,color-mix(in_oklch,var(--math-riemann)_18%,transparent),transparent)]"
		></div>
		<div class="relative mx-auto grid max-w-screen-xl gap-12 px-6 py-20 md:grid-cols-[1.2fr_1fr] md:py-28">
			<div>
				<p class="mb-4 text-sm font-medium tracking-wide text-muted-foreground">Early preview</p>
				<h1 class="font-heading text-4xl leading-[1.05] font-semibold tracking-tight text-balance md:text-6xl">
					General relativity, with a tutor beside you.
				</h1>
				<p class="mt-6 max-w-xl text-lg text-pretty text-muted-foreground">
					Start from wherever you are. Read, listen, move the geometry with your hands, and talk it through until
					curved spacetime makes sense.
				</p>
				<div class="mt-8 flex flex-wrap gap-3">
					<Button size="lg" href="/learn">Start learning</Button>
					{#if data.user}
						<Button size="lg" variant="outline" href="/settings">Connect your keys</Button>
					{:else}
						<Button size="lg" variant="outline" href="/login">Create an account</Button>
					{/if}
				</div>
			</div>
			<div class="flex items-center">
				<div class="w-full rounded-xl border bg-card/80 p-6 shadow-sm backdrop-blur">
					<p class="text-sm text-muted-foreground">Matter tells spacetime how to curve</p>
					<div class="my-4 text-xl" style="color: var(--math-einstein)">
						<Math tex={'G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4}\\, T_{\\mu\\nu}'} display />
					</div>
					<p class="text-sm text-muted-foreground">and curved spacetime tells matter how to move</p>
					<div class="my-4 text-xl" style="color: var(--math-connection)">
						<Math tex={'\\frac{d^2 x^\\mu}{d\\tau^2} + \\Gamma^\\mu{}_{\\alpha\\beta}\\,\\frac{dx^\\alpha}{d\\tau}\\frac{dx^\\beta}{d\\tau} = 0'} display />
					</div>
					<p class="text-xs text-muted-foreground">You will build both equations yourself, one idea at a time.</p>
				</div>
			</div>
		</div>
	</section>

	<section class="mx-auto grid max-w-screen-xl gap-6 px-6 py-16 md:grid-cols-3">
		{#each pillars as pillar (pillar.title)}
			<div class="rounded-xl border p-6">
				<h2 class="font-heading text-lg font-semibold">{pillar.title}</h2>
				<p class="mt-3 text-sm leading-relaxed text-muted-foreground">{pillar.body}</p>
			</div>
		{/each}
	</section>

	<section class="border-t">
		<div class="mx-auto flex max-w-screen-xl flex-col items-start gap-4 px-6 py-14 md:flex-row md:items-center md:justify-between">
			<div>
				<h2 class="font-heading text-xl font-semibold">Bring your own keys</h2>
				<p class="mt-2 max-w-2xl text-sm text-muted-foreground">
					Reading is free. The voice tutor uses your OpenAI account and narration uses your ElevenLabs account. Keys
					are encrypted at rest and never sent back to your browser.
				</p>
			</div>
			<Button variant="secondary" href="/learn">Browse the course</Button>
		</div>
	</section>
</main>
