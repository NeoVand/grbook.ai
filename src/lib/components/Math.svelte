<script lang="ts">
	import { renderMath } from '#lib/math/render.js';

	let { tex, display = false, class: className = '' }: { tex: string; display?: boolean; class?: string } = $props();

	const html = $derived(renderMath(tex, display));
</script>

{#if display}
	<div class="math-display overflow-x-auto py-1 {className}">{@html html}</div>
{:else}
	<span class="math-inline {className}">{@html html}</span>
{/if}
