<script>
    import Deck from "$comp/Deck.svelte"
    export let data;
	export let characters = data.props.characters;

</script>

<main>
    <Deck {characters} />
</main>
