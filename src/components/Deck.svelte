<script>
	import { onMount, afterUpdate } from 'svelte';
	import Card from './Card.svelte';

	let customCarousel;
	let characters = []

	async function* fetchCharacters() {
		function delay(ms) {
			return new Promise((resolve) => setTimeout(resolve, ms));
		}
		const response = await fetch('/characters.json');
		const data = await response.json();
		console.log(data)
		for (const character of data.characters) {
			yield character;
			await delay(100);
		}
	}

	onMount(async () => {
		// scroll with the wheel
		customCarousel.addEventListener('wheel', function (e) {
			if (e.deltaY !== 0) {
				e.preventDefault();
				this.scrollLeft += e.deltaY;
			}
		});

		// load characters one by one
		for await (const character of fetchCharacters()) {
			characters = [...characters, character];
		}
	});

	afterUpdate(() => {
		if (characters.length > 0) {
			const customCarousel = document.querySelector('.custom-carousel');
			const newScrollPosition = -customCarousel.clientWidth;
			customCarousel.scrollTo({
				behavior: 'smooth'
			});
		}
	});
</script>
<section>
	<div class="custom-carousel" bind:this={customCarousel}>
		{#each characters as character}
			<div />
			<Card {character} />
		{/each}
	</div>
</section>

<style>
	section {
		@apply w-full h-full overflow-x-hidden z-0;
	}

	.custom-carousel {
		@apply w-full h-full flex overflow-x-scroll overflow-y-hidden pt-4 touch-pan-x;
		@apply flex-row-reverse items-end pl-12 pr-32;
	}

	/* TODO: Firefox doesn't work with webkit */
	::-webkit-scrollbar {
		@apply z-40;
	}

	::-webkit-scrollbar-track {
		@apply rounded-full;
		box-shadow: inset 0 0 7px grey;
	}

	::-webkit-scrollbar-thumb {
		@apply bg-primary-600 rounded-full;
	}
</style>
