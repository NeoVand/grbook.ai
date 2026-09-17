<script lang="ts">
	import { page } from '$app/state';
	import { toggleMode } from 'mode-watcher';
	import { HugeiconsIcon } from '@hugeicons/svelte';
	import { Moon02Icon, Search01Icon, Settings01Icon, Sun03Icon } from '@hugeicons/core-free-icons';
	import { Button } from '#lib/components/ui/button/index.js';

	let { user }: { user: { name: string; email: string } | null } = $props();

	const links = [
		{ href: '/read', label: 'The book', exact: false },
		{ href: '/learn', label: 'Study notes', exact: true },
		{ href: '/learn/search', label: 'Search', exact: false }
	];

	function active(href: string, exact: boolean) {
		const path = page.url.pathname;
		return exact ? path === href || (path.startsWith(`${href}/`) && !path.startsWith('/learn/search')) : path.startsWith(href);
	}
</script>

<header class="sticky top-0 z-40 border-b bg-background/85 backdrop-blur supports-[backdrop-filter]:bg-background/65">
	<div class="mx-auto flex h-14 max-w-screen-2xl items-center gap-3 px-4">
		<a href="/" class="flex items-center gap-2 font-heading text-[15px] font-semibold tracking-tight">
			<span class="grid size-7 place-items-center rounded-md bg-primary text-xs font-bold text-primary-foreground">G</span>
			<span>grbook<span class="text-muted-foreground">.ai</span></span>
		</a>
		<nav class="ml-2 hidden items-center gap-0.5 text-sm sm:flex">
			{#each links as link (link.href)}
				<a
					href={link.href}
					class="rounded-md px-3 py-1.5 transition-colors hover:bg-muted {active(link.href, link.exact)
						? 'text-foreground'
						: 'text-muted-foreground hover:text-foreground'}"
				>
					{link.label}
				</a>
			{/each}
		</nav>
		<div class="ml-auto flex items-center gap-1">
			<Button variant="ghost" size="icon" href="/learn/search" class="sm:hidden" aria-label="Search">
				<HugeiconsIcon icon={Search01Icon} size={18} />
			</Button>
			<Button variant="ghost" size="icon" onclick={toggleMode} aria-label="Toggle light and dark theme">
				<span class="dark:hidden"><HugeiconsIcon icon={Moon02Icon} size={18} /></span>
				<span class="hidden dark:inline"><HugeiconsIcon icon={Sun03Icon} size={18} /></span>
			</Button>
			{#if user}
				<Button variant="ghost" size="sm" href="/settings">
					<HugeiconsIcon icon={Settings01Icon} size={16} />
					<span class="hidden sm:inline">Settings</span>
				</Button>
			{:else}
				<Button size="sm" href="/login?redirect={encodeURIComponent(page.url.pathname)}">Sign in</Button>
			{/if}
		</div>
	</div>
</header>
