<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import Footer from '../components/Footer.svelte';
	import Navbar from '../components/Navbar.svelte';

	onMount(() => {
		setTimeout(() => {
			const img = new Image();
			img.src = '/assets/bg/full.jpg';

			img.onload = () => {
				const bgDiv = document.querySelector('.bg-div');
				bgDiv.style.backgroundImage = `url(${img.src})`;
			};
		}, 0);
	});
</script>

<section class="background-image">
	<div class="bg-div"></div>
	<Navbar />
	<div class="content">
		<slot />
	</div>
	<Footer />
</section>

<style lang="postcss">
	:global(html),

	:global(:focus) {
  	outline: none;
    box-shadow: none;
	  -webkit-tap-highlight-color: transparent;

	}

	:global(body) {
		@apply h-full m-0;
	}

	
	section {
		@apply flex flex-col h-screen relative;
	}

  .content {
		@apply flex-grow overflow-y-auto text-justify;
	}

	:global(main) {
		@apply w-full h-full flex justify-center items-center;
	}

	:global(html) {
		@apply font-overpass;
	}

	.bg-div {
		@apply absolute inset-0 bg-no-repeat bg-cover bg-center;
		background-image: url('/assets/bg/min.jpg');
		opacity: 0.2; 
		z-index: -1;
	}

	.background-image::before {
		content: '';
		position: absolute;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		z-index: -2;
		/* background: linear-gradient(#647055, #292929); */
		@apply bg-gradient-to-b from-primary-500 to-primary-900;
	}
</style>
