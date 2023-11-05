<script>
	import { onMount, afterUpdate } from 'svelte';
	import Card from '$comp/Card.svelte';
  
	let customCarousel;
	export let characters;
  
	// local array to manage displayed characters
	let displayedCharacters = [];
  
	async function* loadCharacters() {
	  function delay(ms) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	  }
	  for (const character of characters) {
		yield character;
		await delay(100); // Delay between character renders
	  }
	}
  
	onMount(async () => {
	  customCarousel.addEventListener('wheel', function (e) {
		if (e.deltaY !== 0) {
		  e.preventDefault();
		  this.scrollLeft += e.deltaY;
		}
	  });
  
	  for await (const character of loadCharacters()) {
		displayedCharacters = [...displayedCharacters, character];
	  }
	});
  
	afterUpdate(() => {
	  if (displayedCharacters.length > 0) {
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
