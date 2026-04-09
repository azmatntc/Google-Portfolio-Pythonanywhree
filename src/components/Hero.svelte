<script lang="ts">
  import { ArrowRight, MousePointer2 } from 'lucide-svelte';
  import { analytics } from '../services/analyticsService';
  import { fade, fly, scale } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import { onMount } from 'svelte';

  let scrollY = 0;
  let mounted = false;

  onMount(() => {
    mounted = true;
  });

  function trackHireMe() {
    analytics.track({ type: 'click_hire_me', location: 'hero' });
  }
</script>

<svelte:window bind:scrollY />

<section class="relative min-h-screen flex items-center justify-center pt-20 pb-24 px-6 overflow-hidden transition-colors duration-300">
  <!-- Dynamic Background Elements -->
  <div class="absolute inset-0 -z-10 pointer-events-none">
    <div 
      class="absolute top-1/4 left-1/4 w-[600px] h-[600px] bg-indigo-500/10 blur-[120px] rounded-full transition-transform duration-700 ease-out"
      style="transform: translate({scrollY * 0.1}px, {scrollY * 0.05}px)"
    ></div>
    <div 
      class="absolute bottom-1/4 right-1/4 w-[500px] h-[500px] bg-purple-500/10 blur-[120px] rounded-full transition-transform duration-700 ease-out"
      style="transform: translate({-scrollY * 0.15}px, {-scrollY * 0.08}px)"
    ></div>
    
    <!-- Grid Pattern -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:40px_40px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_50%,#000_70%,transparent_100%)]"></div>
  </div>

  <div class="max-w-7xl mx-auto text-center relative z-10">
    {#if mounted}
      <div 
        in:fly={{ y: 20, duration: 800, delay: 200, easing: quintOut }}
        class="inline-flex items-center gap-2 px-4 py-1.5 bg-white/10 dark:bg-neutral-900/50 backdrop-blur-xl text-indigo-600 dark:text-indigo-400 text-[10px] font-black tracking-[0.2em] uppercase rounded-full border border-indigo-500/20 mb-12 shadow-2xl shadow-indigo-500/10"
      >
        <span class="relative flex h-2 w-2">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
        </span>
        Available for Elite Projects
      </div>
      
      <h1 
        class="text-6xl md:text-8xl lg:text-9xl font-black tracking-tighter mb-10 leading-[0.85] text-neutral-900 dark:text-white"
      >
        <div class="overflow-hidden">
          <span in:fly={{ y: 100, duration: 1000, delay: 400, easing: quintOut }} class="block">ELITE FULL-STACK</span>
        </div>
        <div class="overflow-hidden">
          <span in:fly={{ y: 100, duration: 1000, delay: 600, easing: quintOut }} class="block text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 via-purple-600 to-indigo-600 dark:from-indigo-400 dark:via-purple-400 dark:to-indigo-400 bg-[length:200%_auto] animate-gradient">ARCHITECT.</span>
        </div>
      </h1>
      
      <p 
        in:fly={{ y: 20, duration: 800, delay: 800, easing: quintOut }}
        class="text-lg md:text-2xl text-neutral-600 dark:text-neutral-400 max-w-3xl mx-auto mb-16 leading-relaxed font-light"
      >
        Engineering high-performance digital ecosystems with <span class="text-neutral-900 dark:text-white font-medium">Django</span>, 
        <span class="text-neutral-900 dark:text-white font-medium">Svelte</span>, and <span class="text-neutral-900 dark:text-white font-medium">Generative AI</span>. 
        Where precision meets innovation.
      </p>

      <div 
        in:fly={{ y: 20, duration: 800, delay: 1000, easing: quintOut }}
        class="flex flex-col sm:flex-row items-center justify-center gap-6"
      >
        <a 
          href="#contact" 
          on:click={trackHireMe}
          class="w-full sm:w-auto px-10 py-5 bg-indigo-600 text-white font-black uppercase tracking-widest text-xs rounded-full hover:bg-indigo-500 hover:scale-105 active:scale-95 transition-all flex items-center justify-center gap-3 group shadow-xl shadow-indigo-500/25"
        >
          Start a Project <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform" />
        </a>
        <a 
          href="#work" 
          class="w-full sm:w-auto px-10 py-5 bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white font-black uppercase tracking-widest text-xs rounded-full border border-neutral-200 dark:border-neutral-800 hover:border-indigo-500/50 hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-all"
        >
          View Archive
        </a>
      </div>
    {/if}
  </div>

  <!-- Scroll Indicator -->
  <div 
    class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-4 opacity-50 hover:opacity-100 transition-opacity duration-500"
    style="transform: translate(-50%, {scrollY * 0.2}px)"
  >
    <span class="text-[10px] font-black uppercase tracking-[0.4em] text-neutral-400">Scroll</span>
    <div class="w-[1px] h-12 bg-gradient-to-b from-indigo-500 to-transparent relative overflow-hidden">
      <div class="absolute top-0 left-0 w-full h-1/2 bg-white animate-scroll-line"></div>
    </div>
  </div>
</section>

<style>
  @keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  .animate-gradient {
    animation: gradient 6s ease infinite;
  }

  @keyframes scroll-line {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(200%); }
  }

  .animate-scroll-line {
    animation: scroll-line 2s cubic-bezier(0.76, 0, 0.24, 1) infinite;
  }
</style>
