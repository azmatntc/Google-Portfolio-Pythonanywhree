<script lang="ts">
  console.log('App.svelte script executing...');
  import Hero from './components/Hero.svelte';
  import About from './components/About.svelte';
  import Header from './components/Header.svelte';
  import ProjectCard from './components/ProjectCard.svelte';
  import ContactForm from './components/ContactForm.svelte';
  import AIChatWidget from './components/AIChatWidget.svelte';
  import VisibleSection from './components/VisibleSection.svelte';
  import { api, ApiError } from './lib/api';
  import { analytics } from './services/analyticsService';
  import { theme } from './lib/themeStore';
  import { onMount } from 'svelte';
  import { fly, fade } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  let projects = [];
  let loading = true;
  let error: string | null = null;
  let selectedTech: string = 'All';
  let scrollY = 0;
  let innerHeight = 0;
  let containerHeight = 0;

  $: scrollProgress = (scrollY / (containerHeight - innerHeight)) * 100;

  $: filteredProjects = selectedTech === 'All' 
    ? projects 
    : projects.filter(p => p.tech_stack.includes(selectedTech));

  $: allTechs = ['All', ...new Set(projects.flatMap(p => p.tech_stack))];

  onMount(async () => {
    // Initial theme setup
    if ($theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    
    console.log('App.svelte mounted, fetching projects...');
    
    // Safety timeout to ensure loading state is cleared
    const safetyTimeout = setTimeout(() => {
      if (loading) {
        console.warn('App.svelte: Fetching projects taking too long, forcing loading to false');
        loading = false;
      }
    }, 5000);

    try {
      const data = await api.get('/api/projects');
      console.log('Projects fetched successfully:', data);
      projects = data || [];
    } catch (e) {
      console.error('Failed to fetch projects:', e);
      error = e instanceof ApiError ? e.message : 'Could not load projects. Please try again later.';
      // Fallback data if API fails completely
      projects = [
        {
          id: 1,
          title: "AI Portfolio Architect",
          description: "A full-stack portfolio generator with Django and Svelte.",
          tech_stack: ["Django", "Svelte", "MySQL", "Gemini"],
          github_link: "https://github.com/example/portfolio",
          live_demo: "#",
          tags: ["Full-Stack", "AI", "Automation"]
        }
      ];
    } finally {
      clearTimeout(safetyTimeout);
      loading = false;
    }
  });
</script>

<svelte:window bind:scrollY bind:innerHeight />

<main 
  bind:offsetHeight={containerHeight}
  class="min-h-screen bg-white dark:bg-neutral-950 text-neutral-900 dark:text-neutral-100 font-sans selection:bg-indigo-500/30 transition-colors duration-300"
>
  <!-- Scroll Progress Bar -->
  <div class="fixed top-0 left-0 w-full h-[2px] z-[100] pointer-events-none">
    <div 
      class="h-full bg-indigo-600 transition-all duration-150 ease-out"
      style="width: {scrollProgress}%"
    ></div>
  </div>

  <Header {scrollY} />

  <Hero />

  <VisibleSection id="work" className="py-24 px-6 max-w-7xl mx-auto">
    <div class="mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8">
      <div>
        <h2 class="text-3xl font-bold tracking-tight mb-4 text-neutral-900 dark:text-white">Selected Projects</h2>
        <p class="text-neutral-600 dark:text-neutral-400 max-w-2xl">A collection of production-grade systems built with modern stacks and AI integration.</p>
      </div>
      
      <div class="flex flex-wrap gap-2">
        {#each allTechs as tech}
          <button 
            on:click={() => selectedTech = tech}
            class="px-4 py-1.5 text-xs font-bold rounded-full border transition-all duration-300 {selectedTech === tech ? 'bg-indigo-600 border-indigo-600 text-white shadow-lg shadow-indigo-500/20' : 'bg-transparent border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:border-indigo-500/50'}"
          >
            {tech}
          </button>
        {/each}
      </div>
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
        {#each filteredProjects as project, i (project.id)}
          <ProjectCard {project} index={i} />
        {/each}
      </div>
    {/if}
  </VisibleSection>

  <About />

  <VisibleSection id="contact" className="py-32 px-6 relative overflow-hidden">
    <!-- Background Decoration -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-indigo-500/5 dark:bg-indigo-500/10 rounded-full blur-[120px] -z-10"></div>
    
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-16 space-y-6">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-indigo-50 dark:bg-indigo-500/10 border border-indigo-100 dark:border-indigo-500/20 rounded-full">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
          </span>
          <span class="text-[10px] font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-widest">Available for new projects</span>
        </div>
        
        <h2 class="text-4xl md:text-5xl font-black tracking-tight text-neutral-900 dark:text-white uppercase italic">
          Let's build something <span class="text-indigo-600 dark:text-indigo-400">elite</span>.
        </h2>
        
        <p class="text-neutral-600 dark:text-neutral-400 max-w-xl mx-auto text-lg font-light leading-relaxed">
          Ready to transform your vision into a high-performance digital reality? 
          Drop a message below and let's discuss your next breakthrough.
        </p>
      </div>
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-7">
          <ContactForm />
        </div>
        
        <div class="lg:col-span-5 space-y-8">
          <div class="p-8 bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded-3xl space-y-6 shadow-xl shadow-neutral-500/5">
            <h3 class="text-sm font-black uppercase tracking-[0.3em] text-neutral-400">Direct Contact</h3>
            <div class="space-y-4">
              <a href="mailto:azmatntc@gmail.com" class="flex items-center gap-4 group">
                <div class="w-10 h-10 bg-neutral-50 dark:bg-neutral-800 rounded-xl flex items-center justify-center border border-neutral-100 dark:border-neutral-700 group-hover:bg-indigo-600 group-hover:border-indigo-600 transition-all">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-neutral-500 group-hover:text-white transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                </div>
                <div>
                  <div class="text-[10px] font-bold text-neutral-400 uppercase tracking-widest">Email</div>
                  <div class="text-neutral-900 dark:text-white font-medium">azmatntc@gmail.com</div>
                </div>
              </a>
              <div class="flex items-center gap-4 group">
                <div class="w-10 h-10 bg-neutral-50 dark:bg-neutral-800 rounded-xl flex items-center justify-center border border-neutral-100 dark:border-neutral-700">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-neutral-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div>
                  <div class="text-[10px] font-bold text-neutral-400 uppercase tracking-widest">Location</div>
                  <div class="text-neutral-900 dark:text-white font-medium">Remote / Global</div>
                </div>
              </div>
            </div>
          </div>

          <div class="p-8 bg-indigo-600 rounded-3xl text-white space-y-4 shadow-2xl shadow-indigo-500/20">
            <h3 class="text-lg font-bold italic uppercase tracking-tight">Standard Response Time</h3>
            <p class="text-indigo-100 text-sm font-light leading-relaxed">
              I typically respond to all inquiries within <span class="font-bold text-white">4-6 business hours</span>. 
              For urgent technical consulting, please specify "URGENT" in the subject line.
            </p>
          </div>
        </div>
      </div>
    </div>
  </VisibleSection>

  <footer class="py-12 border-t border-neutral-200 dark:border-neutral-800 text-center text-neutral-500 text-sm">
    <p>&copy; 2026 Elite AI Portfolio Architect. Built with Django & Svelte.</p>
  </footer>

  <AIChatWidget />
</main>
