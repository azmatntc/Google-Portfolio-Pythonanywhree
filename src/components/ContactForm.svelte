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
  let fieldErrors: Record<string, string> = { name: '', email: '', message: '' };
  let touched: Record<string, boolean> = { name: false, email: false, message: false };

  function validateField(fieldName: string, value: string) {
    if (fieldName === 'name') {
      if (!value.trim()) return 'Identity is required';
      if (value.trim().length < 2) return 'Name is too short';
    }
    if (fieldName === 'email') {
      if (!value.trim()) return 'Digital address is required';
      if (!value.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) return 'Invalid email format';
    }
    if (fieldName === 'message') {
      if (!value.trim()) return 'Project brief is required';
      if (value.trim().length < 10) return 'Please provide at least 10 characters';
    }
    return '';
  }

  function handleFocus(fieldName: string) {
    fieldFocusTimes[fieldName] = Date.now();
    analytics.track({ type: 'form_field_focus', formName: 'contact', fieldName });
  }

  function handleBlur(fieldName: string) {
    const duration = Date.now() - (fieldFocusTimes[fieldName] || Date.now());
    analytics.track({ type: 'form_field_blur', formName: 'contact', fieldName, duration });
    
    touched[fieldName] = true;
    const value = fieldName === 'name' ? name : fieldName === 'email' ? email : message;
    fieldErrors[fieldName] = validateField(fieldName, value);
  }

  function handleInput(fieldName: string, value: string) {
    analytics.track({ type: 'form_field_input', formName: 'contact', fieldName, valueLength: value.length });
    if (touched[fieldName]) {
      fieldErrors[fieldName] = validateField(fieldName, value);
    }
  }

  // Simple validation
  $: isFormValid = name.trim().length >= 2 && 
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

<div class="bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 p-8 md:p-10 rounded-[2.5rem] relative overflow-hidden transition-all duration-300 shadow-xl shadow-neutral-500/5">
  {#if status === 'success'}
    <div class="text-center py-16 animate-in fade-in zoom-in duration-700">
      <div class="w-20 h-20 bg-green-50 dark:bg-green-500/10 rounded-3xl flex items-center justify-center mx-auto mb-6 border border-green-100 dark:border-green-500/20">
        <CircleCheck class="w-10 h-10 text-green-500" />
      </div>
      <h3 class="text-3xl font-black tracking-tight mb-3 text-neutral-900 dark:text-white uppercase italic">Transmission Received</h3>
      <p class="text-neutral-600 dark:text-neutral-400 max-w-xs mx-auto leading-relaxed">I've received your inquiry and will get back to you within 24 hours.</p>
      <button 
        on:click={() => status = 'idle'} 
        class="mt-10 px-8 py-3 bg-neutral-900 dark:bg-white text-white dark:text-black font-bold rounded-full hover:scale-105 transition-transform"
      >
        Send Another
      </button>
    </div>
  {:else}
    <form on:submit|preventDefault={handleSubmit} class="space-y-8">
      {#if status === 'error'}
        <div class="p-4 bg-red-500/10 border border-red-500/20 rounded-2xl flex items-start gap-3 text-red-600 dark:text-red-400 text-sm animate-in slide-in-from-top-2">
          <CircleAlert class="w-5 h-5 shrink-0" />
          <p class="font-medium">{errorMessage}</p>
        </div>
      {/if}

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="space-y-3">
          <label for="name" class="text-[10px] font-black text-neutral-400 uppercase tracking-[0.2em] ml-1">Identity</label>
          <input 
            id="name"
            type="text" 
            bind:value={name}
            required
            placeholder="Your Name"
            on:focus={() => handleFocus('name')}
            on:blur={() => handleBlur('name')}
            on:input={(e) => handleInput('name', e.currentTarget.value)}
            class="w-full bg-neutral-50 dark:bg-neutral-800/50 border {fieldErrors.name ? 'border-red-500/50 focus:border-red-500 focus:ring-red-500/10' : 'border-neutral-200 dark:border-neutral-800 focus:border-indigo-500 focus:ring-indigo-500/20'} rounded-2xl px-5 py-4 text-neutral-900 dark:text-white focus:outline-none focus:ring-2 transition-all placeholder:text-neutral-400 dark:placeholder:text-neutral-600 font-medium"
          />
          {#if fieldErrors.name}
            <p class="text-[10px] font-bold text-red-500 ml-1 animate-in fade-in slide-in-from-top-1">{fieldErrors.name}</p>
          {/if}
        </div>
        <div class="space-y-3">
          <label for="email" class="text-[10px] font-black text-neutral-400 uppercase tracking-[0.2em] ml-1">Digital Address</label>
          <input 
            id="email"
            type="email" 
            bind:value={email}
            required
            placeholder="email@example.com"
            on:focus={() => handleFocus('email')}
            on:blur={() => handleBlur('email')}
            on:input={(e) => handleInput('email', e.currentTarget.value)}
            class="w-full bg-neutral-50 dark:bg-neutral-800/50 border {fieldErrors.email ? 'border-red-500/50 focus:border-red-500 focus:ring-red-500/10' : 'border-neutral-200 dark:border-neutral-800 focus:border-indigo-500 focus:ring-indigo-500/20'} rounded-2xl px-5 py-4 text-neutral-900 dark:text-white focus:outline-none focus:ring-2 transition-all placeholder:text-neutral-400 dark:placeholder:text-neutral-600 font-medium"
          />
          {#if fieldErrors.email}
            <p class="text-[10px] font-bold text-red-500 ml-1 animate-in fade-in slide-in-from-top-1">{fieldErrors.email}</p>
          {/if}
        </div>
      </div>
      <div class="space-y-3">
        <label for="message" class="text-[10px] font-black text-neutral-400 uppercase tracking-[0.2em] ml-1">Project Brief</label>
        <textarea 
          id="message"
          bind:value={message}
          required
          rows="5"
          placeholder="Tell me about your vision..."
          on:focus={() => handleFocus('message')}
          on:blur={() => handleBlur('message')}
          on:input={(e) => handleInput('message', e.currentTarget.value)}
          class="w-full bg-neutral-50 dark:bg-neutral-800/50 border {fieldErrors.message ? 'border-red-500/50 focus:border-red-500 focus:ring-red-500/10' : 'border-neutral-200 dark:border-neutral-800 focus:border-indigo-500 focus:ring-indigo-500/20'} rounded-2xl px-5 py-4 text-neutral-900 dark:text-white focus:outline-none focus:ring-2 transition-all resize-none placeholder:text-neutral-400 dark:placeholder:text-neutral-600 font-medium"
        ></textarea>
        {#if fieldErrors.message}
          <p class="text-[10px] font-bold text-red-500 ml-1 animate-in fade-in slide-in-from-top-1">{fieldErrors.message}</p>
        {/if}
      </div>

      <button 
        type="submit" 
        disabled={status === 'loading' || !isFormValid}
        class="w-full py-5 bg-indigo-600 text-white font-black rounded-2xl hover:bg-indigo-500 transition-all flex items-center justify-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed shadow-xl shadow-indigo-500/20 uppercase tracking-widest text-sm italic group"
      >
        {#if status === 'loading'}
          <LoaderCircle class="w-5 h-5 animate-spin" />
          Processing...
        {:else}
          <Send class="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
          Initiate Contact
        {/if}
      </button>
    </form>
  {/if}
</div>

