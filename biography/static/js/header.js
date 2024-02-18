class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
    <header>
      <section class="hero py-3 is-main-bg">
      <div class="is-flex hero-body is-justify-content-space-between">
        <div>
          <p class="title is-white mb-20">Organization Name</p>
        </div>
        <div class="is-white-bg p-4 is-rounded button" style="height: auto">
          <img src="./assets/icons/uni-logo.svg" />
        </div>
      </div>
      <div class="is-flex mx-3 head-btn" >
        <!-- language dropdown -->


         <div class="lang">
      <img id="lang-btn" src="./assets/icons/lang-icon.svg" />
      <div class="lang-content">
        <a >Arabic</a>
        <a >English</a>
      </div>
    </div>
       
        <!--  -->

        <!-- login/logout dropdown -->
     <div class="login">
      <img id="lang-btn" src="./assets/icons/login-icon.svg" />
      <div class="login-content">
        <a >Login</a>
      </div>
    </div>
        <!--  -->
      </div>
    </section>
    </header>
    `;
  }
}

customElements.define("header-component", Header);
