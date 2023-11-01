import adapter from '@sveltejs/adapter-auto';
import path from 'path';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter(),
		alias: {
			'@comp': path.resolve('./src/components')
		}
	},
	preprocess: vitePreprocess({
		postcss: true,
		defaults: {
			style: 'postcss'
		}
	}),

};

export default config;

