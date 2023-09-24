<script>
  import { page } from '$app/stores';
  let slug = $page.params.slug;
</script>

<section class="w-full h-full flex flex-col">
  <article class="w-32 h-32 rounded-lg bg-sky-300 border-2 border-bg-sky-400">
    Test: {slug}
  </article>
</section>