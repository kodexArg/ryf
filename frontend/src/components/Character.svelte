<script>
	import PowerBar from '$lib/PowerBar.svelte';
	export let character;

	let enlarged = false;
	let currentClass = 'reduced';
	let center;

	function zoom() {
		enlarged = !enlarged;
		currentClass = enlarged ? 'enlarged' : 'reduced';

		// if (enlarged && center) {
		// 	setTimeout(() => {
		// 		center.style.transform = 'translateX(0)';
		// 		const viewportWidth = window.innerWidth;
		// 		const rect = center.getBoundingClientRect();
		// 		let distanceToCenter = viewportWidth / 2 - (rect.left + rect.width / 2);
		// 		distanceToCenter += distanceToCenter < 0 ? 180 : 80;

		// 		center.style.transform = `translateX(${distanceToCenter}px)`;
		// 	}, 1000);
		// } else {
		// 	center.style.transform = 'translateX(0)';
		// }
	}
</script>

{#if enlarged}
	<div class="overlay" />
{/if}

<article class={currentClass} on:dblclick={zoom}>
	<div bind:this={center} class="card {currentClass}">
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
	.card {
		@apply select-none;
		@apply flex flex-col w-[200px] relative mb-8;
		@apply bg-primary-900 rounded-xl;
		@apply transition duration-500;
		@apply outline outline-2 outline-primary-900;
		box-shadow: 1rem 1rem 1rem rgb(0, 0, 0, 0.75), 0 0 2rem #000;
	}

	.enlarged {
		@apply transition ease-in-out duration-700;
		@apply z-50 scale-[115%] sm:scale-110 -translate-y-6 sm:-translate-y-2 translate-x-16;
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

	article:not(:last-child):not(.enlarged) .card:hover {
		@apply translate-x-16 z-50;
	}

	article:last-child .card:hover {
		@apply z-50;
	}

	article:not(:last-child) {
		@apply -ml-16;
	}

	:has(+ article:hover) {
		@apply translate-x-5;
	}

	article:last-child {
		@apply ml-4;
	}

	/* card picture */
	.card-image {
		@apply w-[200px] aspect-[0.625] relative;
		@apply rounded-t-xl bg-cover;
		@apply flex overflow-hidden;
		background-image: var(--img-url);
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
		@apply py-0.5 pl-2 pr-0.5 mb-1 mt-0.5 rounded-sm;
		@apply font-overpass-mono text-xs tracking-tight leading-none text-primary-50;
		@apply bg-black rounded-l-full bg-opacity-60;
	}
</style>
