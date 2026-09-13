<script lang="ts">
	import './layout.css';
	import favicon from '#lib/assets/favicon.svg';
	import { ModeWatcher } from 'mode-watcher';
	import { Toaster } from '#lib/components/ui/sonner/index.js';
	import AppHeader from '#lib/components/app/AppHeader.svelte';

	let { children, data } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>grbook.ai · General relativity with a tutor</title>
</svelte:head>

<ModeWatcher />
<Toaster />

<div class="min-h-dvh bg-background">
	<AppHeader user={data.user} />
	{@render children()}
</div>
