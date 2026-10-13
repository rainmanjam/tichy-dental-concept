// Tichy Dental — shared site behaviour (null-safe across all pages)
(function () {
  // Enable scroll-reveal animation only when JS is present (content stays visible otherwise)
  document.documentElement.classList.add('js-anim');
  var header = document.getElementById('siteHeader');
  if (header) {
    var ticking = false;
    addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        header.classList.toggle('scrolled', scrollY > 8);
        ticking = false;
      });
    }, { passive: true });
  }
  var nav = document.getElementById('mainNav');
  var burger = document.getElementById('hamburger');
  if (nav && burger) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    burger.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { setMenu(false); burger.focus(); }
    });
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.14 });
    document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.rv').forEach(function (el) { el.classList.add('in'); });
  }
  // Click-to-load map (avoids third-party cookies until the visitor asks for the map)
  var mf = document.getElementById('mapFacade');
  if (mf) {
    var loadMap = function () {
      var f = document.createElement('iframe');
      f.src = mf.getAttribute('data-src');
      f.title = 'Map to Tichy Dental, 18607 Willamette Dr., West Linn, OR';
      f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      f.style.cssText = 'width:100%;height:220px;border:0;border-radius:14px';
      mf.replaceWith(f);
    };
    mf.addEventListener('click', loadMap);
    mf.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); loadMap(); }
    });
  }
})();
