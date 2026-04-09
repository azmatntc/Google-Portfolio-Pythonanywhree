<script lang="ts">
  import { Menu, X, ArrowRight } from 'lucide-svelte';
  import { analytics } from '../services/analyticsService';
  import ThemeToggle from './ThemeToggle.svelte';
  import { fade, fly, slide } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import { onMount } from 'svelte';

  export let scrollY: number = 0;

  let isMenuOpen = false;
  let mounted = false;

  onMount(() => {
    mounted = true;
  });

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
    if (isMenuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  }

  function closeMenu() {
    isMenuOpen = false;
    document.body.style.overflow = 'auto';
  }

  function trackHireMe() {
    analytics.track({ type: 'click_hire_me', location: 'nav' });
    closeMenu();
  }

  const navLinks = [
    { name: 'Work', href: '#work' },
    { name: 'About', href: '#about' },
    { name: 'Contact', href: '#contact' }
  ];

  $: isScrolled = scrollY > 50;
</script>

<header 
  class="fixed top-0 w-full z-[60] transition-all duration-500 {isScrolled ? 'py-3' : 'py-6'}"
>
  <div class="max-w-7xl mx-auto px-6">
    <div 
      class="relative flex items-center justify-between px-6 h-16 rounded-full transition-all duration-500 {isScrolled ? 'bg-white/80 dark:bg-neutral-950/80 backdrop-blur-xl border border-neutral-200 dark:border-neutral-800 shadow-2xl shadow-neutral-500/10' : 'bg-transparent border-transparent'}"
    >
      <!-- Logo -->
      <a 
        href="/" 
        class="text-xl font-black tracking-tighter text-neutral-900 dark:text-white flex items-center gap-1 group"
      >
        <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center text-white text-xs rotate-3 group-hover:rotate-12 transition-transform">P</div>
        PORTFOLIO<span class="text-indigo-600">.AI</span>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden md:flex items-center gap-8">
        {#each navLinks as link}
          <a 
            href={link.href} 
            class="text-sm font-bold text-neutral-500 hover:text-neutral-900 dark:text-neutral-400 dark:hover:text-white transition-colors relative group"
          >
            {link.name}
            <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-indigo-600 transition-all group-hover:w-full"></span>
          </a>
        {/each}
      </nav>

      <!-- Actions -->
      <div class="flex items-center gap-3">
        <div class="hidden md:block">
          <ThemeToggle />
        </div>
        
        <a 
          href="#contact" 
          on:click={trackHireMe} 
          class="hidden md:flex px-6 py-2.5 bg-neutral-900 dark:bg-white text-white dark:text-black text-xs font-black uppercase tracking-widest rounded-full hover:bg-indigo-600 dark:hover:bg-indigo-500 dark:hover:text-white transition-all items-center gap-2"
        >
          Hire Me <ArrowRight class="w-3 h-3" />
        </a>

        <!-- Mobile Menu Toggle -->
        <button 
          on:click={toggleMenu}
          class="md:hidden w-10 h-10 flex items-center justify-center rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-900 dark:text-white"
          aria-label="Toggle Menu"
        >
          {#if isMenuOpen}
            <X class="w-5 h-5" />
          {:else}
            <Menu class="w-5 h-5" />
          {/if}
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu Overlay -->
  {#if isMenuOpen}
    <div 
      transition:fade={{ duration: 300 }}
      class="fixed inset-0 z-[-1] bg-white dark:bg-neutral-950 md:hidden"
    >
      <div class="flex flex-col h-full pt-32 px-8">
        <nav class="flex flex-col gap-8">
          {#each navLinks as link, i}
            <a 
              href={link.href} 
              on:click={closeMenu}
              in:fly={{ x: -20, duration: 500, delay: 100 * i, easing: quintOut }}
              class="text-5xl font-black tracking-tighter text-neutral-900 dark:text-white uppercase italic hover:text-indigo-600 transition-colors"
            >
              {link.name}
            </a>
          {/each}
        </nav>

        <div 
          in:fly={{ y: 20, duration: 500, delay: 400 }}
          class="mt-auto pb-12 space-y-8"
        >
          <div class="flex items-center justify-between p-6 bg-neutral-100 dark:bg-neutral-900 rounded-3xl">
            <span class="font-bold text-neutral-500">Appearance</span>
            <ThemeToggle />
          </div>
          
          <a 
            href="#contact" 
            on:click={trackHireMe}
            class="flex w-full py-6 bg-indigo-600 text-white font-black uppercase tracking-[0.2em] text-sm rounded-2xl items-center justify-center gap-3 shadow-2xl shadow-indigo-500/20"
          >
            Start a Project <ArrowRight class="w-4 h-4" />
          </a>
        </div>
      </div>
    </div>
  {/if}
</header>
