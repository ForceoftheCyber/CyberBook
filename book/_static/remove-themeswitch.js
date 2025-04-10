/**
 * Fix to disable theme switching on the page. Removes the the button for switching themes.
 */
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementsByClassName("btn btn-sm nav-link pst-navbar-icon theme-switch-button")[0];
    if (btn) {
      btn.remove();
    }
  });