<!-- Markdown.svelte -->
<script>
	import { onMount } from 'svelte';
	import MarkdownIt from 'markdown-it';

	export let md = ''; // This will take the name of the markdown file without the extension
	export let extraClass = ''; // This allows passing a class to the container

	let markdownContent = ''; // This will hold the rendered HTML from the markdown
	const mdParser = new MarkdownIt();

	onMount(async () => {
		// Dynamically import the markdown file based on the `md` prop
		const markdownFile = await import(`$docs/${md}.md?raw`);
		markdownContent = mdParser.render(markdownFile.default);
	});
</script>

<article class="markdown {extraClass}">
	{@html markdownContent}
</article>

<style lang="postcss">
	/* TODO: red color palette ffs */
	:global(.markdown) {
		@apply w-full max-w-screen-md mx-auto px-6 pt-12 pb-4;
		@apply bg-primary-50 border-primary-900 border;
		@apply rounded-lg;
		@apply shadow-lg shadow-black;
		@apply text-primary-500;
		@apply font-lato;
	}

	:global(.markdown h1) {
		@apply text-blood-800 text-3xl font-bold mt-2 mb-5;
	}

	:global(.markdown h2) {
		@apply text-blood-700 text-2xl font-bold mt-2 mb-4;
	}

	:global(.markdown h3) {
		@apply text-blood-600 text-xl font-bold mt-2 mb-3;
	}

	:global(.markdown h4) {
		@apply text-primary-600 text-lg mt-1 font-semibold;
	}

	:global(.markdown h5) {
		@apply text-primary-600 font-semibold;
	}

	:global(.markdown h6) {
		@apply text-primary-600 text-sm font-semibold;
	}

	:global(.markdown p) {
		@apply text-primary-700 text-sm mb-3;
		@apply leading-snug;
	}

	:global(.markdown a) {
		@apply text-red-800 underline hover:text-red-800;
	}

	:global(.markdown strong) {
		@apply font-bold;
	}

	:global(.markdown em) {
		@apply italic;
	}

	:global(.markdown blockquote) {
		@apply border-l-4 border-primary-300 pl-4 mb-3 italic;
	}

	:global(.markdown ul) {
		@apply list-disc list-inside mb-3;
	}

	:global(.markdown ol) {
		@apply list-decimal list-inside mb-3;
	}

	:global(.markdown li) {
		@apply ml-5 text-sm;
	}

	:global(.markdown code) {
		@apply bg-primary-100 rounded p-1 text-sm font-mono;
	}

	:global(.markdown pre) {
		@apply bg-primary-800 text-white p-3 rounded mb-3 overflow-x-auto;
	}

	:global(.markdown pre code) {
		@apply bg-transparent p-0;
	}

	:global(.markdown hr) {
		@apply mb-3 border-t border-primary-300;
	}

	:global(.markdown table) {
		@apply min-w-full divide-y divide-primary-300 mb-3;
	}

	:global(.markdown th) {
		@apply bg-primary-100 text-left font-semibold p-2;
	}

	:global(.markdown td) {
		@apply p-2 border-t border-primary-300;
	}

	:global(.markdown img) {
		@apply max-w-full h-auto mb-3;
	}
</style>
