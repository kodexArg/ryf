<script>
  import { fly } from 'svelte/transition'

  export let data;
  data = data.props.character;
</script>

{#if data}
<section
  in:fly={{y:600, delay:500, duration: 1000 }} 
  out:fly={{y:-200, duration: 500 }}
>

  <div class="left-pane">
      <img src='/characters/{data.portrait}' alt={data.portrait}/>
      <h1>
        {#if data.title}{data.title}<br>{/if}
        {data.firstName} {data.lastName}
      </h1>
      <h2>
        {data.mainOccupation}
        {#if data.secondaryOccupation }/{data.secondaryOccupation}{/if}
      </h2>
      <p>
        {data.age} años
      </p>
    </div>
    <div class="right-pane">
      <article class="bio">
        <h2>Bio</h2>
        {@html data.bio}
      </article>
      <article class="secret">
        <h2>Secret</h2>
        {@html data.secret}
      </article>
    </div>
    <button id="floating-button" class="floating-button" onclick="window.location.href='/characters'">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
  </svg>
    </button>
</section>
{:else}
<p>Loading...</p>
{/if}

<style lang="postcss">
  section {
    @apply select-none;
    @apply flex p-2;
  }

  .floating-button {
    @apply fixed bottom-12 right-8 w-10 h-10;
    @apply bg-primary-100 bg-opacity-95 rounded-full;
    @apply text-primary-900 font-sans text-lg leading-none font-bold;
    @apply px-2 py-1;
    @apply cursor-pointer;
    @apply z-50;
  }
  
  img {
    @apply w-[280px] aspect-[0.625] relative;
    @apply rounded-xl bg-cover object-cover;
    @apply flex overflow-hidden;
    @apply filter contrast-[120%];
    box-shadow:
      -17px -17px 0 -7px rgb(255, 255, 255, 0.25),
      17px 17px 0 -7px rgb(0, 0, 0, 0.25);
  }

  .left-pane {
    @apply min-w-fit m-3;

    & h1 {
      @apply ml-2 mt-5;
      @apply font-bahiana text-primary-50 text-4xl font-bold tracking-wider leading-none;
      -webkit-text-stroke: 0.1px black;
      text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
    }
  
    & h2 {
      @apply overline;
      @apply w-full text-primary-100 text-end mt-1;
      @apply font-overpass uppercase text-lg tracking-tighter leading-none;
    }

    & p {
      @apply text-primary-100 text-end leading-none tracking-tighter;
    }
  }

  .right-pane {
    @apply mx-3 mb-16;

    & h2 {
      @apply w-full rounded-t-lg pt-2 pb-1 pl-4;
      @apply text-primary-100 bg-primary-900;
      @apply font-overpass leading-none tracking-tighter uppercase text-lg;
    }

    & p {
      @apply font-overpass-mono border-none;
    }
  }

  .bio,
  .secret {
    @apply my-4 shadow-lg shadow-primary-900;
    @apply text-sm font-overpass-mono tracking-tighter text-primary-700;

    & p {
      @apply p-3 border-2 border-primary-900;
    }
  }
  
  .bio {
    @apply bg-primary-200 rounded-lg;
  }
  
  .secret {
    @apply bg-primary-400 rounded-lg;
  }

</style>
