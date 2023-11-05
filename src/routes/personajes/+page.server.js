// Make sure this file is named correctly: +page.server.js

export async function load({ fetch }) {
	try {
		const response = await fetch('http://localhost:8000/api/characters/');

		if (response.ok) {
			const characters = await response.json();
			return {
				props: { characters }
			};
		} else {
			// Handle server errors
			const error = new Error('Failed to fetch characters');
			error.status = response.status;
			throw error;
		}
	} catch (error) {
		// Handle network errors
		error.message = 'Failed to fetch characters';
		throw error;
	}
}
