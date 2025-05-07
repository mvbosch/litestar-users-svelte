<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  
  import { configState, modalState } from '$lib/store.svelte';
  import Register from '$domain/users/forms/Register.svelte';

  let socketConnection: WebSocket;

  function socketMessageHandler(event: MessageEvent) {
    const data = JSON.parse(event.data);
    modalState.trigger("Success", "Here is your verification URL: " + data.url);
  }

  onMount(() => {
    socketConnection = new WebSocket(`ws://localhost:5400/api/token/${configState.sessionId}`);
    socketConnection.onmessage = socketMessageHandler;
  })

  onDestroy(() => {
    if (socketConnection) {
      socketConnection.close();
    }
  })
</script>

<div>
  <h2>Register</h2>
  <form-container>
    <Register />
    <p>Already have an account? <a href="/auth/register">Login here</a></p>
  </form-container>
</div>

<style>
    h2 {
      margin-bottom: 20px;
      color: #333;
      font-size: 1.5rem;
  }
  p {
    margin-top: 1rem;
  }
  form-container {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
    align-items: center;
    justify-items: center;
  }

</style>
