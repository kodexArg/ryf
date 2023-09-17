<script>
	import { onMount } from 'svelte';
	import Character from './Character.svelte';
	let characters = [];

	onMount(async () => {
		const response = await fetch('/characters.json');
		const data = await response.json();
		characters = data.characters;
	});
	
</script>

<section>
	<div class="custom-carousel">
		{#each characters as character, index}
		<Character {character} {index} />
		{/each}
	</div>
</section>

<style lang="postcss">
	section {
		@apply w-full h-full overflow-x-hidden z-0 mb-32 sm:mb-0;
	}

	.custom-carousel {
		@apply w-full h-full flex overflow-x-scroll overflow-y-hidden pt-4 touch-pan-x;
		@apply flex-row-reverse items-end pl-12 pr-32;
	}


	/* TODO: Firefox doesn't work with webkit */
	::-webkit-scrollbar {
		@apply z-50;
	}

	::-webkit-scrollbar-track {
		@apply rounded-full;
		box-shadow: inset 0 0 7px grey;
	}

	::-webkit-scrollbar-thumb {
		@apply bg-primary-600 rounded-full;
	}
</style>