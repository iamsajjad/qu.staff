class LinksEdit extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `

 <div
      class="box mx-4 mt-6 mb-4 is-flex is-flex-direction-row is-justify-content-space-between"
    >
      <div class="is-flex is-flex-direction-row">
        <img
          class="is-pointer mx-2"
          src="./assets/icons/link.svg"
        />
        <p class="is-main is-font-md">Links</p>
      </div>
      <img
        id="links_btn"
        class="is-pointer"
        src="./assets/icons/down-arrow.svg"
      />
    </div>
  <div class="box mx-4 my-1" id="links_part">
      <div class="m-3 is-main-light-bg p-3" style="border-radius: 10px">
        <div
          class="is-flex is-links-container is-justify-content-space-between is-align-items-center is-full-width"
        >
          <div class="is-flex is-flex-direction-row">
            <div class="is-links-image p-1 mr-2 my-2 is-full-width">
              <img
                src="./assets/icons/scopus.png"
                style="border-radius: 10px; width: 100%"
              />
            </div>
            <div
              class="is-main mt-3 pt-2 ml-2 is-underlined"
              style="overflow-x: auto"
            >
              http://scholar.google.com/citations?user=IZmYBCsAAAAJ&hl=en
            </div>
          </div>
          <div class="is-flex is-flex-direction-row" style="gap: 7px">
            <img
              data-target="modal-delete"
              class="modal-trigger-delete is-clickable"
              src="./assets/icons/delete.svg"
            />
            <img
              data-target="modal-link-edit"
              class="link-trigger-edit is-clickable"
              src="./assets/icons/edit.svg"
            />
          </div>
        </div>
        <div
          class="is-flex is-links-container is-justify-content-space-between is-align-items-center is-full-width"
        >
          <div class="is-flex is-flex-direction-row">
            <div class="is-links-image p-1 mr-2 my-2 is-full-width">
              <img
                src="./assets/icons/gs.png"
                style="border-radius: 10px; width: 100%"
              />
            </div>
            <div
              class="is-main mt-3 pt-2 ml-2 is-underlined"
              style="overflow-x: auto"
            >
              http://scholar.google.com/citations?user=IZmYBCsAAAAJ&hl=en
            </div>
          </div>
          <div class="is-flex is-flex-direction-row" style="gap: 7px">
            <img
              data-target="modal-delete"
              class="is-pointer modal-trigger-delete is-clickable"
              src="./assets/icons/delete.svg"
            />
            <img
              data-target="modal-link-edit"
              class="link-trigger-edit is-clickable"
              src="./assets/icons/edit.svg"
            />
          </div>
        </div>
      </div>
    </div> 
    `;
  }
}

customElements.define("edit-links-component", LinksEdit);
