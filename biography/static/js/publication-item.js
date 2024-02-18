class PublicationItem extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
  <div id="modal-edit" class="modal custom-modal">
      <div class="modal-background"></div>

      <div class="modal-content modal-card is-full-width">
        <div class="box">
          <p class="is-font-md my-4 is-main is-centered">
            Article title goes here
          </p>
          <div class="is-flex is-flex-direction-column">
            <p class="is-main my-2">Title</p>
            <input
              class="input is-normal"
              type="text"
              placeholder="Normal input"
            />
          </div>
          <div
            class="is-flex is-flex-direction-row is-justify-content-space-between is-flex-wrap-wrap is-full-width"
          >
            <div class="is-flex is-flex-direction-column mr-4">
              <p class="is-main my-2">Journal</p>
              <input
                class="input is-normal"
                type="text"
                placeholder="Normal input"
              />
            </div>
            <div class="is-flex is-flex-direction-column">
              <p class="is-main my-2">pages</p>
              <input
                class="input is-normal"
                type="text"
                placeholder="Normal input"
              />
            </div>
            <div class="is-flex is-flex-direction-column">
              <p class="is-main my-2">Publisher</p>
              <input
                class="input is-normal"
                type="text"
                placeholder="Normal input"
              />
            </div>
            <div class="is-flex is-flex-direction-column">
              <p class="is-main my-2">URL</p>
              <input
                class="input is-normal"
                type="text"
                placeholder="Normal input"
              />
            </div>
            <div class="is-flex is-flex-direction-column">
              <p class="is-main my-2">Issue</p>
              <input
                class="input is-normal"
                type="number"
                placeholder="Normal input"
              />
            </div>
            <div class="is-flex is-flex-direction-column">
              <p class="is-main my-2">Volume</p>
              <input
                class="input is-normal"
                type="number"
                placeholder="Normal input"
              />
            </div>

            <div class="is-flex my-3 is-flex-direction-column is-full-width">
              <p class="is-main my-2">Description</p>
              <textarea
                class="textarea"
                placeholder="Write your description here ..."
                rows="10"
              ></textarea>
            </div>
          </div>

          <button class="button is-main-bg is-rounded is-white">Save</button>
        </div>
      </div>

      <button class="modal-close is-large" aria-label="close"></button>
    </div> 
    `;
  }
}

customElements.define("publication-component", PublicationItem);
