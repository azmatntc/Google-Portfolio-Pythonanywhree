<script lang="ts">
  import { Send, LoaderCircle, CircleCheck, CircleAlert } from 'lucide-svelte';
  import { api, ApiError } from '../lib/api';
  import { analytics } from '../services/analyticsService';
  
  let name = '';
  let email = '';
  let message = '';
  let status: 'idle' | 'loading' | 'success' | 'error' = 'idle';
  let errorMessage = '';
  let fieldFocusTimes: Record<string, number> = {};

  function handleFocus(fieldName: string) {
    fieldFocusTimes[fieldName] = Date.now();
    analytics.track({ type: 'form_field_focus', formName: 'contact', fieldName });
  }

  function handleBlur(fieldName: string) {
    const duration = Date.now() - (fieldFocusTimes[fieldName] || Date.now());
    analytics.track({ type: 'form_field_blur', formName: 'contact', fieldName, duration });
  }

  function handleInput(fieldName: string, value: string) {
    analytics.track({ type: 'form_field_input', formName: 'contact', fieldName, valueLength: value.length });
  }

  // Simple validation
  $: isFormValid = name.trim().length > 0 && 
                  email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/) && 
                  message.trim().length >= 10;

  async function handleSubmit() {
    if (!isFormValid) return;
    
    status = 'loading';
    errorMessage = '';
    
    try {
      await api.post('/api/leads', { name, email, message });
      status = 'success';
      analytics.track({ type: 'form_submission_success', formName: 'contact' });
      name = ''; email = ''; message = '';
    } catch (e) {
      console.error('Lead capture failed:', e);
      status = 'error';
      errorMessage = e instanceof ApiError ? e.message : 'Failed to send message. Please check your connection.';
      analytics.track({ 
        type: 'form_submission_error', 
        formName: 'contact', 
        error: errorMessage 
      });
    }
  }
</script>

<div class="bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 p-8 rounded-3xl relative overflow-hidden transition-colors duration-300">
  {#if status === 'success'}
    <div class="text-center py-12 animate-in fade-in zoom-in duration-500">
      <CircleCheck class="w-16 h-16 text-green-500 mx-auto mb-4" />
      <h3 class="text-2xl font-bold mb-2 text-neutral-900 dark:text-white">Message Sent!</h3>
      <p class="text-neutral-600 dark:text-neutral-400">I've received your inquiry and will get back to you within 24 hours.</p>
      <button on:click={() => status = 'idle'} class="mt-8 text-indigo-600 dark:text-indigo-400 font-bold uppercase tracking-widest text-xs hover:text-indigo-500 dark:hover:text-indigo-300 transition-colors">Send another</button>
    </div>
  {:else}
    <form on:submit|preventDefault={handleSubmit} class="space-y-6">
      {#if status === 'error'}
        <div class="p-4 bg-red-500/10 border border-red-500/20 rounded-xl flex items-start gap-3 text-red-600 dark:text-red-400 text-sm animate-in slide-in-from-top-2">
          <CircleAlert class="w-5 h-5 shrink-0" />
          <p>{errorMessage}</p>
        </div>
      {/if}

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="space-y-2">
          <label for="name" class="text-xs font-bold text-neutral-500 uppercase tracking-widest">Name</label>
          <input 
            id="name"
            type="text" 
            bind:value={name}
            required
            placeholder="John Doe"
            on:focus={() => handleFocus('name')}
            on:blur={() => handleBlur('name')}
            on:input={(e) => handleInput('name', e.currentTarget.value)}
            class="w-full bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-xl px-4 py-3 text-neutral-900 dark:text-white focus:outline-none focus:border-indigo-500 transition-colors placeholder:text-neutral-400 dark:placeholder:text-neutral-600"
          />
        </div>
        <div class="space-y-2">
          <label for="email" class="text-xs font-bold text-neutral-500 uppercase tracking-widest">Email</label>
          <input 
            id="email"
            type="email" 
            bind:value={email}
            required
            placeholder="john@example.com"
            on:focus={() => handleFocus('email')}
            on:blur={() => handleBlur('email')}
            on:input={(e) => handleInput('email', e.currentTarget.value)}
            class="w-full bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-xl px-4 py-3 text-neutral-900 dark:text-white focus:outline-none focus:border-indigo-500 transition-colors placeholder:text-neutral-400 dark:placeholder:text-neutral-600"
          />
        </div>
      </div>
      <div class="space-y-2">
        <label for="message" class="text-xs font-bold text-neutral-500 uppercase tracking-widest">Message (Min 10 chars)</label>
        <textarea 
          id="message"
          bind:value={message}
          required
          rows="4"
          placeholder="Tell me about your project..."
          on:focus={() => handleFocus('message')}
          on:blur={() => handleBlur('message')}
          on:input={(e) => handleInput('message', e.currentTarget.value)}
          class="w-full bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-xl px-4 py-3 text-neutral-900 dark:text-white focus:outline-none focus:border-indigo-500 transition-colors resize-none placeholder:text-neutral-400 dark:placeholder:text-neutral-600"
        ></textarea>
      </div>

      <button 
        type="submit" 
        disabled={status === 'loading' || !isFormValid}
        class="w-full py-4 bg-indigo-600 text-white font-bold rounded-xl hover:bg-indigo-500 transition-all flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {#if status === 'loading'}
          <LoaderCircle class="w-5 h-5 animate-spin" />
          Sending...
        {:else}
          <Send class="w-5 h-5" />
          Send Message
        {/if}
      </button>
    </form>
  {/if}
</div>

