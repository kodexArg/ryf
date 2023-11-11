<script lang="ts">
	export let svg: string = '';

	let svgContent = '';

	$: if (svg) {
		import(`./svg/${svg}.svg?raw`).then(({ default: content }) => {
			if ($$props.class) {
				svgContent = content.replace('<svg ', `<svg class="${$$props.class}" `);
			} else {
				svgContent = content;
			}
		});
	}
</script>

{@html svgContent}
