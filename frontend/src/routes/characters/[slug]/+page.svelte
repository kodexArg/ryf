<script>
  import { fly } from "svelte/transition";
  import { expoOut } from "svelte/easing";
  import SkillBar from "$lib/SkillBar.svelte";

  export let data;
  data = data.props.character;
  
</script>

<main in:fly={{ y: 600, delay: 500, duration: 1000, easing: expoOut }}>

  <section>
    <img src="/characters/{data.portrait}" alt={data.portrait} />
  </section>
  
  <section>
    <div class="character-name">
      <div>
        {#if data.title}{data.title}{/if}
      </div>
      <div>
        {data.firstName}
        {data.lastName}
      </div>
    </div>
    <div class="character-ocupation">
      {data.mainOccupation}{#if data.secondaryOccupation}/{data.secondaryOccupation}{/if}
      ({data.age})
    </div>
  </section>

  <section>
    <div class="character-skills">
      {#each Object.entries(data.stats) as [key, value]}
        <SkillBar stat={key} number={value} />
      {/each}
    </div>
  </section>

  <section>
    <details>
      <summary>BIOGRAFÍA</summary>
      <div class="typewriter-text">{@html data.bio}</div>
    </details>
  </section>

  <section>
    <details>
      <summary>SECRETO</summary>
      <div class="typewriter-text">{@html data.secret}</div>
    </details>
  </section>

</main>

<style lang="postcss">

  main {
    @apply w-min p-3 sm:p-6;
    @apply flex flex-col sm:flex-wrap gap-4;
    @apply items-start justify-start;
  }

  section {
    @apply w-[320px];
  }

  .character-name {
    @apply font-bahiana text-white text-4xl font-bold tracking-wider leading-none;
    -webkit-text-stroke: 0.1px black;
    text-shadow: 4px 4px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000,
      -2px 2px 0 #000, 2px 2px 0 #000;
  }

  .character-ocupation {
    @apply font-overpass-mono text-lg text-primary-100 ml-4;
    @apply overline;
  }

  .character-skills {
    @apply bg-primary-100 rounded-xl border-2 border-primary-900 p-2;
    @apply shadow-lg shadow-primary-900;
  }

  img {
    @apply w-[320px] aspect-[0.625] -z-10;
    @apply rounded-xl bg-cover object-cover;
    @apply flex overflow-hidden;
    @apply filter contrast-[120%];
    box-shadow: -17px -17px 0 -7px rgb(255, 255, 255, 0.25),
      17px 17px 0 -7px rgb(0, 0, 0, 0.25);
  }

  /* TODO: Accordion animation */
  summary {
    @apply p-2 rounded-lg bg-primary-900;
    @apply font-overpass-mono font-bold tracking-tighter text-primary-300;
    @apply shadow-lg shadow-primary-900;
  }

  /* TODO: typewriter effect? */
  .typewriter-text {
    @apply max-h-[300px] -mt-2 py-2 px-3 bg-primary-300 overflow-x-hidden overflow-y-auto rounded-b-lg;
    @apply font-overpass-mono text-sm text-primary-800; 
    @apply shadow-lg shadow-primary-900;
  }
</style>
