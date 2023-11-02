<script>
  import { fly } from "svelte/transition";
  import { goto } from "$app/navigation";
  import SkillBar from "$lib/SkillBar.svelte";
  export let character;

  let clickTimeout;
  let card;
  let enlarged = false;
  let dblclick = false;
  let flyConfig = { x: 100, y: 500, duration: 400, opacity: 0.9 }; // Default fly config

  function handleCardClick() {
    if (enlarged) {
      clickTimeout = setTimeout(() => {
        if (!dblclick) {
          enlarged = false;
        }
      }, 500); // delay to check for double click
    }
  }

  async function handleCardDoubleClick() {
    if (clickTimeout) clearTimeout(clickTimeout);
    if (enlarged) {
      dblclick = true;
      goto(`/characters/${character.slug}`);
    } else {
      enlarged = true;
    }
  }
</script>

{#if enlarged}
  <div
    class="overlay"
    on:click={() => (enlarged = false)}
    on:keydown={(e) => e.key === "Enter" && (enlarged = false)}
    tabindex="-1"
    role="button"
  />
{/if}

<article class:enlarged class:reduced={!enlarged}>
  <card
    data-sveltekit-preload-data
    class="card"
    class:enlarged
    class:reduced={!enlarged}
    class:centered={enlarged}
    bind:this={card}
    on:dblclick={handleCardDoubleClick}
    on:click={handleCardClick}
    tabindex="-1"
    role="button"
    on:keydown={(e) => e.key === "Enter" && handleCardDoubleClick()}
    in:fly={flyConfig}
  >
    <div class="card-image">
      <img src="/characters/{character.portrait}" alt={character.portrait} />
      <div class="portrait-box">
        <div class="name">
          {#if character.title}{character.title}<br />{/if}
          {character.firstName}
          {character.lastName}
        </div>
        <div class="subtitle">
          <div class="occupation">
            {character.mainOccupation}{#if character.secondaryOccupation}/{character.secondaryOccupation}{/if}
          </div>
        </div>
      </div>
    </div>

    <div class="m-2">
      {#each Object.entries(character.stats) as [key, value]}
        <SkillBar stat={key} number={value} />
      {/each}
    </div>
  </card>
</article>

<style lang="postcss">
  /* TODO: anidation (future) */
  .card {
    @apply select-none;
    @apply relative flex flex-col w-[200px] mb-8;
    @apply bg-primary-900 rounded-xl;
    @apply outline outline-2 outline-primary-900;
    @apply cursor-pointer;
    box-shadow: 1rem 1rem 1rem rgb(0, 0, 0, 0.75), 0 0 2rem #000;
  }

  .enlarged {
    @apply z-50 scale-[115%] -translate-y-6 translate-x-16;
  }

  @media (min-width: 640px) {
    .enlarged {
      @apply scale-110 -translate-y-2;
    }
  }

  .enlarged .card {
    @apply bg-primary-100;
  }

  .reduced {
    @apply z-0 scale-100;
  }

  .overlay {
    @apply fixed -left-20 inset-0 bg-primary-900 opacity-50 z-30;
  }


  /* card picture */
  .card-image {
    @apply relative flex w-[200px] aspect-[0.625] overflow-hidden;
    @apply rounded-t-xl bg-cover;
    @apply filter contrast-[120%];
  }

  .card-image img {
    @apply absolute z-0;
    @apply w-full aspect-[0.625] object-cover;
  }

  /* text over image */
  .portrait-box {
    @apply absolute bottom-0 right-0 z-10;
  }

  .portrait-box .name {
    @apply font-bahiana text-primary-50 text-right text-2xl font-bold tracking-wider leading-none pr-3;
    -webkit-text-stroke: 0.1px black;
    text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000,
      -1px 1px 0 #000, 1px 1px 0 #000;
  }

  .portrait-box .subtitle {
    @apply pt-0.5 pl-2 pr-0.5 mb-1 mt-0.5 rounded-sm;
    @apply bg-black rounded-l-full bg-opacity-50;
    @apply font-overpass-mono text-xs tracking-tight leading-none text-primary-50;
  }

  article:not(:last-child) {
    @apply -ml-10;
  }

  article:last-child {
    @apply ml-4;
  }

  /* looks like a :has :not tutorial... let's comment this nightmare for the Gabriel of the future: */
  /* the items are rendering from back to front using flex-row-reverse in the Characters.svelte component, so last-child is actually the first element at left of the screen... and this is important! */

  /* HOVER! (focus!) */
  article:not(:last-child):not(.enlarged) .card:hover {
    @apply translate-x-12 duration-1000 delay-500;
  }

  /* first sibiling displacement */
  article:has(+ * + article:hover) {
    @apply translate-x-8 duration-1000 delay-500;
  }

  /* first sibiling is second element displacement (overwrite) */
  article:has(+ * + article:hover):has(+ * + article:last-child) {
    @apply translate-x-4 duration-1000 delay-500;
  }
</style>
