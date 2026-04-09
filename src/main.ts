import { mount } from 'svelte';
import App from './App.svelte';
import './index.css';

console.log('Svelte app mounting App component...');

try {
  const root = document.getElementById('root');
  if (root) {
    mount(App, { target: root });
    console.log('App component mounted successfully');
  } else {
    console.error('Root element not found');
  }
} catch (err) {
  console.error('Svelte mount error:', err);
}
