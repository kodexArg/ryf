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
	{#each characters as character}
		<Character {character} />
	{/each}
</section>

<style lang="postcss">
	section {
		@apply flex;
	}
</style>
