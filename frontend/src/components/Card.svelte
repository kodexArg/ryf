<script>
	import { goto } from '$app/navigation';
	import { fly } from 'svelte/transition';
	import PowerBar from '$lib/PowerBar.svelte';
	export let character;

	let clickTimeout;
	let card;
	let enlarged = false;
	let leaving = false;

	function handleCardClick() {
		if (enlarged) {
			clickTimeout = setTimeout(() => {
				if (!leaving) {
					enlarged = false;
				} else {
				}
			}, 250); // delay to check for double click
		}
	}

	function handleCardDoubleClick() {
		if (clickTimeout) clearTimeout(clickTimeout); // prevent single click action
		if (enlarged) {
			leaving = true;
			goto(`/characters/${character.slug}`)
		} else {
			enlarged = true;
		}
	}
	

</script>

{#if enlarged}
	<div class="overlay" 
	     on:click={() => (enlarged = false)} 
	     on:keydown={(e) => e.key === 'Enter' && (enlarged = false)} 
	     tabindex="-1" 
	     role="button" />
{/if}

<article class:enlarged class:reduced={!enlarged}>
	<div
		class="card"
		class:enlarged
		class:reduced={!enlarged}
		class:centered={enlarged}
		bind:this={card}
		on:dblclick={handleCardDoubleClick}
		on:click={handleCardClick}
		tabindex="-1"
		role="button"
		on:keydown={(e) => e.key === 'Enter' && handleCardDoubleClick()}
		in:fly={{ x: 100, y:500, duration: 400, opacity: 90 }}
	>
		<div class="card-image" style="--img-url: url('/characters/{character.portrait}')">
			<div class="over-image">
				<div class="name">
					{#if character.title}{character.title}<br />{/if}
					{character.firstName}
					{character.lastName}
				</div>
				<div class="subtitle">
					<div class="occupation">
						{character.mainOccupation}{#if character.secondaryOccupation}/{character.secondaryOccupation}{/if}
					</div>
				</div>
			</div>
		</div>

		<div class="m-2">
			{#each Object.entries(character.stats) as [key, value]}
				<PowerBar stat={key} number={value} />
			{/each}
		</div>
	</div>
</article>

<style lang="postcss">
	/* TODO: anidation (future) */
	.card {
		@apply select-none;
		@apply flex flex-col w-[200px] relative mb-8;
		@apply bg-primary-900 rounded-xl;
		@apply transition duration-500;
		@apply outline outline-2 outline-primary-900;
		box-shadow: 1rem 1rem 1rem rgb(0, 0, 0, 0.75), 0 0 2rem #000;
		@apply cursor-pointer;
	}

	.enlarged {
		@apply transition ease-in-out duration-300;
		@apply z-50 scale-[115%] -translate-y-6 translate-x-16;
	}

	@media (min-width: 640px) {
		.enlarged {
			@apply scale-110 -translate-y-2;
		}
	}

	.enlarged .card {
		@apply bg-primary-100;
	}

	.reduced {
		@apply transition ease-in-out duration-500;
		@apply z-0 scale-100;
	}

	.overlay {
		@apply fixed -left-20 inset-0 bg-primary-900 opacity-50 z-30;
	}

	.centered {
		@apply transition ease-in-out delay-100 duration-500 -translate-x-4;
		@apply bg-red-500;
	}

	article:not(:last-child) {
		@apply -ml-16;
	}

	article:last-child {
		@apply ml-4;
	}

	/* looks like a :has :not tutorial... let's comment this nightmare for the Gabriel of the future: */
	/* the items are rendering from back to front using flex-row-reverse in the Characters.svelte component, so last-child is actually the first element at left of the screen... and this is important! */

	/* HOVER! (focus!) */
	article:not(:last-child):not(.enlarged) .card:hover {
		@apply translate-x-16;
	}

	/* first sibiling displacement */
	article:has(+ article:hover) {
		@apply translate-x-12;
	}

	/* first sibiling is second element displacement (overwrite) */
	article:has(+ article:hover):has(+ article:last-child) {
		@apply translate-x-4;
	}

	/* second sibiling is third element displacement (overwrite) */
	:has(+ * + article:hover):has(+ * + article:last-child) {
		@apply translate-x-2;
	}

	/* card picture */
	.card-image {
		@apply w-[200px] aspect-[0.625] relative;
		@apply rounded-t-xl bg-cover;
		@apply flex overflow-hidden;
		background-image: var(--img-url);
		@apply filter contrast-[120%];
	}

	/* container for text over image */
	.over-image {
		@apply bottom-0 right-0 absolute flex flex-col items-end;
	}

	/* character's name */
	.over-image .name {
		@apply font-bahiana text-primary-50 text-right text-2xl font-bold tracking-wider leading-none pr-3;
		-webkit-text-stroke: 0.1px black;
		text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
	}

	/* profession tag black background */
	.subtitle {
		@apply pt-0.5 pl-2 pr-0.5 mb-1 mt-0.5 rounded-sm;
		@apply font-overpass-mono text-xs tracking-tight leading-none text-primary-50;
		@apply bg-black rounded-l-full bg-opacity-50;
	}
</style>
