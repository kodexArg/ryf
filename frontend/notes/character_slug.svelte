<script>
  import { fly } from "svelte/transition";
  import { expoOut } from 'svelte/easing';

  
  export let data;

  data = data.props.character;
  console.log(data);
</script>

<section in:fly={{ y: 600, delay: 500, duration: 1000, easing: expoOut }}>
  <div class="container">
    <div class="pane title-pane">
      <h1>
        {#if data.title}
          {data.title}
        {/if}
      </h1>
      <h1>
        {data.firstName}
        {data.lastName}
      </h1>
    </div>
    <div class="pane left-pane">
      <img
        src="/characters/{data.portrait}"
        alt={data.portrait}
      />
      <h2>
        {data.mainOccupation}
        {#if data.secondaryOccupation}/{data.secondaryOccupation}{/if} ({data.age})
      </h2>
    </div>
    <div class="pane right-pane">
      <details class="bio">
        <h2>Bio</h2>
        <div>{@html data.bio}</div>
      </details>
      <details class="secret">
        <h2>Secreto</h2>
        <div>{@html data.secret}</div>
      </details>
    </div>
  </div>
</section>

<style lang="postcss">
  section {
    @apply select-none;
    @apply bg-gradient-to-b from-transparent via-transparent to-primary-900;
    @apply flex px-4 py-2;
  }

  .container {
    @apply px-4 py-2;
    @apply grid;
  }

  .title-pane {
    @apply w-full;
    @apply flex space-x-3;
    @apply sm:flex-row sm:space-x-3;
    @apply font-bahiana text-white text-[3.2rem] font-bold tracking-wider leading-none;
    -webkit-text-stroke: 0.1px black;
    text-shadow: 4px 4px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000,
      -2px 2px 0 #000, 2px 2px 0 #000;
  }

  img {
    @apply w-[280px] aspect-[0.625] ;
    @apply rounded-xl bg-cover object-cover;
    @apply flex overflow-hidden;
    @apply filter contrast-[120%];
    box-shadow: -17px -17px 0 -7px rgb(255, 255, 255, 0.25),
      17px 17px 0 -7px rgb(0, 0, 0, 0.25);

  }

  .left-pane {
    @apply max-w-sm mb-10;
    @apply flex-shrink-0;
  }

  .left-pane h2 {
    @apply overline pt-5;
    @apply w-full text-primary-100 text-end mt-1;
    @apply font-overpass uppercase text-lg leading-none;
  }

  .right-pane {
    @apply sm:pl-6;
    @apply flex flex-col;
  }

  .right-pane h2 {
    @apply w-full rounded-t-lg pt-3 pb-1 pl-2;
    @apply text-primary-200 bg-primary-900;
    @apply font-overpass leading-none tracking-wider uppercase text-xl;
  }

  .bio,
  article {
    @apply w-72 md:w-full flex-shrink;
  }

  .secret,
  article {
    @apply w-72 md:w-full flex-shrink;
  }

  .bio div,
  .secret div {
    @apply mb-5 px-3 py-2;
    @apply border-2 border-primary-900;
    @apply font-overpass-mono leading-tight tracking-tighter text-sm;
    box-shadow: 17px 17px 0 -7px rgb(0, 0, 0, 0.25);
  }

  .bio div {
    @apply text-primary-900 bg-primary-200 bg-opacity-75;
  }

  .secret div {
    @apply text-primary-200 bg-primary-500 bg-opacity-75;
  }
</style>
