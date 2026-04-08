<script lang="ts">
  console.log('App.svelte script executing...');
  import Hero from './components/Hero.svelte';
  import About from './components/About.svelte';
  import ProjectCard from './components/ProjectCard.svelte';
  import ContactForm from './components/ContactForm.svelte';
  import AIChatWidget from './components/AIChatWidget.svelte';
  import ThemeToggle from './components/ThemeToggle.svelte';
  import { api, ApiError } from './lib/api';
  import { analytics } from './services/analyticsService';
  import { theme } from './lib/themeStore';
  import { onMount } from 'svelte';

  let projects = [];
  let loading = true;
  let error: string | null = null;

  onMount(async () => {
    // Initial theme setup
    if ($theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    
    console.log('App.svelte mounted, fetching projects...');
    try {
      projects = await api.get('/api/projects');
      console.log('Projects fetched:', projects);
    } catch (e) {
      console.error('Failed to fetch projects:', e);
      error = e instanceof ApiError ? e.message : 'Could not load projects. Please try again later.';
    } finally {
      loading = false;
    }
  });

  function trackHireMe() {
    analytics.track({ type: 'click_hire_me', location: 'nav' });
  }
</script>

<main class="min-h-screen bg-white dark:bg-neutral-950 text-neutral-900 dark:text-neutral-100 font-sans selection:bg-indigo-500/30 transition-colors duration-300">
  <nav class="fixed top-0 w-full z-50 bg-white/80 dark:bg-neutral-950/80 backdrop-blur-md border-b border-neutral-200 dark:border-neutral-800 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
      <div class="text-xl font-bold tracking-tighter text-neutral-900 dark:text-white">
        PORTFOLIO<span class="text-indigo-500">.AI</span>
      </div>
      <div class="flex items-center gap-4 md:gap-8 text-sm font-medium text-neutral-600 dark:text-neutral-400">
        <div class="hidden md:flex items-center gap-8">
          <a href="#work" class="hover:text-neutral-900 dark:hover:text-white transition-colors">Work</a>
          <a href="#about" class="hover:text-neutral-900 dark:hover:text-white transition-colors">About</a>
        </div>
        <ThemeToggle />
        <a href="#contact" on:click={trackHireMe} class="px-4 py-2 bg-indigo-600 text-white rounded-full hover:bg-indigo-500 transition-all">Hire Me</a>
      </div>
    </div>
  </nav>

  <Hero />

  <section id="work" class="py-24 px-6 max-w-7xl mx-auto">
    <div class="mb-16">
      <h2 class="text-3xl font-bold tracking-tight mb-4 text-neutral-900 dark:text-white">Selected Projects</h2>
      <p class="text-neutral-600 dark:text-neutral-400 max-w-2xl">A collection of production-grade systems built with modern stacks and AI integration.</p>
    </div>

    {#if loading}
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="h-64 bg-neutral-100 dark:bg-neutral-900 animate-pulse rounded-2xl"></div>
        <div class="h-64 bg-neutral-100 dark:bg-neutral-900 animate-pulse rounded-2xl"></div>
      </div>
    {:else if error}
      <div class="p-8 bg-red-500/10 border border-red-500/20 rounded-2xl text-center">
        <p class="text-red-400 font-medium">{error}</p>
        <button on:click={() => window.location.reload()} class="mt-4 text-sm font-bold text-neutral-900 dark:text-white underline underline-offset-4">Retry</button>
      </div>
    {:else}
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        {#each projects as project}
          <ProjectCard {project} />
        {/each}
      </div>
    {/if}
  </section>

  <About />

  <section id="contact" class="py-24 px-6 max-w-3xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold tracking-tight mb-4 text-neutral-900 dark:text-white">Let's build something elite.</h2>
      <p class="text-neutral-600 dark:text-neutral-400">Capture leads, automate follow-ups, and scale your vision.</p>
    </div>
    <ContactForm />
  </section>

  <footer class="py-12 border-t border-neutral-200 dark:border-neutral-800 text-center text-neutral-500 text-sm">
    <p>&copy; 2026 Elite AI Portfolio Architect. Built with Django & Svelte.</p>
  </footer>

  <AIChatWidget />
</main>
