<script lang="ts">
  import { ArrowRight } from 'lucide-svelte';
  import { analytics } from '../services/analyticsService';
  import { fade, fly, scale } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  function trackHireMe() {
    analytics.track({ type: 'click_hire_me', location: 'hero' });
  }
</script>

<section class="relative pt-32 pb-24 px-6 overflow-hidden transition-colors duration-300">
  <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full -z-10">
    <div 
      transition:scale={{ duration: 1500, opacity: 0, start: 0.8, easing: quintOut }}
      class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[600px] bg-indigo-500/10 blur-[120px] rounded-full"
    ></div>
  </div>

  <div class="max-w-7xl mx-auto text-center">
    <div 
      in:fly={{ y: 20, duration: 600, delay: 200, easing: quintOut }}
      class="inline-flex items-center gap-2 px-3 py-1 bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-bold tracking-widest uppercase rounded-full border border-indigo-500/20 mb-8"
    >
      <span class="relative flex h-2 w-2">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
      </span>
      Available for Projects
    </div>
    
    <h1 
      in:fly={{ y: 30, duration: 800, delay: 400, easing: quintOut }}
      class="text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter mb-8 leading-[0.9] text-neutral-900 dark:text-white"
    >
      ELITE FULL-STACK <br/>
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ARCHITECT.</span>
    </h1>
    
    <p 
      in:fly={{ y: 20, duration: 600, delay: 600, easing: quintOut }}
      class="text-lg md:text-xl text-neutral-600 dark:text-neutral-400 max-w-2xl mx-auto mb-12 leading-relaxed"
    >
      Building production-grade systems with Django, Svelte, and AI. 
      Optimized for performance, security, and conversion.
    </p>

    <div 
      in:fly={{ y: 20, duration: 600, delay: 800, easing: quintOut }}
      class="flex flex-col sm:flex-row items-center justify-center gap-4"
    >
      <a 
        href="#contact" 
        on:click={trackHireMe}
        class="w-full sm:w-auto px-8 py-4 bg-neutral-900 dark:bg-white text-white dark:text-black font-bold rounded-full hover:bg-neutral-800 dark:hover:bg-neutral-200 transition-all flex items-center justify-center gap-2 group"
      >
        Hire Me <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform" />
      </a>
      <a href="#work" class="w-full sm:w-auto px-8 py-4 bg-neutral-100 dark:bg-neutral-900 text-neutral-900 dark:text-white font-bold rounded-full border border-neutral-200 dark:border-neutral-800 hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-all">
        View Work
      </a>
    </div>
  </div>
</section>
