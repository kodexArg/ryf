<script>
	import Icon from '$lib/Icon.svelte'

</script>

<footer class="flex h-5 justify-between items-end px-2 bg-black">
	<a class="text-primary-200 text-xs hover:text-primary-100"
	   href="https://github.com/kodexArg/ryf">
	   ©️2023 <strong>kodexArg</strong>
	</a>
	<address class="flex justify-between items-center space-x-1 px-3">
		<a href="https://github.com/kodexArg/ryf" 
		   target="_blank"
		   class="text-primary-200 text-xs hover:text-primary-100"
		   >
			<Icon svg="github" class="w-4 h-4 text-primary-300 hover:text-white" />

		</a>
		<a href="mailto:kodexarg@gmail.com" 
		   target="_blank"
		   class="text-primary-200 text-xs hover:text-primary-100"
		   >
			<Icon svg="envelop" class="w-4 h-4 text-primary-300 hover:text-white"/>

		</a>
	</address>
</footer>
