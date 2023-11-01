/** @type {import('tailwindcss').Config}*/

const config = {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
	],

	darkMode: 'class',

	theme: {
		extend: {
			fontFamily: {
				bahiana: ['Bahiana', 'sans-serif'],
				overpass: ['Overpass', 'sans-serif'],
				'overpass-mono': ['Overpass Mono', 'monospace'],
				lato: ['Lato', 'sans-serif']
			},
			colors: {
				// SyV: palette from https://tailcolor.com/palettes/6e7458
				primary: {
					50: '#f1f1ee',
					100: '#e2e3de',
					200: '#c5c7bc',
					300: '#a8ac9b',
					400: '#8b9079',
					500: '#6e7458',
					600: '#585d46',
					700: '#424635',
					800: '#2c2e23',
					900: '#161712'
				}
			}
		}
	}
};

export default config;
