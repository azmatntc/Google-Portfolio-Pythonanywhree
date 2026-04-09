<script lang="ts">
  import { Sun, Moon } from 'lucide-svelte';
  import { theme } from '../lib/themeStore';
  import { scale } from 'svelte/transition';

  function toggleTheme() {
    theme.update(t => t === 'dark' ? 'light' : 'dark');
  }
</script>

<button 
  on:click={toggleTheme}
  class="w-10 h-10 flex items-center justify-center rounded-full bg-neutral-100 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-100 hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-all border border-neutral-200 dark:border-neutral-700 relative overflow-hidden"
  aria-label="Toggle Theme"
>
  {#if $theme === 'dark'}
    <div in:scale={{ duration: 300, start: 0.5 }} out:scale={{ duration: 300, start: 0.5 }} class="absolute">
      <Sun class="w-5 h-5" />
    </div>
  {:else}
    <div in:scale={{ duration: 300, start: 0.5 }} out:scale={{ duration: 300, start: 0.5 }} class="absolute">
      <Moon class="w-5 h-5" />
    </div>
  {/if}
</button>
