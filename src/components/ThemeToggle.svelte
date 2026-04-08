<script lang="ts">
  import { Sun, Moon } from 'lucide-svelte';
  import { theme } from '../lib/themeStore';

  function toggleTheme() {
    theme.update(t => t === 'dark' ? 'light' : 'dark');
  }
</script>

<button 
  on:click={toggleTheme}
  class="p-2 rounded-full bg-neutral-100 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-100 hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-all border border-neutral-200 dark:border-neutral-700"
  aria-label="Toggle Theme"
>
  {#if $theme === 'dark'}
    <Sun class="w-5 h-5" />
  {:else}
    <Moon class="w-5 h-5" />
  {/if}
</button>
