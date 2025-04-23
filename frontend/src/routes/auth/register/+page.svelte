<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  
  import Register from '$domain/users/forms/Register.svelte';

  let socketConnection: WebSocket;

  function socketMessageHandler(event: MessageEvent) {
    const data = JSON.parse(event.data);
    console.log('Message from server ', data);
  }

  onMount(() => {
    socketConnection = new WebSocket('wss://localhost:5400/api/');
    socketConnection.onmessage = socketMessageHandler;
  })

  onDestroy(() => {
    socketConnection.close();
  })
</script>

<div>
  <h1>Register</h1>
  <form-container>
    <Register />
    <p>Already have an account? <a href="/auth/register">Login here</a></p>
  </form-container>
</div>

<style>
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
