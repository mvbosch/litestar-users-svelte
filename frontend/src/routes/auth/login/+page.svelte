<script>
  import Login from '$domain/users/forms/Login.svelte';
</script>

<div>
  <h1>Login</h1>
  <form-container>
    <Login />
    <p>Don't have an account? <a href="/auth/register">Register here</a></p>
    <p><a href="/auth/forgot-password">Forgot Password?</a></p>
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
