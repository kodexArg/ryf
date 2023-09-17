<script>
  export let number = 0;
  export let stat;
  export let classString = "h-5 w-12";
  
  // Spanish titles
  const statTitles = {
    physique: "Físico",
    empathy: "Empatía",
    intellect: "Intelecto",
    ability: "Habilidad"
  };
</script>

<div class="text-primary-500 uppercase font-overpass-mono text-xs font-bold flex justify-between items-center">
  <h3>{statTitles[stat]}</h3>
  <svg class={classString} viewBox="0 0 40 10">
    {#each Array(number).fill(null) as _, i}
    <rect x={40 - (number - i) * 8} y="0" width="6" height="7" fill={i===0 ? '#8b9079' : i===1 ? '#6e7458' : i===2
      ? '#585d46' : i===3 ? '#424635' : '#2c2e23' } />
    {/each}
  </svg>
</div>
