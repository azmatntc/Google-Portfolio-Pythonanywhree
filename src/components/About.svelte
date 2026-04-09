<script lang="ts">
  import { Briefcase, GraduationCap, Award, Code2, Cpu, Zap } from 'lucide-svelte';
  import { analytics } from '../services/analyticsService';
  import VisibleSection from './VisibleSection.svelte';

  const achievements = [
    {
      year: '2025',
      title: 'Lead Architect @ TechFlow',
      description: 'Scaled a Django-based microservices architecture to handle 1M+ daily active users.',
      icon: Briefcase
    },
    {
      year: '2023',
      title: 'AI Integration Specialist',
      description: 'Implemented Gemini-powered automated support systems, reducing response times by 80%.',
      icon: Cpu
    },
    {
      year: '2021',
      title: 'Senior Full-Stack Developer',
      description: 'Pioneered Svelte adoption for high-performance dashboarding in fintech.',
      icon: Code2
    },
    {
      year: '2019',
      title: 'CS Excellence Award',
      description: 'Graduated with honors, specializing in distributed systems and security.',
      icon: Award
    }
  ];

  const skills = [
    { name: 'Backend', items: ['Django', 'Python', 'Node.js', 'PostgreSQL', 'Redis'] },
    { name: 'Frontend', items: ['Svelte', 'React', 'Tailwind CSS', 'TypeScript', 'D3.js'] },
    { name: 'Infrastructure', items: ['AWS', 'Docker', 'Kubernetes', 'CI/CD', 'Terraform'] },
    { name: 'AI/ML', items: ['Gemini API', 'LangChain', 'OpenAI', 'PyTorch'] }
  ];

  function trackResumeDownload() {
    analytics.track({ type: 'click_resume_download' });
  }
</script>

<section id="about" class="py-32 bg-neutral-50 dark:bg-neutral-900/30 border-y border-neutral-200 dark:border-neutral-800/50 transition-colors duration-300">
  <VisibleSection className="px-6 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-start">
      
      <!-- Left Column: Bio & Philosophy -->
      <div class="lg:col-span-7 space-y-12">
        <div>
          <h2 class="text-4xl md:text-5xl font-black tracking-tighter mb-8 bg-gradient-to-r from-neutral-900 to-neutral-500 dark:from-white dark:to-neutral-500 bg-clip-text text-transparent">
            ARCHITECTING <br/>DIGITAL EXCELLENCE.
          </h2>
          <div class="space-y-6 text-lg text-neutral-600 dark:text-neutral-400 leading-relaxed max-w-2xl">
            <p>
              I don't just write code; I build <span class="text-neutral-900 dark:text-white font-medium">resilient systems</span> that solve complex business problems. With over 7 years of experience in full-stack architecture, my approach is rooted in the philosophy of <span class="text-indigo-600 dark:text-indigo-400 font-medium italic">"Performance by Design."</span>
            </p>
            <p>
              My expertise lies at the intersection of robust backend engineering with Django and fluid, reactive frontend experiences with Svelte. I believe that every line of code should serve a purpose, and every system should be built to scale from day one.
            </p>
            <p>
              Currently, I'm focused on integrating <span class="text-neutral-900 dark:text-white font-medium">Generative AI</span> into production workflows, moving beyond simple wrappers to create truly intelligent, autonomous applications.
            </p>
          </div>
        </div>

        <!-- Skills Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 pt-8 border-t border-neutral-200 dark:border-neutral-800">
          {#each skills as category}
            <div class="space-y-4">
              <h3 class="text-sm font-bold tracking-widest uppercase text-indigo-600 dark:text-indigo-400">{category.name}</h3>
              <div class="flex flex-wrap gap-2">
                {#each category.items as item}
                  <span class="px-3 py-1 bg-neutral-100 dark:bg-neutral-800/50 text-neutral-700 dark:text-neutral-300 text-xs font-medium rounded-full border border-neutral-200 dark:border-neutral-700/50 hover:border-indigo-500/50 transition-colors">
                    {item}
                  </span>
                {/each}
              </div>
            </div>
          {/each}
        </div>

        <div class="pt-8">
          <button 
            on:click={trackResumeDownload}
            class="px-8 py-4 bg-neutral-900 dark:bg-neutral-100 text-white dark:text-black font-bold rounded-full hover:bg-neutral-800 dark:hover:bg-white transition-all flex items-center gap-2 group"
          >
            Download Full CV <Zap class="w-4 h-4 fill-current group-hover:scale-110 transition-transform" />
          </button>
        </div>
      </div>

      <!-- Right Column: Profile & Timeline -->
      <div class="lg:col-span-5 space-y-16">
        <!-- Profile Picture -->
        <div class="relative group">
          <div class="absolute -inset-1 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-3xl blur opacity-25 group-hover:opacity-50 transition duration-1000 group-hover:duration-200"></div>
          <div class="relative aspect-[4/5] bg-neutral-100 dark:bg-neutral-900 rounded-3xl border border-neutral-200 dark:border-neutral-800 overflow-hidden">
            <img 
              src="https://picsum.photos/seed/architect/800/1000" 
              alt="Developer Profile" 
              class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-700"
              referrerPolicy="no-referrer"
            />
            <div class="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black/80 to-transparent">
              <p class="text-white font-bold text-xl">Elite Architect</p>
              <p class="text-indigo-400 text-sm">Full-Stack & AI Specialist</p>
            </div>
          </div>
        </div>

        <!-- Timeline -->
        <div class="space-y-8">
          <h3 class="text-xl font-bold tracking-tight text-neutral-900 dark:text-white flex items-center gap-2">
            <GraduationCap class="w-5 h-5 text-indigo-600 dark:text-indigo-500" />
            Key Milestones
          </h3>
          <div class="space-y-8 relative before:absolute before:left-[11px] before:top-2 before:bottom-2 before:w-[2px] before:bg-neutral-200 dark:before:bg-neutral-800">
            {#each achievements as item}
              <div class="relative pl-10 group">
                <div class="absolute left-0 top-1 w-6 h-6 bg-white dark:bg-neutral-950 border-2 border-neutral-200 dark:border-neutral-800 rounded-full flex items-center justify-center group-hover:border-indigo-500 transition-colors z-10">
                  <svelte:component this={item.icon} class="w-3 h-3 text-neutral-400 dark:text-neutral-500 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors" />
                </div>
                <div>
                  <span class="text-xs font-bold text-indigo-600 dark:text-indigo-500/80 tracking-widest uppercase">{item.year}</span>
                  <h4 class="text-neutral-900 dark:text-white font-bold mb-1">{item.title}</h4>
                  <p class="text-sm text-neutral-500 leading-relaxed">{item.description}</p>
                </div>
              </div>
            {/each}
          </div>
        </div>
      </div>

    </div>
  </VisibleSection>
</section>
