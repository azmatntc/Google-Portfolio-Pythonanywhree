<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  export let id: string = '';
  export let className: string = '';
  export let delay: number = 0;
  export let y: number = 40;
  export let duration: number = 1000;

  let visible = false;
  let element: HTMLElement;

  onMount(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          visible = true;
          observer.unobserve(element);
        }
      },
      { threshold: 0.1 }
    );

    observer.observe(element);
    return () => observer.disconnect();
  });
</script>

<section {id} bind:this={element} class={className}>
  {#if visible}
    <div in:fly={{ y, duration, delay, opacity: 0, easing: quintOut }}>
      <slot />
    </div>
  {:else}
    <div class="opacity-0">
      <slot />
    </div>
  {/if}
</section>
