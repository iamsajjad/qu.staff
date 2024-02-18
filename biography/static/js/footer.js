class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <section class="is-main-bg p-4">
        <div class="columns">
          <div class="column is-white is-four-fifths">
            Technical Support : support@gmail.com
          </div>
          <div class="is-left-border mt-3"></div>
          <div class="column">
            <div class="columns">
              <section class="column has-text-centered">
                <div class="is-white title">444</div>
                <div class="is-white">Visits</div>
              </section>
              <section class="column has-text-centered">
                <div class="is-white title">8584</div>
                <div class="is-white">Visits</div>
              </section>
            </div>
            <section class="has-text-centered">
              <div class="is-white title">66s</div>
              <div class="is-white">Fetch time</div>
            </section>
          </div>
        </div>
        <div class="is-white has-text-centered">Copyright Al-x org ©2023</div>
      </section>
    `;
  }
}

customElements.define("footer-component", Footer);
