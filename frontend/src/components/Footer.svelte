<script>
	import { GithubSolid, EnvelopeSolid } from 'flowbite-svelte-icons';
</script>

<footer>
	<a href="https://github.com/kodexArg/ryf">©️2023 kodexArg</a>
	<address>
		<a href="https://github.com/kodexArg/ryf" target="_blank">
			<GithubSolid size="xs" />
		</a>
		<a href="mailto:kodexarg@gmail.com" target="_blank">
			<EnvelopeSolid size="xs" />
		</a>
	</address>
</footer>

<style lang="postcss">
	footer {
		@apply flex justify-between px-3 p-0.5 bg-primary-900 bg-opacity-50 border-t-2 border-primary-900 drop-shadow-xl;
	}

	address {
		@apply font-overpass flex space-x-2;
	}

	a {
		@apply text-primary-200 text-xs hover:text-white;
	}
</style>
