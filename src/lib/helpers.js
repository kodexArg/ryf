// $lib/helpers.js
import { goto } from '$app/navigation';
import { page } from '$app/stores';
import { get } from 'svelte/store';

export const goSomeWhereBack = () => {
    const $page = get(page); // get the current value of the page store
    const backPath = $page.url.pathname.substring(0, $page.url.pathname.lastIndexOf('/'));
    goto(backPath || '/');
};
