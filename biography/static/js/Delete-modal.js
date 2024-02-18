class DeleteModal extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
  <div id="modal-delete" class="modal custom-modal">
      <div class="modal-background"></div>

      <div class="modal-content modal-card is-full-width">
        <div class="box">
      
          <p class="is-main is-font-md m-6">Are you sure you want to delete this item?</p>
          <button class="button is-danger is-rounded is-white">Delete</button>
        </div>
      </div>
      <button class="modal-close is-large" mx-6 aria-label="close">Close</button>
    </div> 
    `;
  }
}

customElements.define("delete-component", DeleteModal);
