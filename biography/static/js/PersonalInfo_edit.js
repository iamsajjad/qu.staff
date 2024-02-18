class PersonalInfoEdit extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
    <div  class="is-flex is-flex-direction-row is-align-items-center">
    <div
      class="box is-full-width m-4 is-flex is-flex-direction-row is-justify-content-space-between"
    >
      <p class="is-main is-font-md">Personal Info</p>
      <img
        id="personal_btn"
        class="is-pointer"
        src="./assets/icons/down-arrow.svg"
      />
    </div>
    <button class="button is-rounded is-main-bg is-white mr-3"> Save</button>
    </div>
    <div
      id="personal_part"
      class="is-flex-wrap-wrap mx-4 is-flex is-flex-direction-column mb-6"
    >
      <div class="is-flex is-flex-direction-row">
        <div class="is-flex is-full-width is-flex-direction-column mx-2">
          <p class="is-main my-1 is-font-sm">Gender</p>
          <div class="select is-flex is-flex-direction-column">
            <select id="dropdown">
              <option value="option1">Female</option>
              <option value="option2">Male</option>
            </select>
          </div>
        </div>
        <div class="is-flex is-full-width is-flex-direction-column mx-2">
          <p class="is-main my-1 is-font-sm">Nationality</p>
          <div class="select is-flex is-flex-direction-column">
            <select id="dropdown">
              <option value="option1">Iraqi</option>
              <option value="option1">Iraqi</option>
            </select>
          </div>
        </div>
      </div>

      <div class="is-flex is-flex-direction-row">
        <div class="is-full-width is-flex is-flex-direction-column m-3">
          <p class="is-main is-font-sm">full name</p>
          <input class="input my-1" type="text" />
        </div>

        <div class="is-flex is-flex-direction-column my-3 is-full-width">
          <p class="is-main is-font-sm">Birthday</p>
          <input class="input my-1" type="date" />
        </div>
      </div>

      <div
        class="is-flex is-flex-direction-row is-justify-content-space-between"
      >
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Postion</p>
          <input class="input my-1" type="text" />
        </div>
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Nationality</p>
          <input class="input my-1" type="text" />
        </div>
      </div>
      <div
        class="is-flex is-flex-direction-row is-justify-content-space-between"
      >
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Department</p>
          <input class="input my-1" type="text" />
        </div>
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Formal Email</p>
          <input class="input my-1" type="text" />
        </div>
      </div>
      <div
        class="is-flex is-flex-direction-row is-justify-content-space-between"
      >
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Work Eemail</p>
          <input class="input my-1" type="text" />
        </div>
        <div class="is-flex is-flex-direction-column m-3 is-full-width">
          <p class="is-main is-font-sm">Work Eemail</p>
          <input class="input my-1" type="text" />
        </div>
      </div>
    </div>

    `;
  }
}

customElements.define("edit-infocomponent", PersonalInfoEdit);
