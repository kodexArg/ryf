<script>
	import Icon from '$lib/Icon.svelte';
	import { fade } from 'svelte/transition';

	export let text;
	export let icon;
	export let href = '/';
	
	let showText = false;
	let timeout;

	const setVis = (forceValue) => {
		if (timeout) clearTimeout(timeout);

		if (typeof forceValue === 'boolean') {
			showText = forceValue;
		} else {
			if (showText) {
				timeout = setTimeout(() => {
					showText = false;
				}, 150);  // delay in ms.
			} else {
				showText = true;
			}
		}
	};
</script>

<div class="z-50" aria-hidden="true" on:mouseover={() => setVis(true)} on:mouseout={() => setVis()} >
	<a
		class="flex space-x-3 items-center justify-end p-1 shadow hover:shadow-primary-600 bg-primary-400 hover:bg-opacity-100 bg-opacity-50 rounded-lg overflow-hidden"
		href={href}
		role="button"
	>
		{#if showText}
			<p in:fade={{duration: 200}} 
                class="text-right text-primary-900 w-24 font-overpass-mono leading-4">
		        {text}
			</p>
		{/if}
		<Icon svg={icon} class="w-10 h-10 p-1 bg-primary-900 text-primary-500 rounded-lg border border-black" />
	</a>
</div>
