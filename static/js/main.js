(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {
    select("#navbar").classList.toggle("navbar-mobile");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /**
   * Animation on scroll
   */
  window.addEventListener("load", () => {
    AOS.init({
      duration: 0,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Contact Form functionality
   */
  document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".input");

    function focusFunc() {
      let parent = this.parentNode;
      parent.classList.add("focus");
    }

    function blurFunc() {
      let parent = this.parentNode;
      if (this.value == "") {
        parent.classList.remove("focus");
      }
    }

    inputs.forEach((input) => {
      input.addEventListener("focus", focusFunc);
      input.addEventListener("blur", blurFunc);
    });

    const sendButton = document.getElementById("sendButton");
    const usernameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');
    const messageInput = document.querySelector('textarea[name="message"]');

    sendButton.addEventListener("click", function () {
      const username = usernameInput.value;
      const email = emailInput.value;
      const phone = phoneInput.value;
      const message = messageInput.value;
      const phoneNumber = "+9779806400774";

      if (
        username.trim() !== "" &&
        email.trim() !== "" &&
        phone.trim() !== "" &&
        message.trim() !== ""
      ) {
        const encodedMessage = encodeURIComponent(
          `Username: ${username}\nEmail: ${email}\nPhone: ${phone}\nMessage: ${message}`
        );
        window.open(
          `https://wa.me/${phoneNumber}?text=${encodedMessage}`,
          "_blank"
        );
      } else {
        alert("Please fill in all fields.");
      }
    });

    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    menuToggle.addEventListener("click", function () {
      navLinks.classList.toggle("active");
    });
  });
})();
