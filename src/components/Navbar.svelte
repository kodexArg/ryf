<script>
	import { onDestroy } from 'svelte';
	import { fade } from 'svelte/transition';
	import { page } from '$app/stores';
	import { goSomeWhereBack } from '$lib/helpers.js';
	import Icon from '$lib/Icon.svelte';
	import SquareButton from '$lib/SquareButton.svelte';

	let showPopup = false;
	let showPopupTimer; // time before fading out
	let transitionConfig = { duration: 200 }; // config for transitions used here

	const togglePopup = () => {
		showPopup = !showPopup;
		if (showPopup) {
			setTimer();
		}
	};

	const setTimer = () => {
		clearTimer();
		showPopupTimer = setTimeout(() => {
			showPopup = false;
		}, 2000);
	};

	const resetTimer = () => clearTimer();

	const clearTimer = () => {
		if (showPopupTimer) clearTimeout(showPopupTimer);
	};

	onDestroy(clearTimer);
</script>

<nav class="z-50 h-12 flex justify-between items-center bg-black px-3">
	<h1 class="text-4xl font-bahiana text-primary-500">Subordinación y Valor</h1>
	<div class="flex h-11 space-x-3 w-fit">
		{#if $page.url.pathname !== '/'}
			<button on:click={goSomeWhereBack} transition:fade={transitionConfig}>
				<Icon
					svg="back-arrow"
					class="w-11 h-11 p-1 text-primary-500 hover:text-primary-400 hover:scale-95"
				/>
			</button>
		{/if}
		<button
			on:click={togglePopup}
			on:mouseover={() => (showPopup = true)}
			class:scale-95={showPopup}
			class="w-11 h-11"
		>
			<Icon svg="sandwitch" class="w-11 h-11 p-1 text-primary-500 hover:text-primary-400 " />
		</button>
	</div>
</nav>

{#if showPopup}
	<div
		on:mouseover={resetTimer}
		on:mouseout={setTimer}
		on:click={() => (showPopup = false)}
		class="fixed z-50 mt-1 right-2 top-12 flex flex-col items-end space-y-1 mr-0.5"
		transition:fade={transitionConfig}
	>
		<SquareButton icon="home" text="Cuartel General" href="/" />
		<SquareButton icon="officer" text="Personajes Generados" href="/personajes" />
		<SquareButton icon="secrets" text="Archivos Secretos" href="/" />
		<SquareButton icon="ryf" text="Sistema de Juego" href="/sistema" />
	</div>
{/if}
