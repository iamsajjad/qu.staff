class Links extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
     <div class="box mx-6 my-3">
        <div class="is-flex is-justify-content-start">
          <span class="mx-2"><img src="./assets/icons/Links-icon.svg" /></span>
          <span class="is-font-md is-main mx-2"> Links</span>
        </div>

        <div class="m-3 is-main-light-bg p-3" style="border-radius: 10px">
          <div class="is-flex is-links-container is-align-items-center is-full-width">
            <div class="is-links-image p-1 mr-2 my-2 is-full-width">
              <img
                src="./assets/icons/scopus.png"
               
                style="border-radius: 10px; width: 100%"
              />
            </div>
            <div class="is-right-border"></div>
            <div  class="is-main pt-2 ml-2 is-underlined" style=" overflow-x: auto;   ">
              http://scholar.google.com/citations?user=IZmYBCsAAAAJ&hl=en
            </div>
          </div>
         <div class="is-flex is-links-container is-align-items-center is-full-width">
            <div class="is-links-image p-1 mr-2 my-2 is-full-width">
              <img
                src="./assets/icons/gs.png"
               
                style="border-radius: 10px; width: 100%"
              />
            </div>
            <div class="is-right-border"></div>
            <div  class="is-main pt-2 ml-2 is-underlined" style=" overflow-x: auto;   ">
              http://scholar.google.com/citations?user=IZmYBCsAAAAJ&hl=en
            </div>
          </div>
        </div>
      </div>
    `;
  }
}

customElements.define("links-component", Links);
