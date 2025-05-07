<script lang="ts">
	import { superForm, defaults, type SuperValidated } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';

	import { UserService } from '$domain/users/service';
	import { authenticationSchema, type AuthenticationSchemaType } from '$domain/users/schemas';
	import FieldWrapper from '$lib/forms/formsnap_wrappers/FieldWrapper.svelte';
	import ControlWrapper from '$lib/forms/formsnap_wrappers/ControlWrapper.svelte';
	import { handleSubmissionErrors } from '$lib/forms/utils';

  const userService = new UserService();
  const form = superForm(defaults(zod(authenticationSchema)), {
    SPA: true,
    dataType: 'json',
    resetForm: false,
    validators: zod(authenticationSchema),
    onUpdate: async ({ form }) => await makeRequest(form)
  });
  const { form: formData, enhance } = form;

	async function makeRequest(form: SuperValidated<AuthenticationSchemaType>) {
		if (form.valid) {
			try {
				const user = await userService.register(form.data);
			} catch (error: unknown) {
				try {
					handleSubmissionErrors(error, form, { 409: ['email', 'The user already exists'] });
				} catch (error: unknown) {
					console.error(`Error: ${error}`);
			}
		}
	}}
</script>

<div class="form-container">
<form use:enhance>
  <FieldWrapper {form} name="email" >
    <ControlWrapper label="Email" style="width: 100%">
      <input  type="email" bind:value={$formData.email} />
    </ControlWrapper>
  </FieldWrapper>
  <FieldWrapper {form} name="password" >
    <ControlWrapper  label="Password">
      <input  type="password" bind:value={$formData.password} />
    </ControlWrapper>
  </FieldWrapper>
  <button type="submit">Register</button>
</form>
</div>

<style>
  form {
      display: flex;
      flex-direction: column;
  }
</style>
