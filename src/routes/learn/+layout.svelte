<script lang="ts">
	import { HugeiconsIcon } from '@hugeicons/svelte';
	import { SparklesIcon } from '@hugeicons/core-free-icons';
	import * as Sheet from '#lib/components/ui/sheet/index.js';
	import { buttonVariants } from '#lib/components/ui/button/index.js';
	import TutorDock from '#lib/components/tutor/TutorDock.svelte';
	import { tutor } from '#lib/tutor/live-client.svelte.js';

	let { children, data } = $props();
	let open = $state(false);
</script>

<div class="mx-auto flex max-w-screen-2xl">
	<div class="min-w-0 flex-1">
		{@render children()}
	</div>
	<aside class="sticky top-14 hidden h-[calc(100dvh-3.5rem)] w-[360px] shrink-0 border-l xl:block">
		<TutorDock signedIn={Boolean(data.user)} keys={data.keys} />
	</aside>
</div>

<div class="fixed right-4 bottom-4 z-30 xl:hidden">
	<Sheet.Root bind:open>
		<Sheet.Trigger class="{buttonVariants({ size: 'lg' })} rounded-full shadow-lg">
			<HugeiconsIcon icon={SparklesIcon} size={16} />
			{tutor.status === 'live' ? 'Tutor is listening' : 'Tutor'}
		</Sheet.Trigger>
		<Sheet.Content side="right" class="w-full p-0 sm:max-w-md">
			<Sheet.Title class="sr-only">Tutor</Sheet.Title>
			<TutorDock signedIn={Boolean(data.user)} keys={data.keys} />
		</Sheet.Content>
	</Sheet.Root>
</div>
