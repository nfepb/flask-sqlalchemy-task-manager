document.addEventListener("DOMContentLoaded", function () {
  // Sidenav initialisation
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
  // Modal initialisation
  let modal = document.querySelectorAll(".modal");
  M.Modal.init(modal);
  // Datepicker initialisation
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" },
  });
  // Select dropdown initialisation
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);
});
