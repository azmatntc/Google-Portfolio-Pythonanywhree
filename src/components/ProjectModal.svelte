<script lang="ts">
  import { X, ExternalLink, Github, Code2, Globe, Cpu, Database, Layers, CheckCircle2 } from 'lucide-svelte';
  import { fade, fly, scale } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  export let project;
  export let isOpen = false;
  export let onClose: () => void;

  const techIcons: Record<string, any> = {
    'Django': Layers,
    'Svelte': Code2,
    'MySQL': Database,
    'Gemini': Cpu,
    'Python': Code2,
    'Terraform': Globe,
    'AWS': Globe,
    'React': Code2,
    'Node.js': Layers,
    'PostgreSQL': Database,
  };

  const features = [
    'Real-time Data Sync',
    'AI-Powered Insights',
    'Secure OAuth2 Auth',
    'Responsive Dashboard',
    'Automated CI/CD',
    'Cloud-Native Scaling'
  ];

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') onClose();
  }
</script>

<svelte:window on:keydown={handleKeydown} />

{#if isOpen}
  <div 
    class="fixed inset-0 z-[200] flex items-center justify-center p-4 md:p-8 overflow-hidden"
    transition:fade={{ duration: 300 }}
  >
    <!-- Backdrop -->
    <div 
      class="absolute inset-0 bg-neutral-950/90 backdrop-blur-md"
      on:click={onClose}
    ></div>

    <!-- Modal Content -->
    <div 
      class="relative w-full max-w-6xl max-h-[90vh] bg-white dark:bg-neutral-900 rounded-[2.5rem] shadow-2xl overflow-hidden flex flex-col border border-neutral-200 dark:border-neutral-800"
      transition:fly={{ y: 100, duration: 600, easing: quintOut }}
    >
      <!-- Header -->
      <div class="px-8 py-6 border-b border-neutral-100 dark:border-neutral-800 flex items-center justify-between bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl sticky top-0 z-20">
        <div class="flex items-center gap-4">
          <div class="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/20">
            <Code2 class="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 class="text-2xl font-black tracking-tight text-neutral-900 dark:text-white uppercase italic">{project.title}</h2>
            <p class="text-[10px] font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-[0.2em]">Case Study / Detailed View</p>
          </div>
        </div>
        <button 
          on:click={onClose}
          class="p-3 rounded-full hover:bg-neutral-100 dark:hover:bg-neutral-800 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-all hover:rotate-90 duration-300"
        >
          <X class="w-6 h-6" />
        </button>
      </div>

      <!-- Body -->
      <div class="flex-1 overflow-y-auto p-8 md:p-12 space-y-20 scroll-smooth">
        
        <!-- Hero Section -->
        <section class="space-y-8">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-8">
              <div class="relative aspect-video rounded-[2rem] overflow-hidden group shadow-2xl">
                <img 
                  src={`https://picsum.photos/seed/${project.id}-hero/1200/800`} 
                  alt="Main Screenshot" 
                  class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110"
                  referrerPolicy="no-referrer"
                />
                <div class="absolute inset-0 bg-gradient-to-t from-neutral-900/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
              </div>
            </div>
            <div class="lg:col-span-4 grid grid-cols-1 gap-8">
              <div class="aspect-square rounded-[2rem] overflow-hidden shadow-xl">
                <img 
                  src={`https://picsum.photos/seed/${project.id}-side1/600/600`} 
                  alt="Detail 1" 
                  class="w-full h-full object-cover"
                  referrerPolicy="no-referrer"
                />
              </div>
              <div class="aspect-square rounded-[2rem] overflow-hidden shadow-xl">
                <img 
                  src={`https://picsum.photos/seed/${project.id}-side2/600/600`} 
                  alt="Detail 2" 
                  class="w-full h-full object-cover"
                  referrerPolicy="no-referrer"
                />
              </div>
            </div>
          </div>
        </section>

        <!-- Content Grid -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-16">
          <div class="lg:col-span-2 space-y-12">
            <div class="space-y-6">
              <h3 class="text-3xl font-black tracking-tight text-neutral-900 dark:text-white uppercase italic">The Challenge</h3>
              <p class="text-xl text-neutral-600 dark:text-neutral-400 leading-relaxed font-light">
                {project.description}
                <br/><br/>
                Building a scalable architecture requires more than just code; it requires a deep understanding of the problem domain. This project pushed the boundaries of <span class="text-indigo-600 dark:text-indigo-400 font-medium">modern web engineering</span>, focusing on low-latency interactions and high-throughput data processing.
              </p>
            </div>

            <div class="space-y-8">
              <h3 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-3">
                <CheckCircle2 class="w-6 h-6 text-green-500" />
                Core Capabilities
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {#each features as feature, i}
                  <div 
                    class="p-4 bg-neutral-50 dark:bg-neutral-800/30 rounded-2xl border border-neutral-200 dark:border-neutral-800 flex items-center gap-4 hover:border-indigo-500/30 transition-colors group"
                    transition:fly={{ x: -20, delay: 400 + (i * 100), duration: 500 }}
                  >
                    <div class="w-2 h-2 bg-indigo-500 rounded-full group-hover:scale-150 transition-transform"></div>
                    <span class="text-neutral-700 dark:text-neutral-300 font-medium">{feature}</span>
                  </div>
                {/each}
              </div>
            </div>
          </div>

          <div class="space-y-12">
            <!-- Tech Stack -->
            <div class="space-y-6">
              <h3 class="text-sm font-black uppercase tracking-[0.3em] text-neutral-400">Technology Stack</h3>
              <div class="grid grid-cols-1 gap-3">
                {#each project.tech_stack as tech, i}
                  <div 
                    class="flex items-center gap-4 p-4 bg-white dark:bg-neutral-800 rounded-2xl border border-neutral-200 dark:border-neutral-800 shadow-sm hover:shadow-md transition-all hover:-translate-x-2"
                    transition:fly={{ x: 20, delay: 600 + (i * 100), duration: 500 }}
                  >
                    <div class="w-12 h-12 bg-neutral-50 dark:bg-neutral-900 rounded-xl flex items-center justify-center border border-neutral-100 dark:border-neutral-700">
                      <svelte:component this={techIcons[tech] || Code2} class="w-6 h-6 text-indigo-600 dark:text-indigo-400" />
                    </div>
                    <div>
                      <div class="font-bold text-neutral-900 dark:text-white">{tech}</div>
                      <div class="text-[10px] text-neutral-500 uppercase tracking-widest font-bold">Core Module</div>
                    </div>
                  </div>
                {/each}
              </div>
            </div>

            <!-- CTA -->
            <div class="p-8 bg-indigo-600 rounded-[2rem] text-white space-y-6 shadow-2xl shadow-indigo-500/30">
              <h4 class="text-xl font-bold leading-tight">Ready to see it in action?</h4>
              <p class="text-indigo-100 text-sm font-light">Explore the live deployment or dive into the codebase on GitHub.</p>
              <div class="space-y-3">
                <a 
                  href={project.live_demo} 
                  target="_blank"
                  class="w-full py-4 bg-white text-indigo-600 font-bold rounded-xl hover:bg-neutral-100 transition-all flex items-center justify-center gap-2 shadow-lg"
                >
                  Launch Project <Globe class="w-4 h-4" />
                </a>
                <a 
                  href={project.github_link} 
                  target="_blank"
                  class="w-full py-4 bg-indigo-700 text-white font-bold rounded-xl hover:bg-indigo-800 transition-all flex items-center justify-center gap-2 border border-indigo-500/50"
                >
                  Source Code <Github class="w-4 h-4" />
                </a>
              </div>
            </div>
          </div>
        </section>

        <!-- Footer / Next Steps -->
        <footer class="pt-20 border-t border-neutral-100 dark:border-neutral-800 text-center space-y-6 pb-12">
          <div class="inline-block px-4 py-1 bg-neutral-100 dark:bg-neutral-800 rounded-full text-[10px] font-bold text-neutral-500 uppercase tracking-widest">End of Case Study</div>
          <h3 class="text-2xl font-black text-neutral-900 dark:text-white uppercase italic">Interested in working together?</h3>
          <button 
            on:click={onClose}
            class="px-8 py-4 bg-neutral-900 dark:bg-neutral-100 text-white dark:text-black font-bold rounded-full hover:scale-105 transition-transform"
          >
            Get In Touch
          </button>
        </footer>

      </div>
    </div>
  </div>
{/if}

<style>
  /* Prevent scrolling on body when modal is open */
  :global(body.modal-open) {
    overflow: hidden;
  }
</style>
