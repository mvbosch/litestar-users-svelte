<script lang="ts" context="module">
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	import type { FormPath } from "sveltekit-superforms";
 
	// the form object
	type T = Record<string, unknown>;
	// the path/name of the field in the form object
	type U = unknown;
</script>
 
<script
	lang="ts"
	generics="T extends Record<string, unknown>, U extends FormPath<T>"
>
	import { Description, Field, type FieldProps, FieldErrors } from "formsnap";
	import type { SuperForm } from "sveltekit-superforms";
 
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
  type DescriptionProps = { description: string } | {};
	type $$Props = FieldProps<T, U> & DescriptionProps;
 
	export let form: SuperForm<T>;
	export let name: U;
  export let description: string = "";
</script>
 
<!-- passing the slot props down are optional -->
<Field {form} {name} let:value let:errors let:tainted let:constraints>
	<slot {value} {errors} {tainted} {constraints} />
  {#if description}
    <Description>{description}</Description>
  {/if}
	<FieldErrors />
</Field>
