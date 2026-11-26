/* v3 shared language switcher — progressive-enhancement disclosure.
   With no JS the language links stay visible inline; with JS (html.js,
   set inline in <head> before first paint) the CSS collapses them behind
   the globe button. This script only wires the open/close interaction —
   the initial collapsed state lives entirely in CSS so nothing shifts
   after first paint. One switcher per page. */
(function () {
  var sw = document.querySelector("[data-lang-switch]");
  if (!sw) return;
  var btn = sw.querySelector(".lang-btn");
  var menu = sw.querySelector(".lang-menu");
  if (!btn || !menu) return;

  function setOpen(open) {
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  }

  btn.addEventListener("click", function () {
    setOpen(btn.getAttribute("aria-expanded") !== "true");
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && btn.getAttribute("aria-expanded") === "true") {
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
