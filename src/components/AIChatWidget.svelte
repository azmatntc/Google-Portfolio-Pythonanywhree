<script lang="ts">
  import { MessageSquare, X, Send, LoaderCircle, Bot, CircleAlert } from 'lucide-svelte';
  import { api, ApiError } from '../lib/api';
  import { analytics } from '../services/analyticsService';
  import { onMount } from 'svelte';

  let isOpen = false;
  let input = '';
  let messages = [
    { role: 'assistant', text: "Hi! I'm your AI assistant. Ask me anything about my services, portfolio, or availability." }
  ];
  let loading = false;
  let error: string | null = null;

  function toggleChat() {
    isOpen = !isOpen;
    if (isOpen) {
      analytics.track({ type: 'chat_opened' });
    }
  }

  async function sendMessage() {
    if (!input.trim() || loading) return;

    const userMsg = input;
    input = '';
    messages = [...messages, { role: 'user', text: userMsg }];
    loading = true;
    error = null;

    analytics.track({ type: 'chat_message_sent', messageLength: userMsg.length });

    try {
      const data = await api.post<{ reply: string }>('/api/chat', { message: userMsg });
      messages = [...messages, { role: 'assistant', text: data.reply }];
    } catch (e) {
      console.error('AI Chat Error:', e);
      error = e instanceof ApiError ? e.message : 'I encountered an error. Please try again.';
      messages = [...messages, { role: 'assistant', text: "Sorry, I'm having trouble processing that right now." }];
    } finally {
      loading = false;
    }
  }
</script>

<div class="fixed bottom-6 right-6 z-[100]">
  {#if isOpen}
    <div class="mb-4 w-[350px] sm:w-[400px] h-[500px] bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-in slide-in-from-bottom-4 duration-300">
      <div class="p-4 bg-neutral-50 dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-indigo-600 rounded-full flex items-center justify-center">
            <Bot class="w-5 h-5 text-white" />
          </div>
          <div>
            <div class="text-sm font-bold text-neutral-900 dark:text-white">AI Assistant</div>
            <div class="text-[10px] text-green-600 dark:text-green-500 font-bold uppercase tracking-widest">Online</div>
          </div>
        </div>
        <button on:click={() => isOpen = false} class="text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors">
          <X class="w-5 h-5" />
        </button>
      </div>

      <div class="flex-1 overflow-y-auto p-4 space-y-4 scroll-smooth">
        {#each messages as msg}
          <div class="flex {msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-2 duration-300">
            <div class="max-w-[85%] p-3 rounded-2xl text-sm {msg.role === 'user' ? 'bg-indigo-600 text-white rounded-tr-none' : 'bg-neutral-100 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-300 rounded-tl-none'}">
              {msg.text}
            </div>
          </div>
        {/each}
        
        {#if loading}
          <div class="flex justify-start">
            <div class="bg-neutral-100 dark:bg-neutral-800 p-4 rounded-2xl rounded-tl-none flex gap-1 items-center">
              <div class="w-1.5 h-1.5 bg-neutral-400 dark:bg-neutral-500 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
              <div class="w-1.5 h-1.5 bg-neutral-400 dark:bg-neutral-500 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
              <div class="w-1.5 h-1.5 bg-neutral-400 dark:bg-neutral-500 rounded-full animate-bounce"></div>
            </div>
          </div>
        {/if}

        {#if error}
          <div class="flex justify-center">
            <div class="px-3 py-1 bg-red-500/10 border border-red-500/20 rounded-full text-[10px] text-red-600 dark:text-red-400 flex items-center gap-1.5">
              <CircleAlert class="w-3 h-3" />
              {error}
            </div>
          </div>
        {/if}
      </div>

      <form on:submit|preventDefault={sendMessage} class="p-4 border-t border-neutral-200 dark:border-neutral-800 flex gap-2 bg-white dark:bg-neutral-900">
        <input 
          type="text" 
          bind:value={input}
          disabled={loading}
          placeholder={loading ? "AI is thinking..." : "Ask me something..."}
          class="flex-1 bg-neutral-50 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-xl px-4 py-2 text-sm text-neutral-900 dark:text-white focus:outline-none focus:border-indigo-500 transition-colors placeholder:text-neutral-400 dark:placeholder:text-neutral-600 disabled:opacity-50 disabled:cursor-not-allowed"
        />
        <button type="submit" disabled={!input.trim() || loading} class="p-2 bg-indigo-600 text-white rounded-xl hover:bg-indigo-500 transition-colors disabled:opacity-50 min-w-[40px] flex items-center justify-center">
          {#if loading}
            <LoaderCircle class="w-4 h-4 animate-spin" />
          {:else}
            <Send class="w-4 h-4" />
          {/if}
        </button>
      </form>
    </div>
  {/if}

  <button 
    on:click={toggleChat}
    class="w-14 h-14 bg-indigo-600 text-white rounded-full shadow-lg hover:bg-indigo-500 transition-all flex items-center justify-center group active:scale-95"
  >
    {#if isOpen}
      <X class="w-6 h-6" />
    {:else}
      <MessageSquare class="w-6 h-6 group-hover:scale-110 transition-transform" />
    {/if}
  </button>
</div>

