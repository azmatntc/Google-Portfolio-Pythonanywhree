<script lang="ts">
  import { GitBranch, ExternalLink, Eye } from 'lucide-svelte';
  import { fly } from 'svelte/transition';
  import { onMount } from 'svelte';
  import { analytics } from '../services/analyticsService';
  import ProjectModal from './ProjectModal.svelte';

  export let project;

  let visible = false;
  let element: HTMLElement;
  let isModalOpen = false;

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

  function trackLink(linkType: 'github' | 'live' | 'case_study') {
    analytics.track({
      type: 'click_project_link',
      projectTitle: project.title,
      linkType
    });
  }

  function toggleModal() {
    isModalOpen = !isModalOpen;
    if (isModalOpen) {
      document.body.classList.add('modal-open');
    } else {
      document.body.classList.remove('modal-open');
    }
  }
</script>

<div 
  bind:this={element}
  class="group relative bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded-3xl overflow-hidden hover:border-indigo-500/50 transition-all duration-500 hover:-translate-y-2 hover:scale-[1.02] hover:shadow-2xl hover:shadow-indigo-500/10"
>
  {#if visible}
    <div in:fly={{ y: 40, duration: 800, delay: 100 }} class="h-full flex flex-col">
      <div class="aspect-video bg-neutral-200 dark:bg-neutral-800 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 dark:from-neutral-950 to-transparent opacity-60"></div>
        <div class="absolute bottom-6 left-6 right-6">
          <div class="flex flex-wrap gap-2 mb-3">
            {#each project.tech_stack as tech}
              <span class="px-2 py-0.5 bg-white/10 backdrop-blur-md text-[10px] font-bold text-white uppercase tracking-wider rounded-md border border-white/10">{tech}</span>
            {/each}
          </div>
          <h3 class="text-xl font-bold text-white">{project.title}</h3>
        </div>

        <!-- Hover Overlay -->
        <div class="absolute inset-0 bg-indigo-600/20 backdrop-blur-sm opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
          <button 
            on:click={toggleModal}
            class="px-6 py-3 bg-white text-neutral-900 font-bold rounded-full flex items-center gap-2 transform translate-y-4 group-hover:translate-y-0 transition-all duration-300 shadow-xl"
          >
            <Eye class="w-4 h-4" /> View Details
          </button>
        </div>
      </div>
      
      <div class="p-6 flex-1 flex flex-col">
        <p class="text-neutral-600 dark:text-neutral-400 text-sm mb-6 line-clamp-2">{project.description}</p>
        
        <div class="mt-auto flex items-center justify-between">
          <div class="flex gap-4">
            <a 
              href={project.github_link} 
              on:click={() => trackLink('github')}
              class="text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors"
            >
              <GitBranch class="w-5 h-5" />
            </a>
            <a 
              href={project.live_demo} 
              on:click={() => trackLink('live')}
              class="text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors"
            >
              <ExternalLink class="w-5 h-5" />
            </a>
          </div>
          <button 
            on:click={() => {
              trackLink('case_study');
              toggleModal();
            }}
            class="text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300 transition-colors uppercase tracking-widest"
          >
            Case Study
          </button>
        </div>
      </div>
    </div>
  {:else}
    <div class="aspect-video bg-neutral-100 dark:bg-neutral-900/50"></div>
    <div class="p-6 space-y-4">
      <div class="h-4 bg-neutral-200 dark:bg-neutral-800 rounded w-3/4"></div>
      <div class="h-4 bg-neutral-200 dark:bg-neutral-800 rounded w-1/2"></div>
    </div>
  {/if}
</div>

<ProjectModal 
  {project} 
  isOpen={isModalOpen} 
  onClose={toggleModal} 
/>
