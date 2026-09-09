/* v3 shared language switcher — progressive-enhancement disclosure.
   With no JS the language links stay visible inline; this collapses
   them behind the globe button. One switcher per page. */
(function () {
  var sw = document.querySelector("[data-lang-switch]");
  if (!sw) return;
  var btn = sw.querySelector(".lang-btn");
  var menu = sw.querySelector(".lang-menu");
  if (!btn || !menu) return;

  sw.classList.add("js");
  btn.hidden = false;
  menu.hidden = true;
  btn.setAttribute("aria-expanded", "false");

  function setOpen(open) {
    menu.hidden = !open;
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  }

  btn.addEventListener("click", function () {
    setOpen(menu.hidden);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !menu.hidden) {
      setOpen(false);
      btn.focus();
    }
  });

  document.addEventListener("click", function (e) {
    if (!sw.contains(e.target)) setOpen(false);
  });

  sw.addEventListener("focusout", function (e) {
    if (!sw.contains(e.relatedTarget)) setOpen(false);
  });
})();
