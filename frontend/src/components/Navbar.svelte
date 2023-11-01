<script>
	import SandwitchIcon from "$lib/svg/sandwitch.svelte"
</script>
<nav>
	<div>
		<button>
			<SandwitchIcon />
		</button>
	</div>
	<h1>Subordinación y Valor</h1>
	<div></div>
</nav>

<style lang="postcss">
	button {
		@apply hover:bg-primary-900 h-full aspect-square;
	}

	nav {
		@apply p-0 m-0 flex justify-between z-40;
		@apply bg-black;
	}

	h1 {
		@apply text-4xl font-bahiana text-primary-400;
	}
</style>
