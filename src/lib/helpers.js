// $lib/helpers.js
import { goto } from '$app/navigation';
import { get } from 'svelte/store';
import { page } from '$app/stores';

export const goSomeWhereBack = () => {
    const $page = get(page); // get the current value of the page store
    const backPath = $page.url.pathname.substring(0, $page.url.pathname.lastIndexOf('/'));
    goto(backPath || '/');
};
