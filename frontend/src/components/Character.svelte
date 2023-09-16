<script>
	let vCard = false;
	export let character;
</script>

<article>
	<div class="card">
		<div class="card-image" style="--img-url: url('/characters/{character.portrait}')">
			<div class="overimage">
				<div class="name">
					{character.firstName}
					{character.lastName}
				</div>
				<div class="overimage2">
					<div class="occupation">
						{character.mainOccupation}
					</div>
					<div class="age">
						{character.age} años
					</div>
				</div>
			</div>
		</div>

		<div class="card-text">Biografía</div>
	</div>
</article>

<style lang="postcss">
	.card {
		@apply w-[220px] h-fit m-2;
		@apply bg-primary-900 rounded-t-xl;
		@apply shadow-sm shadow-primary-900;
		transition: 350ms ease-in-out;
	}

	.card:hover {
		scale: 1.05;
	}

	.card-image {
		@apply w-[220px] h-[320px] relative;
		@apply rounded-t-xl bg-cover;
		background-image: var(--img-url);
	}

	.overimage {
		@apply bottom-0 right-4 absolute;
		@apply font-bahiana text-primary-50 leading-none text-2xl text-right;
		text-shadow: 2px 2px 3px rgb(0, 0, 0, 0.5);
	}

	.overimage2 {
		@apply flex space-x-2 font-overpass text-xs justify-end;
	}

	.card-text {
		@apply text-primary-500 uppercase font-overpass p-1;
	}
</style>
