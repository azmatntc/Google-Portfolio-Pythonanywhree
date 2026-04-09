<!-- src/components/VisibleSection.svelte -->
<script>
    export let id = "";
    export let className = "";
</script>

<section {id} class={className}>
    <slot />
</section>
