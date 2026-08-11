// Luke 12 bottom-sheet peek — vanilla port of the design prototype's interaction
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    var sheet = document.querySelector('[data-peek]');
    var backdrop = document.querySelector('[data-peek-backdrop]');
    if (!sheet || !backdrop) return;

    function open() { sheet.classList.add('open'); backdrop.classList.add('open'); }
    function close() { sheet.classList.remove('open'); backdrop.classList.remove('open'); }

    document.querySelectorAll('[data-peek-open]').forEach(function (el) {
      el.addEventListener('click', function (e) { e.preventDefault(); open(); });
    });
    backdrop.addEventListener('click', close);
    sheet.querySelectorAll('[data-peek-close]').forEach(function (el) {
      el.addEventListener('click', close);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  });
})();
