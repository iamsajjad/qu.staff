document.addEventListener("DOMContentLoaded", function () {
  const publication_btn = document.getElementById("publication_btn");
  const publication_part = document.getElementById("publication_part");
  const personal_btn = document.getElementById("personal_btn");
  const personal_part = document.getElementById("personal_part");
  const links_part = document.getElementById("links_part");
  const links_btn = document.getElementById("links_btn");
  personal_btn.addEventListener("click", () => {
    personal_part.classList.toggle("hide");
  });
  publication_btn.addEventListener("click", () => {
    publication_part.classList.toggle("hide");
  });
  links_btn.addEventListener("click", () => {
    links_part.classList.toggle("hide");
  });
  // const lang_list = document.getElementById("lang-list");
  // const login_list = document.getElementById("login-list");
  const login_btn = document.getElementById("login-btn");
  // const lang_btn = document.getElementById("lang-btn");

  lang_btn.addEventListener("click", function (event) {
    event.stopPropagation();
    lang_list.classList.toggle("is-active");
    login_list.classList.remove("is-active");
    // You can add an additional class to the button to indicate that it's active
    lang_btn.classList.toggle("is-active-btn");
    login_btn.classList.remove("is-active-btn");
  });

  login_btn.addEventListener("click", function (event) {
    event.stopPropagation();
    login_list.classList.toggle("is-active");
    lang_list.classList.remove("is-active");
    // You can add an additional class to the button to indicate that it's active
    login_btn.classList.toggle("is-active-btn");
    lang_btn.classList.remove("is-active-btn");
  });

  // Close the dropdown when clicking outside of it
  document.addEventListener("click", function (event) {
    if (
      !login_list.contains(event.target) &&
      !login_btn.contains(event.target)
    ) {
      login_list.classList.remove("is-active");
      // Remove the active class from the button
      login_btn.classList.remove("is-active-btn");
    }
    if (!lang_list.contains(event.target) && !lang_btn.contains(event.target)) {
      lang_list.classList.remove("is-active");
      // Remove the active class from the button
      lang_btn.classList.remove("is-active-btn");
    }
  });

  const lang_list = document.getElementById("lang-list");
  const login_list = document.getElementById("login-list");
  const loging_btn = document.getElementById("login-btn");
  const lang_btn = document.getElementById("lang-btn");

  lang_btn.addEventListener("click", function (event) {
    event.stopPropagation();
    lang_list.classList.toggle("is-active");
    login_list.classList.remove("is-active");
  });
  loging_btn.addEventListener("click", function (event) {
    event.stopPropagation();
    login_list.classList.toggle("is-active");
    lang_list.classList.remove("is-active");
  });

  // Close the dropdown when clicking outside of it
  document.addEventListener("click", function (event) {
    if (!login_list.contains(event.target)) {
      login_list.classList.remove("is-active");
    }
    if (!lang_list.contains(event.target)) {
      lang_list.classList.remove("is-active");
    }
  });
});
document.addEventListener("DOMContentLoaded", () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeModal($el) {
    $el.classList.remove("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal

  // edit publications modal
  (document.querySelectorAll(".modal-trigger-edit") || []).forEach(
    ($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);

      $trigger.addEventListener("click", () => {
        openModal($target);
      });
    }
  );
  // edit links modal
  (document.querySelectorAll(".link-trigger-edit") || []).forEach(
    ($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);

      $trigger.addEventListener("click", () => {
        openModal($target);
      });
    }
  );
  // delete publications modal
  (document.querySelectorAll(".modal-trigger-delete") || []).forEach(
    ($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);

      $trigger.addEventListener("click", () => {
        openModal($target);
      });
    }
  );
  // Add a click event on various child elements to close the parent modal
  (
    document.querySelectorAll(
      ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button"
    ) || []
  ).forEach(($close) => {
    const $target = $close.closest(".modal");

    $close.addEventListener("click", () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener("keydown", (event) => {
    if (event.code === "Escape") {
      closeAllModals();
    }
  });
});

/// change the main color by the color input in the setting page
const colorPicker = document.getElementById("colorPicker");

colorPicker.addEventListener("input", function () {
  const selectedColor = colorPicker.value;
  document.documentElement.style.setProperty("--main-color", selectedColor);
});

function fileSize(FILE_SIZS) {

  var file = document.getElementById("image");

  const fileSize = file.files[0].size;
  const FILE_SIZS_BYTE = FILE_SIZS * 1024 * 1024;

  if (fileSize > FILE_SIZS_BYTE){
    file.setCustomValidity(`File must not exceed ${FILE_SIZS}MB in size`);
    file.reportValidity();
  } else {
    file.setCustomValidity("");
  }
}

async function copy(textToCopy) {
  // Navigator clipboard api needs a secure context (https)
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(textToCopy);
  } else {
    // Use the 'out of viewport hidden text area' trick
    const textArea = document.createElement("textarea");
    textArea.value = textToCopy;

    // Move textarea out of the viewport so it's not visible
    textArea.style.position = "absolute";
    textArea.style.left = "-999999px";

    document.body.prepend(textArea);
    textArea.select();

    try {
      document.execCommand('copy');
    } catch (error) {
      console.error(error);
    } finally {
      textArea.remove();
    }
  }
}
