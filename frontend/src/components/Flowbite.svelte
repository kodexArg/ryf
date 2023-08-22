<script>
  import {Icon, icons} from 'flowbite-svelte-icons';
</script>


<!-- code to show all the icons-->
<div class="grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-8 px-4 dark:text-white">
  {#each Object.keys(icons) as name}
    <div class="flex gap-4 items-center text-lg">
      <Icon name={name} size="md" class="inline" />
      {name}
    </div>
  {/each}
</div>