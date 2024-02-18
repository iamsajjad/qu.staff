class PersonalInfo extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
 <div class="box mx-6 my-4">
        <section class="is-flex is-justify-content-space-between is-mobile">
          <div>
            <!-- birthday icon -->
            <span class="pr-2 icon-text m-3 is-right-border">
              <span class="icon">
                <img src="./assets/icons/birthday-icon.svg" />
              </span>
              <span class="mt-1 is-main">1998</span>
            </span>
            <!-- gender icon -->
            <span class="pr-2 icon-text m-3 is-right-border">
              <span class="icon">
                <img src="./assets/icons/gender-icon.svg" />
              </span>
              <span class="mt-1 is-main">male</span>
            </span>
          </div>
          <div style="width: auto; position: relative">
            <div class="is-white-bg p-4 is-rounded button is-avatar">
              <p style="font-size: 100px" class="is-main">A</p>
            </div>
            <p class="mt-6 is-font-md">Dr. Full name goes here</p>
          </div>

          <div>
            <!-- location icon -->
            <span class="pl-2 icon-text m-3 is-left-border">
              <span class="icon">
                <img src="./assets/icons/location-icon.svg" />
              </span>
              <span class="mt-1 is-main">Iraqi</span>
            </span>
            <!-- graduation year icon -->
            <span class="pl-2 icon-text m-3 is-left-border">
              <span class="icon">
                <img src="./assets/icons/graduation-icon.svg" />
              </span>
              <span class="mt-1 is-main">PHD</span>
            </span>
          </div>
        </section>
        <hr class="navbar-divider" />
        <div class="is-flex is-justify-content-space-between is-flex-wrap-wrap">
          <div class="is-flex is-flex-direction-column">
            <div class="my-1">
              <span class="is-main">Scientific Title : </span>
              <span>Scientific lecturer</span>
            </div>
            <div class="my-1">
              <span class="is-main">Specialty :</span>
              <span> Network </span>
            </div>
            <div class="my-1">
              <span class="is-main">General Specialty: </span>
              <span> Engineering </span>
            </div>
            <div class="my-1">
              <span class="is-main">Personal Email: </span>
              <span>AhmedAil@gmail.com</span>
            </div>
          </div>

          <div class="is-flex is-flex-direction-column">
            <div class="my-1">
              <span class="is-main">Position :</span>
              <span>Lecturer</span>
            </div>
            <div class="my-1">
              <span class="is-main">Department:</span>
              <span>Information Network</span>
            </div>
            <div class="my-1">
              <span class="is-main">Mother language :</span>
              <span>Arabic </span>
            </div>
            <div class="my-1">
              <span class="is-main">Formal Email:</span>
              <span> AhmedAil@gmail.com </span>
            </div>
          </div>
        </div>
      </div>
    `;
  }
}

customElements.define("info-component", PersonalInfo);
