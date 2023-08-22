<script>
	import { Navbar, NavBrand } from 'flowbite-svelte';
</script>

<Navbar color="primary">
	<NavBrand href="/"><span id="Title">Subordinación y Valor</span></NavBrand>
</Navbar>

<style>
	#Title {
		@apply font-bahiana text-3xl leading-none;
	}
</style>
