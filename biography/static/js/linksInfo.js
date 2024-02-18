class LinksInfo extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
  <div id="modal-link-edit" class="modal custom-modal">
      <div class="modal-background"></div>

      <div class="modal-content modal-card is-full-width">
        <div class="box">
       
          <div class="is-flex my-3 is-flex-direction-column">
            <p class="is-main is-font-md my-2">Link</p>
            <input
              class="input is-normal"
              type="text"
              placeholder="Write the llink here ..."
            />
          </div>
          <button class="button is-main-bg is-rounded is-white">Save</button>
        </div>
      </div>

      <button class="modal-close is-large" aria-label="close"></button>
    </div> 
    </div> 
      `;
  }
}

customElements.define("links-info-component", LinksInfo);
