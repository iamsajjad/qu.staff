class PublicationsEdit extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
  <div
      class="box mx-4 mb-6 is-flex is-flex-direction-row is-justify-content-space-between"
    >
      <div class="is-flex is-flex-direction-row">
        <img class="is-pointer mx-2" src="./assets/icons/publication.svg" />

        <p class="is-main is-font-md">Publication</p>
      </div>
      <img
        id="publication_btn"
        class="is-pointer"
        src="./assets/icons/down-arrow.svg"
      />
    </div>
    <div class="box mx-4 publication" id="publication_part">
      <div
        class="my-2 is-justify-content-space-between is-flex-wrap-wrap p-2 is-gray-bg is-flex is-flex-direction-row"
      >
        <div class="is-flex is-flex-direction-column">
          <div class="is-font-md is-main">
            Soft computing approach on estimating the lateral confinement
            coefficient
          </div>
          <div class="my-2">
            O India, 2023Advances in Decision Sciences, 27, (1), 172-191
          </div>
        </div>
        <div class="is-flex is-flex-direction-row" style="gap: 7px">
          <img 
          data-target="modal-delete"
          class="is-pointer modal-trigger-delete is-clickable" 
          src="./assets/icons/delete.svg" />
          <img 
           data-target="modal-edit"
          class="is-pointer modal-trigger-edit is-clickable" src="./assets/icons/edit.svg" />
        </div>
      </div>

      <!-- new item -->
      <div
        class="my-2 is-justify-content-space-between is-flex-wrap-wrap p-2 is-gray-bg is-flex is-flex-direction-row"
      >
        <div class="is-flex is-flex-direction-column">
          <div class="is-font-md is-main">
            Soft computing approach on estimating the lateral confinement
            coefficient
          </div>
          <div class="my-2">
            O India, 2023Advances in Decision Sciences, 27, (1), 172-191
          </div>
        </div>
        <div class="is-flex is-flex-direction-row" style="gap: 7px">
          <img 
          data-target="modal-delete"
          class="is-pointer modal-trigger-delete is-clickable" 
          src="./assets/icons/delete.svg" />
          <img 
           data-target="modal-edit"
          class="is-pointer modal-trigger-edit is-clickable" src="./assets/icons/edit.svg" />
        </div>
      </div>
      <!-- new item -->
      <div
        class="my-2 is-justify-content-space-between is-flex-wrap-wrap p-2 is-gray-bg is-flex is-flex-direction-row"
      >
        <div class="is-flex is-flex-direction-column">
          <div class="is-font-md is-main">
            Soft computing approach on estimating the lateral confinement
            coefficient
          </div>
          <div class="my-2">
            O India, 2023Advances in Decision Sciences, 27, (1), 172-191
          </div>
        </div>
        <div class="is-flex is-flex-direction-row" style="gap: 7px">
          <img 
          data-target="modal-delete"
          class="is-pointer modal-trigger-delete is-clickable" 
          src="./assets/icons/delete.svg" />
          <img 
           data-target="modal-edit"
          class="is-pointer modal-trigger-edit is-clickable" src="./assets/icons/edit.svg" />
        </div>
      </div>
      <!-- new item -->
      <div
        class="my-2 is-justify-content-space-between is-flex-wrap-wrap p-2 is-gray-bg is-flex is-flex-direction-row"
      >
        <div class="is-flex is-flex-direction-column">
          <div class="is-font-md is-main">
            Soft computing approach on estimating the lateral confinement
            coefficient
          </div>
          <div class="my-2">
            O India, 2023Advances in Decision Sciences, 27, (1), 172-191
          </div>
        </div>
        <div class="is-flex is-flex-direction-row" style="gap: 7px">
          <img 
          data-target="modal-delete"
          class="is-pointer modal-trigger-delete is-clickable" 
          src="./assets/icons/delete.svg" />
          <img 
           data-target="modal-edit"
          class="is-pointer modal-trigger-edit is-clickable" src="./assets/icons/edit.svg" />
        </div>
      </div>
      <!-- new item -->
      <div
        class="my-2 is-justify-content-space-between is-flex-wrap-wrap p-2 is-gray-bg is-flex is-flex-direction-row"
      >
        <div class="is-flex is-flex-direction-column">
          <div class="is-font-md is-main">
            Soft computing approach on estimating the lateral confinement
            coefficient
          </div>
          <div class="my-2">
            O India, 2023Advances in Decision Sciences, 27, (1), 172-191
          </div>
        </div>
        <div class="is-flex is-flex-direction-row" style="gap: 7px">
          <img 
          data-target="modal-delete"
          class="is-pointer modal-trigger-delete is-clickable" 
          src="./assets/icons/delete.svg" />
          <img 
           data-target="modal-edit"
          class="is-pointer modal-trigger-edit is-clickable" src="./assets/icons/edit.svg" />
        </div>
      </div>
    </div>
    `;
  }
}

customElements.define("edit-publications-component", PublicationsEdit);
