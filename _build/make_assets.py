#!/usr/bin/env python3
"""Extract base CSS verbatim from index.html, append subpage component styles,
write assets/css/site.css and a null-safe assets/js/site.js."""
import os, re

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css_path = os.path.join(PROJECT, "assets", "css", "site.css")
m = re.search(r'<style>([\s\S]*?)</style>', open(os.path.join(PROJECT, "index.html"), encoding="utf-8").read())
if m:
    base_css = m.group(1).strip()                      # first run: inline style still in index.html
else:
    full = open(css_path, encoding="utf-8").read()     # later runs: recover base from existing site.css
    base_css = full.split("\n/* ===========", 1)[0].strip()

# Gate scroll-reveal behind a JS-added class so content is NEVER hidden without JS.
# Collapse any prefixes left by earlier runs first, so re-running stays idempotent.
base_css = re.sub(r"(?:html\.js-anim )+\.rv", ".rv", base_css)
base_css = base_css.replace(
    ".rv{opacity:0;transform:translateY(22px);transition:opacity .6s ease, transform .6s ease}",
    "html.js-anim .rv{opacity:0;transform:translateY(22px);transition:opacity .6s ease, transform .6s ease}")
base_css = base_css.replace(
    ".rv.in{opacity:1;transform:none}",
    "html.js-anim .rv.in{opacity:1;transform:none}")

COMPONENTS = r"""
/* =========================================================
   Components added for interior (sub) pages — same system
   ========================================================= */
.subhero{background:
    radial-gradient(900px 520px at 88% -10%, var(--teal-soft) 0%, transparent 60%),
    linear-gradient(180deg,var(--paper) 0%, var(--teal-mist) 100%);
  border-bottom:1px solid var(--line)}
.subhero .wrap{padding:54px 28px 50px}
.breadcrumb{font-size:13px;color:var(--muted);margin-bottom:12px;display:flex;gap:8px;flex-wrap:wrap}
.breadcrumb a:hover{color:var(--teal)}
.breadcrumb span.sep{opacity:.5}
.breadcrumb .here{color:var(--ink);font-weight:600}
.subhero h1{font-size:clamp(32px,4vw,50px);margin:10px 0 16px;max-width:22ch}
.subhero h1 em{font-style:italic;color:var(--teal)}
.subhero .lede{margin-bottom:0}

.pagebody{padding:74px 0}
.pagebody.tight{padding:60px 0}
.prose{max-width:760px}
.prose.wide{max-width:1000px}
.prose h2{font-family:var(--display);font-weight:560;font-size:clamp(24px,2.6vw,32px);margin:36px 0 14px;letter-spacing:-.01em}
.prose h2:first-child{margin-top:0}
.prose h3{font-family:var(--display);font-weight:560;font-size:21px;margin:26px 0 10px}
.prose p{margin-bottom:16px;color:#36525C}
.prose ul{margin:0 0 18px;padding-left:0;list-style:none}
.prose ul li{position:relative;padding-left:28px;margin-bottom:10px;color:#36525C}
.prose ul li::before{content:"";position:absolute;left:4px;top:10px;width:9px;height:9px;border-radius:50%;background:var(--amber)}
.prose a.inline{color:var(--teal);font-weight:600;text-decoration:underline;text-underline-offset:2px}
.prose a.inline:hover{color:var(--amber-deep)}
.lead-para{font-size:19px;color:var(--ink);font-family:var(--display);line-height:1.5;margin-bottom:22px}

.split{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:start}
.split .media img{border-radius:20px;box-shadow:var(--shadow);width:100%}
.split.rev{grid-template-columns:.9fr 1.1fr}

.svc-list{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:4px}
.svc-list .item{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:26px 24px;transition:transform .2s,box-shadow .2s}
.svc-list .item:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.svc-list .item .num{font-family:var(--display);font-size:13px;font-weight:700;color:var(--amber);letter-spacing:.12em}
.svc-list .item h3{font-family:var(--display);font-size:19px;margin:6px 0 8px;color:var(--ink)}
.svc-list .item p{font-size:14.5px;color:var(--muted);margin:0}

.figrow{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:28px 0}
.figrow figure{margin:0}
.figrow img{border-radius:16px;box-shadow:var(--shadow);width:100%;aspect-ratio:4/3;object-fit:cover;background:var(--teal-soft)}
.figrow figcaption{font-size:13px;color:var(--muted);margin-top:10px;line-height:1.5}

.steps{counter-reset:step;display:grid;gap:12px;margin:18px 0}
.steps li{list-style:none;position:relative;padding:18px 20px 18px 66px;background:#fff;border:1px solid var(--line);border-radius:14px;color:#36525C}
.steps li::before{counter-increment:step;content:counter(step);position:absolute;left:18px;top:16px;width:34px;height:34px;border-radius:50%;background:var(--teal-soft);color:var(--teal);font-weight:800;display:grid;place-items:center;font-size:15px}

.faq-group{max-width:840px}
.faq-group .glabel{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--teal);margin:34px 0 14px}
.faq-group .glabel:first-child{margin-top:0}
details.qa{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:12px;overflow:hidden;transition:box-shadow .2s}
details.qa[open]{box-shadow:var(--shadow)}
details.qa summary{list-style:none;cursor:pointer;padding:20px 56px 20px 22px;font-weight:600;font-size:16.5px;color:var(--ink);position:relative}
details.qa summary::-webkit-details-marker{display:none}
details.qa summary::after{content:"+";position:absolute;right:22px;top:50%;transform:translateY(-50%);font-size:26px;font-weight:300;color:var(--teal);transition:transform .2s}
details.qa[open] summary::after{content:"\2013"}
details.qa .a{padding:2px 22px 20px;color:#36525C}
details.qa .a p{margin-bottom:10px}
details.qa .a ul{margin:4px 0 8px;padding-left:0;list-style:none}
details.qa .a ul li{position:relative;padding-left:22px;margin-bottom:8px}
details.qa .a ul li::before{content:"";position:absolute;left:3px;top:10px;width:7px;height:7px;border-radius:50%;background:var(--amber)}

.gallery{columns:3;column-gap:18px;margin-top:8px}
.gallery figure{break-inside:avoid;margin:0 0 18px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:10px;box-shadow:0 12px 32px -24px rgba(14,58,71,.5)}
.gallery img{border-radius:8px;width:100%}

.ins-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:6px 0}
.ins-grid .ins{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px 20px;text-align:center;color:var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;min-height:140px;transition:transform .2s,box-shadow .2s}
.ins-grid .ins:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.ins-grid .ins img{max-height:50px;max-width:170px;width:auto;object-fit:contain}
.ins-grid .ins .insname{font-size:12.5px;color:var(--muted);font-weight:600;line-height:1.3}
.ins-grid .ins .ic{width:42px;height:42px;border-radius:12px;background:var(--teal-soft);display:grid;place-items:center;color:var(--teal)}
.ins-note{background:var(--teal-soft);border:1px solid var(--line);border-radius:16px;padding:22px 24px;color:var(--ink);margin-top:20px;line-height:1.6}
.mt0{margin-top:0}

/* brand logo now carries the wordmark — show it a touch larger, no adjacent text */
.brand img{height:58px;width:auto}
footer .fbrand img{height:54px;width:auto}
@media (max-width:640px){ .brand img{height:50px} }

/* ---- accessibility / Lighthouse fixes ---- */
/* darker amber so white button text meets WCAG AA (was 2.97:1) */
.btn-amber{background:#9A6A14;box-shadow:0 10px 26px -10px rgba(154,106,20,.55)}
.btn-amber:hover{background:#7F560F}
/* darker amber for small "Learn more" links so they meet AA on white (was 4.0:1) */
.svc a{color:#8A5E12}
/* smaller trademark / registered marks */
.tm{font-size:.52em;vertical-align:super;line-height:0;font-weight:400;margin-left:1px}
h1 .tm,h2 .tm{font-size:.42em}
/* images carry width/height attributes now; keep them responsive */
img{height:auto}
/* insurer cards that show two logos */
.ins-grid .ins .logos{display:flex;align-items:center;justify-content:center;gap:16px;flex-wrap:wrap}
.ins-grid .ins .logos img{max-width:120px}
/* text testimonials */
.rev-grid{columns:3;column-gap:18px}
.rev{break-inside:avoid;margin:0 0 18px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 22px 18px}
.rev .stars{font-size:14px;display:block;margin-bottom:8px}
.rev blockquote{margin:0;color:#36525C;font-size:15px;line-height:1.6}
.rev figcaption{margin-top:12px;font-size:13px;font-weight:700;color:var(--ink)}
@media (max-width:1020px){ .rev-grid{columns:2} }
@media (max-width:640px){ .rev-grid{columns:1} }
/* footer legal links */
.legal a{text-decoration:underline;text-underline-offset:2px}
.legal a:hover{color:#fff}
/* team section (6 slots from _build/team.json) */
.team{background:var(--teal-mist)}
.team-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.member{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column}
.member .photo{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:center top;display:block;background:var(--teal-soft)}
.member .photo.empty{display:grid;place-items:center;color:#8FAFBA}
.member .body{padding:20px 22px 24px}
.member .role{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--teal)}
.member h3{font-size:20px;margin:6px 0 8px}
.member p{font-size:14.5px;color:var(--muted)}
.member.empty{border-style:dashed}
.member.empty h3{color:var(--muted)}
@media (max-width:1020px){ .team-grid{grid-template-columns:repeat(2,1fr)} }
@media (max-width:640px){ .team-grid{grid-template-columns:1fr} }
/* skip link + visible keyboard focus */
.skip-link{position:absolute;left:12px;top:-60px;z-index:100;background:var(--ink);color:#fff;padding:10px 16px;border-radius:10px;font-weight:700;transition:top .15s}
.skip-link:focus{top:12px}
a:focus-visible,button:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:3px solid var(--amber-deep);outline-offset:3px;border-radius:6px}
.scopeband a:focus-visible,.book a:focus-visible,footer a:focus-visible,footer [tabindex]:focus-visible,.topbar a:focus-visible{outline-color:#F3C878}
main:focus{outline:none}
/* small print */
.fine{font-size:12.5px;color:#9FC2CE;margin-top:12px;line-height:1.5;max-width:240px}
.ins-updated{font-size:13px;color:var(--muted);margin-top:14px}
/* emergency page */
.em-alert{background:#FFF4E5;border:1px solid #E9BE78;border-radius:16px;padding:18px 22px;margin:0 0 22px;color:var(--ink);line-height:1.6}
.em-alert strong{display:block;font-size:16.5px;margin-bottom:4px}
.em-call{display:flex;gap:14px;flex-wrap:wrap;margin:0 0 30px}
/* keep the header CTA on one line on phones */
.nav-cta .btn{white-space:nowrap}
@media (max-width:480px){ .nav-cta .btn{font-size:14px;padding:11px 16px} .nav-cta{gap:8px} }
.nowrap{white-space:nowrap}
/* template placeholders — fill in before launch */
.tbd{background:#FFF6E0;border:1.5px dashed #C9962E;border-radius:6px;padding:1px 6px;color:#5C4510;font-weight:600}
.tbd-banner{background:#FFF6E0;border:1.5px dashed #C9962E;border-radius:14px;padding:16px 20px;margin:0 0 22px;color:#5C4510;line-height:1.6}
.tbd-banner strong{display:block;margin-bottom:2px}
/* lighter footer legal text for contrast on the dark footer */
.legal{color:#9FC2CE}
/* footer column headings are now <h2> (keep the small uppercase look) */
footer h2{color:#fff;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px;font-family:var(--body)}
/* map facade: click-to-load keeps the map but avoids third-party cookies on page load */
.mapfacade{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;height:220px;
  border-radius:14px;cursor:pointer;text-align:center;color:#EAF5F9;border:1px solid rgba(255,255,255,.14);
  background:linear-gradient(135deg,#124a5a,#0E3A47);transition:border-color .2s}
.mapfacade:hover{border-color:rgba(143,211,232,.6)}
.mapfacade strong{font-weight:700;font-size:14.5px}
.mapfacade small{color:#8FB9C8;font-size:12.5px;max-width:200px}
.mapfacade svg{opacity:.85}

@media (max-width:1020px){
  .split,.split.rev{grid-template-columns:1fr;gap:40px}
  .gallery{columns:2}
}
@media (max-width:760px){
  .svc-list{grid-template-columns:1fr}
  .figrow{grid-template-columns:1fr}
  .ins-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:480px){
  .gallery{columns:1}
  .ins-grid{grid-template-columns:1fr}
}
"""

os.makedirs(os.path.join(PROJECT, "assets", "css"), exist_ok=True)
os.makedirs(os.path.join(PROJECT, "assets", "js"), exist_ok=True)
with open(os.path.join(PROJECT, "assets", "css", "site.css"), "w", encoding="utf-8") as f:
    fonts_css = os.path.join(PROJECT, "assets", "fonts", "fonts.css")
    font_faces = open(fonts_css, encoding="utf-8").read() if os.path.exists(fonts_css) else ""
    f.write(base_css + "\n" + COMPONENTS + "\n" + font_faces)

JS = """// Tichy Dental — shared site behaviour (null-safe across all pages)
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
"""
with open(os.path.join(PROJECT, "assets", "js", "site.js"), "w", encoding="utf-8") as f:
    f.write(JS)

print("base css lines:", base_css.count("\n")+1)
print("site.css bytes:", os.path.getsize(os.path.join(PROJECT,'assets','css','site.css')))
print("site.js bytes:", os.path.getsize(os.path.join(PROJECT,'assets','js','site.js')))
