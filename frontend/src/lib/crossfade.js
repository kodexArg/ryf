// crossfade.js
import { crossfade as svelteCrossfade } from 'svelte/transition';

const [send, receive] = svelteCrossfade({
  duration: 2000,
});

export { send, receive };
