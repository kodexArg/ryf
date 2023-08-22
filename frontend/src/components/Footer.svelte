<script>
	import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from 'flowbite-svelte';
	import { DarkMode } from 'flowbite-svelte';
	import { Icon } from 'flowbite-svelte-icons';
</script>

<Footer class="rounded-none bg-primary-50 !py-1">
	<FooterCopyright href="https://github.com/kodexArg" by="kodexArg" year={2023} copyrightMessage="MIT License"/>
	<FooterLinkGroup ulClass="flex flex-wrap text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
    <FooterLink href="https://github.com/kodexArg" target="_blank"><Icon name="github-solid" /></FooterLink>
		<FooterLink href="mailto:kodexarg@gmail.com?subject=[Subordinación y Valor]" target="_blank">
      <Icon name="envelope-solid" />
		</FooterLink>
    <DarkMode btnClass=""/>
	</FooterLinkGroup>
</Footer>
