/** @type {import('tailwindcss').Config}*/

const config = {
	content: ['./src/**/*.{html,svg,js,svelte,ts}'],

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
				},
				blood: {
					50: '#faf3ed',
					100: '#f2e5da',
					200: '#e3c1ac',
					300: '#d19880',
					400: '#ad4836',
					500: '#8a0303',
					600: '#7d0202',
					700: '#660101',
					800: '#520101',
					900: '#3d0101',
					950: '#290000'
				}
			}
		}
	}
};

export default config;
