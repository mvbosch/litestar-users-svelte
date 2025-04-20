<script lang="ts">
	import { Control, Label, type ControlProps } from "formsnap";
 
	type $$Props = ControlProps & {
		label: string;
	};
 
	export let label: string;
</script>
 
<Control let:attrs {...$$restProps}>
	<div class="flex flex-col gap-2">
		<Label>{label}</Label>
		<slot {attrs} />
	</div>
</Control>
