// Bottom-sheet peek — vanilla port of the design prototype's interaction
// Supports multiple peeks per page: give each sheet a data-peek="key" and
// each trigger a matching data-peek-open="key". A trigger/sheet pair with no
// key (data-peek-open, data-peek="") falls back to the page's only sheet.
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    var backdrop = document.querySelector('[data-peek-backdrop]');
    var sheets = document.querySelectorAll('[data-peek]');
    if (!backdrop || !sheets.length) return;

    var current = null;

    function open(sheet) {
      if (!sheet) return;
      if (current && current !== sheet) current.classList.remove('open');
      sheet.classList.add('open');
      backdrop.classList.add('open');
      current = sheet;
    }
    function close() {
      if (current) current.classList.remove('open');
      backdrop.classList.remove('open');
      current = null;
    }

    document.querySelectorAll('[data-peek-open]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        var key = el.getAttribute('data-peek-open');
        var target = key ? document.querySelector('[data-peek="' + key + '"]') : sheets[0];
        open(target);
      });
    });
    backdrop.addEventListener('click', close);
    sheets.forEach(function (sheet) {
      sheet.querySelectorAll('[data-peek-close]').forEach(function (el) {
        el.addEventListener('click', close);
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  });
})();
