class Publications extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
   <div class="box mx-6">
        <div class="is-flex is-justify-content-start mb-4">
          <span class="mx-2"
            ><img src="./assets/icons/Publication-icon.svg"
          /></span>
          <span class="is-font-md is-main mx-2"> Publications</span>
        </div>
        <div class="is-flex is-flex-direction-row is-full-width">
          <section
            class="px-2"
            style="overflow-y: auto; height: 320px; overflow-x: hidden"
          >
            <!-- single year -->
            <section class="is-flex is-align-items-center">
              <div class="is-main">1990</div>
              <div
                class="is-flex is-flex-direction-column is-align-items-center"
              >
                <span class="is-dot is-active-dot"></span>
                <div class="is-dot-col"></div>
              </div>
            </section>
            <!-- single year -->
            <section class="is-flex is-align-items-center">
              <div class="is-main-light">1990</div>
              <div
                class="is-flex is-flex-direction-column is-align-items-center"
              >
                <span class="is-dot"></span>
                <div class="is-dot-col"></div>
              </div>
            </section>
            <!-- single year -->
            <section class="is-flex is-align-items-center">
              <div class="is-main-light">1990</div>
              <div
                class="is-flex is-flex-direction-column is-align-items-center"
              >
                <span class="is-dot"></span>
                <div class="is-dot-col"></div>
              </div>
            </section>
          </section>
          <section
            class="is-full-width ml-3"
            style="overflow-y: auto; height: 310px"
          >
            <div
              data-target="modal-edit"
              class="modal-trigger-edit is-clickable is-gray-bg p-2 my-2 is-full-width"
            >
              <div class="my-2 is-main">
                Soft computing approach on estimating the lateral confinement
                coefficient
              </div>
              <div style="color: gray">
                O India, 2023Advances in Decision Sciences, 27, (1), 172-191
              </div>
            </div>
            <div
              data-target="modal-edit"
              class="modal-trigger-edit is-clickable is-gray-bg p-2 my-2 is-full-width"
            >
              <div class="my-2 is-main">
                Soft computing approach on estimating the lateral confinement
                coefficient
              </div>
              <div style="color: gray">
                O India, 2023Advances in Decision Sciences, 27, (1), 172-191
              </div>
            </div>
            <div
              data-target="modal-edit"
              class="modal-trigger-edit is-clickable is-gray-bg p-2 my-2 is-full-width"
            >
              <div class="my-2 is-main">
                Soft computing approach on estimating the lateral confinement
                coefficient
              </div>
              <div style="color: gray">
                O India, 2023Advances in Decision Sciences, 27, (1), 172-191
              </div>
            </div>
          </section>
        </div>
      </div>
    `;
  }
}

customElements.define("publications-component", Publications);
