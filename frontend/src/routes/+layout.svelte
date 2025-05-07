<script lang="ts">
  import "$lib/styles.css"
  import { ConfigService } from "$lib/config/service";
  import { configState, modalState } from "$lib/store.svelte";
  import Modal from "$lib/popup/Modal.svelte";


  let { children } = $props();
  const configService = new ConfigService();

  async function initialise(): Promise<void> {
    const config = await configService.getConfig();
    Object.assign(configState, config);
  }
</script>

<!-- This ensures that the config is always initialised before any components are rendered -->
{#await initialise()}
  <div class="loading">
    <p>Loading...</p>
  </div>
{:catch error}
  <div class="error">
    <p>Error loading config: {error.message}</p>
  </div>
{:then}
  {@render children()}
{/await}

<Modal
  bind:showModal={modalState.showModal}
  header={modalState.header}
  children={modalState.body}
  on:close={() => (modalState.showModal = false)}
/>
