<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import Icon from '$lib/Icon.svelte';

	const goSomeWhereBack = () => {
		const backPath = $page.url.pathname.substring(0, $page.url.pathname.lastIndexOf('/'));
		goto(backPath || '/');
	};
</script>

<nav class="h-11 flex justify-between items-center z-40 bg-black">
	<div>
		{#if $page.url.pathname === '/'}
			<button class="hover:bg-primary-900 flex ml-1">
				<Icon svg="sandwitch" class="w-11 h-11 p-1 text-primary-500" />
			</button>
		{:else}
			<button class="hover:bg-primary-900 flex ml-1" on:click={goSomeWhereBack}>
				<Icon svg="back-arrow" class="w-11 h-11 p-1 text-primary-500" />
			</button>
		{/if}
	</div>
	<h1 class="pt-1 text-4xl font-bahiana text-primary-400">Subordinación y Valor</h1>
	<div />
</nav>
