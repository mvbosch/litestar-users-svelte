import { type ConfigSchemaType } from "$lib/config/schema";

type ModalObject = {
  showModal: boolean;
  modalType: string;
  header: string;
  body: string;
  trigger: CallableFunction;
}

export let configState: ConfigSchemaType = $state({sessionId: ''});
export let modalState: ModalObject = $state(
  {
    showModal: false,
    modalType: '',
    header: '',
    body: '',
    trigger: function(header: string, body: string) {
      this.showModal = true;
      this.header = header;
      this.body = body;
    }
  }
)
