document.addEventListener("DOMContentLoaded", function () {
  // Sidenav initialisation
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
  let modal = document.querySelectorAll(".modal");
  M.Modal.init(modal);
});
