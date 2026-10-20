#!/usr/bin/env python3
"""Generate the 9-page Tichy Dental redesign (index.html + 8 subpages) from the
concept template design system. Shared chrome is defined once to prevent drift."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
page_images = json.load(open(os.path.join(HERE, "page_images.json")))

# ---- assets ----
LOGO     = "assets/img/f9995c_cca9f03d99c441ec81741650af77e7dd.jpg"   # full-colour primary logo (navy/gray)
HERO     = "assets/img/f9995c_5be93b1d9ba34f959aafca2070564038.jpg"   # real waiting-room office photo
SCOPE    = "assets/img/f9995c_fd8c251dab4d4b16b397c91b6fc6f6e5.jpg"
PORTRAIT = "assets/img/f9995c_119eb82f2552473c929929d883e91d19.jpg"
SKI      = "assets/img/f9995c_edc524d14c1f4b72919e09828f1bd65d.jpg"
CEREC1   = "assets/img/f9995c_e64c8f0bd6694827baccabe86364e652.jpg"
CEREC2   = "assets/img/f9995c_05ddc86fd8204f06ad9e614b937cfe92.jpg"

# ---- outbound links (kept external, exactly like the template) ----
APPT  = "https://tch.identalcloud.com/TichyDental/Patient/_practice/1/Appointment"
REG   = "https://tch.identalcloud.com/TichyDental/Patient/_practice/1/Registration"
LOGIN = "https://tch.identalcloud.com/TichyDental/Patient/_practice/1"
MAPS  = "https://www.google.com/maps/place/Tichy+Dental+LLC/@45.3912526,-122.6463701,15z/data=!4m5!3m4!1s0x0:0xe9531c70db6f1a0b!8m2!3d45.3912526!4d-122.6463701"
FB    = "https://www.facebook.com/TichyDental/"
IG    = "https://www.instagram.com/tichydental/"
TW    = "https://twitter.com/MichaelTichyDMD"
YELP  = "https://www.yelp.com/search?find_desc=Tichy+Dental&find_loc=West+Linn%2C+OR"
CLARITY = "https://www.solventum.com/en-us/home/"   # maker of 3M Clarity Aligners (3M Oral Care is now Solventum)
ALIGN_PAGE = "clarity-aligners.html"

# ---- launch / profile settings (edit these) ----
LIVE = False                  # False = GitHub Pages preview (noindex, assets from GitHub). True = production on tichydental.com
YELP_URL = "https://www.yelp.com/biz/tichy-dental-west-linn"
GOOGLE_REVIEW_URL = "https://search.google.com/local/writereview?placeid=ChIJlUWZp4pzlVQRCxpv23AcU-k"   # opens Google's review form
NPP_URL = "notice-of-privacy-practices.html"   # HIPAA Notice of Privacy Practices (template page — complete in Wix)
PORTAL_PRIVACY_URL = "https://tch.identalcloud.com/TichyDental/Patient/_practice/1/PrivacyPolicy"   # practice's patient-portal privacy policy
SHOW_EMPTY_TEAM_SLOTS = False # True shows "coming soon" cards for unfilled team slots
GOOGLE_CID_URL = "https://maps.google.com/?cid=" + str(int("e9531c70db6f1a0b", 16))
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=Tichy+Dental+LLC,+18607+Willamette+Dr,+West+Linn,+OR+97068"
if YELP_URL:
    YELP = YELP_URL
GREVIEW = GOOGLE_REVIEW_URL or MAPS
JADA  = "https://jada.ada.org/article/S0002-8177(14)63733-8/fulltext"
MICRO1 = "https://www.oralhealthgroup.com/features/the-value-of-the-dental-operating-microscope-in-restorative-dentistry-axiomatic-or-absurd/"
MICRO2 = "https://www.globalsurgical.com/microscope-benefits.html"
MICRO3 = "https://pubmed.ncbi.nlm.nih.gov/10649948/"

def testimonial_shots():
    out = []
    for im in page_images["testimonials"]:
        f = im["file"]; alt = im["alt"]
        if alt in ("Facebook", "Instagram", "Twitter"): continue
        if f == LOGO: continue
        if "Screen Shot" in alt or "Screenshot" in alt:
            out.append(f)
    return out
SHOTS = testimonial_shots()

TOPBAR = '''<!-- top utility bar -->
<div class="topbar">
  <div class="wrap">
    <div class="left">
      <a href="tel:5036353588"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3A19.5 19.5 0 0 1 5.2 13 19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c1 .3 1.9.5 2.9.7a2 2 0 0 1 1.6 2z"/></svg> (503) 635-3588</a>
      <a class="addr" href="''' + MAPS + '''" target="_blank" rel="noopener"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg> 18607 Willamette Dr., West Linn, OR 97068</a>
    </div>
    <span class="hours">Mon–Thu 8am–5pm · Fri Closed</span>
  </div>
</div>
'''

def header(is_home):
    svc  = "#services" if is_home else "index.html#services"
    abt  = "#about"    if is_home else "index.html#about"
    book = "#book"     if is_home else "index.html#book"
    return '''<!-- header -->
<header class="site" id="siteHeader">
  <div class="wrap navrow">
    <a class="brand" href="index.html" aria-label="Tichy Dental — home">
      <img src="''' + LOGO + '''" alt="Tichy Dental — cosmetic, family &amp; emergency dentistry">
    </a>
    <nav class="main" id="mainNav">
      <div>
        <a class="top" href="''' + svc + '''">Our Services ▾</a>
        <div class="dd">
          <span class="sub">General</span>
          <a href="general-dentistry.html">General &amp; Family Dentistry</a>
          <a href="emergency-dentist.html">Emergency Dental Care</a>
          <span class="sub">Cosmetic</span>
          <a href="clarity-aligners.html">3M Clarity Aligners</a>
          <span class="sub">Restorative</span>
          <a href="cerec-crowns.html">CEREC Same-Day Crowns</a>
          <span class="sub">Advanced Technology</span>
          <a href="microscopically-assisted-dentistry.html">Microscopic Dentistry</a>
        </div>
      </div>
      <div>
        <a class="top" href="''' + abt + '''">About ▾</a>
        <div class="dd">
          <a href="meet-dr-tichy.html">Meet Dr. Tichy</a>
          <a href="meet-dr-tichy.html#team">Our Team</a>
          <a href="testimonials.html">Patient Reviews</a>
        </div>
      </div>
      <div>
        <a class="top" href="''' + book + '''">Patient Info ▾</a>
        <div class="dd">
          <a href="''' + REG + '''" target="_blank" rel="noopener">New Patient Forms</a>
          <a href="insurance.html">Insurance &amp; Billing</a>
          <a href="faq.html">FAQ</a>
        </div>
      </div>
      <div><a class="top" href="#contact">Contact</a></div>
    </nav>
    <div class="nav-cta">
      <a class="login-link" href="''' + LOGIN + '''" target="_blank" rel="noopener">Patient Login</a>
      <a class="btn btn-amber" href="''' + APPT + '''" target="_blank" rel="noopener">Request Appointment</a>
      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-controls="mainNav" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
'''

def book_band():
    return '''<!-- booking band -->
<section class="book" id="book">
  <div class="wrap rv">
    <span class="eyebrow" style="color:#F3C878">Ready When You Are</span>
    <h2>Request your appointment online</h2>
    <p>Request a visit, register as a new patient, and sign consent forms — all through our secure patient portal, on your schedule. Our front desk will follow up to confirm your appointment time.</p>
    <div class="row">
      <a class="btn btn-amber" href="''' + APPT + '''" target="_blank" rel="noopener">Request Appointment</a>
      <a class="btn btn-ghost" href="''' + REG + '''" target="_blank" rel="noopener">New Patient Forms</a>
      <a class="btn btn-ghost" href="''' + LOGIN + '''" target="_blank" rel="noopener">Patient Login</a>
    </div>
    <div class="note">Prefer to call? We'd love to hear from you: (503) 635-3588</div>
  </div>
</section>
'''

FOOTER = '''<!-- footer -->
<footer id="contact">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="fbrand">
          <img src="''' + LOGO + '''" alt="Tichy Dental logo">
        </div>
        <p class="mission">Gentle, microscope-assisted dentistry for families in West Linn, Lake Oswego, Oregon City, and Marylhurst.</p>
        <div class="socials">
          <a href="''' + FB + '''" target="_blank" rel="noopener" aria-label="Facebook"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.7c0-.9.3-1.6 1.7-1.6h1.5V4.2c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.7H7.8V14h2.7v8z"/></svg></a>
          <a href="''' + IG + '''" target="_blank" rel="noopener" aria-label="Instagram"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".8" fill="currentColor"/></svg></a>
          <a href="''' + TW + '''" target="_blank" rel="noopener" aria-label="Twitter / X"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2h3.3l-7.2 8.3L22.8 22h-6.6l-5.2-6.8L5 22H1.7l7.7-8.9L1.5 2h6.8l4.7 6.2zm-1.2 18h1.8L7.3 3.9H5.4z"/></svg></a>
        </div>
      </div>
      <div>
        <h2>Quick Links</h2>
        <ul>
          <li><a href="general-dentistry.html">Our Services</a></li>
          <li><a href="emergency-dentist.html">Dental Emergencies</a></li>
          <li><a href="meet-dr-tichy.html">About Us</a></li>
          <li><a href="insurance.html">Insurance</a></li>
          <li><a href="testimonials.html">Testimonials</a></li>
          <li><a href="''' + LOGIN + '''" target="_blank" rel="noopener">Patient Portal</a></li>
        </ul>
      </div>
      <div>
        <h2>Visit Us</h2>
        <div class="nap">
          <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg><span>18607 Willamette Dr.<br>West Linn, OR 97068<br><a href="''' + DIRECTIONS + '''" target="_blank" rel="noopener">Get directions &rarr;</a></span></div>
          <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3A19.5 19.5 0 0 1 5.2 13 19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c1 .3 1.9.5 2.9.7a2 2 0 0 1 1.6 2z"/></svg><a href="tel:5036353588">(503) 635-3588</a></div>
          <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg><a href="mailto:info@tichydental.com">info@tichydental.com</a></div>
        </div>
        <div class="hourstable">
          <div><span>Mon – Thu</span><span>8am – 5pm</span></div>
          <div><span>Friday</span><span class="closed">Closed</span></div>
          <div><span>Sat – Sun</span><span class="closed">Closed</span></div>
        </div>
        <p class="fine">Please don't email health information. Use the secure patient portal instead.</p>
      </div>
      <div class="fmap">
        <h2>Find Us</h2>
        <div class="mapfacade" id="mapFacade" role="button" tabindex="0"
             data-src="https://www.google.com/maps?q=Tichy+Dental+LLC,+18607+Willamette+Dr,+West+Linn,+OR+97068&output=embed">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <strong>Load interactive map</strong>
          <small>18607 Willamette Dr., West Linn, OR 97068</small>
        </div>
      </div>
    </div>
    <div class="legal">
      <span>© 2026 Tichy Dental LLC · West Linn, Oregon</span>
      <span><a href="privacy.html">Privacy Policy</a> · <a href="notice-of-privacy-practices.html">Notice of Privacy Practices</a> · <a href="accessibility.html">Accessibility</a></span>
    </div>
  </div>
</footer>
'''

def shell(title, desc, body):
    # wrap everything between the header and the footer in a single <main> landmark
    body = body.replace("</header>", "</header>\n<main id=\"main\" tabindex=\"-1\">", 1)
    body = body.replace("<!-- footer -->", "</main>\n<!-- footer -->", 1)
    return ('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + title + '''</title>
<meta name="description" content="''' + desc + '''">
<link rel="preload" href="assets/fonts/figtree-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/fraunces-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/fraunces-italic-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
''' + body + '''
<script src="assets/js/site.js"></script>
</body>
</html>
''')

def subhero(eyebrow, h1, lede, here):
    return '''<div class="subhero">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span class="sep">/</span><span class="here">''' + here + '''</span></nav>
    <span class="eyebrow">''' + eyebrow + '''</span>
    <h1>''' + h1 + '''</h1>
    <p class="lede">''' + lede + '''</p>
  </div>
</div>
'''

PAGES = {}

# ---------------- HOME ----------------
home_body = TOPBAR + header(True) + '''
<!-- hero -->
<div class="hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">West Linn, Oregon <span class="dot">·</span> Microscope-Assisted Dentistry</span>
      <h1>Family &amp; cosmetic dentistry, <em>seen up close.</em></h1>
      <p class="lede">Dr. Michael Tichy treats every patient under a dental operating microscope — precise, conservative, comfortable care for the whole family, from routine cleanings to same-day CEREC crowns and 3M Clarity clear aligners.</p>
      <div class="cta-row">
        <a class="btn btn-amber" href="''' + APPT + '''" target="_blank" rel="noopener">Request Appointment <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-ghost" href="#services">Explore Our Services</a>
      </div>
      <div class="rating"><span class="stars" aria-hidden="true">★★★★★</span> Rated 5.0 on Google by local families</div>
    </div>
    <div class="hero-visual rv">
      <img class="office" loading="lazy" src="''' + HERO + '''" alt="Tichy Dental office in West Linn, Oregon">
      <div class="chip"><b>1%</b><span>of general dentists use an operating microscope for every procedure. Dr. Tichy is one of them.</span></div>
      <div class="lens" title="Through the scope">
        <img loading="lazy" src="''' + SCOPE + '''" alt="Dr. Michael Tichy practicing with a dental operating microscope">
      </div>
      <span class="lens-tag">Through the scope ↗</span>
    </div>
  </div>
</div>
<!-- trust bar -->
<div class="trust">
  <div class="wrap">
    <span class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2.4 4.9 5.4.8-3.9 3.8.9 5.4L12 14.3 7.2 16.9l.9-5.4L4.2 7.7l5.4-.8z"/></svg> 5.0 Stars on Google</span>
    <span class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.1V12a10 10 0 1 1-5.9-9.1"/><path d="M22 4L12 14l-3-3"/></svg> 3M Clarity Aligner Provider</span>
    <span class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> CEREC Same-Day Crowns</span>
    <span class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/></svg> OHSU-Trained, D.M.D.</span>
    <span class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg> Cosmetic · Family · Emergency</span>
  </div>
</div>
<!-- services -->
<section class="services" id="services">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">What We Do <span class="dot">·</span> Care For The Whole Family</span>
      <h2>Our specialized dental services</h2>
      <p class="lede">From routine checkups to advanced restorations — every exam and procedure performed under the microscope.</p>
    </div>
    <div class="svc-grid">
      <div class="svc rv">
        <div class="icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2a7 7 0 0 1 7 7c0 3-1.5 4-2 6s-.5 7-2.5 7S13 17 12 17s-.5 5-2.5 5S8 17 7 15s-2-3-2-6a7 7 0 0 1 7-7z"/></svg></div>
        <h3>CEREC Same-Day Crowns</h3>
        <p>A precision-milled ceramic crown designed, made, and placed in a single visit — no temporaries, no second appointment.</p>
        <a href="cerec-crowns.html">Learn more →</a>
      </div>
      <div class="svc rv">
        <div class="icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 15c2-1.5 4-2 9-2s7 .5 9 2"/><path d="M3 9c2 1.5 4 2 9 2s7-.5 9-2"/><rect x="2" y="6" width="20" height="12" rx="6"/></svg></div>
        <h3>3M Clarity Aligners</h3>
        <p>Straighten your smile discreetly with nearly invisible 3M Clarity clear aligners, scanned digitally and checked under the scope at every step.</p>
        <a href="clarity-aligners.html">Learn more →</a>
      </div>
      <div class="svc rv">
        <div class="icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/><path d="M11 8v6M8 11h6"/></svg></div>
        <h3>Microscopic Dentistry</h3>
        <p>Greater magnification means earlier detection, smaller fillings, and more of your healthy tooth preserved.</p>
        <a href="microscopically-assisted-dentistry.html">Learn more →</a>
      </div>
      <div class="svc rv">
        <div class="icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17 8a5 5 0 1 0-10 0c0 5-3 6-3 9a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3c0-3-3-4-3-9z" transform="translate(0 -1)"/><path d="M9 21v-3a3 3 0 0 1 6 0v3"/></svg></div>
        <h3>General &amp; Family Care</h3>
        <p>Gentle cleanings, exams, and preventive care for adults and children — with your exam shown live on overhead TVs.</p>
        <a href="general-dentistry.html">Learn more →</a>
      </div>
    </div>
  </div>
</section>
<!-- microscope band -->
<section class="scopeband">
  <div class="wrap">
    <div class="scope-photo rv">
      <div class="ring"><img loading="lazy" src="''' + SCOPE + '''" alt="The dental operating microscope at Tichy Dental in West Linn"></div>
      <div class="cross"></div>
    </div>
    <div class="rv">
      <span class="eyebrow">The Tichy Difference</span>
      <h2>Every procedure. Under the microscope.</h2>
      <p>Most dentists work with loupes. Dr. Tichy belongs to the rare group of general dentists who perform every exam and procedure with a dental operating microscope — the gold standard of precision care.</p>
      <p>More magnification means decay is caught earlier, treatment stays conservative, and more of your healthy tooth is preserved. A camera on the scope streams to ceiling-mounted TVs, so you watch your own exam in real time while Dr. Tichy explains what he sees.</p>
      <div class="mag">
        <div class="m hot"><b>1%</b><span>Of general dentists scope every procedure</span></div>
        <div class="m"><b>LED</b><span>Built-in microscope light</span></div>
        <div class="m"><b>Live</b><span>Overhead exam TVs</span></div>
      </div>
      <a class="btn btn-amber" href="microscopically-assisted-dentistry.html" style="margin-top:26px">How the microscope works →</a>
    </div>
  </div>
</section>
<!-- about -->
<section class="about" id="about">
  <div class="wrap">
    <div class="about-photo rv">
      <img class="portrait" loading="lazy" src="''' + PORTRAIT + '''" alt="Dr. Michael Tichy, D.M.D. — dentist in West Linn, Oregon">
      <img class="ski" loading="lazy" src="''' + SKI + '''" alt="Dr. Michael Tichy alpine ski racing">
    </div>
    <div class="rv">
      <span class="eyebrow">Meet Your Dentist <span class="dot">·</span> Dr. Michael Tichy, D.M.D.</span>
      <h2>Precision has always been the job.</h2>
      <p>Before dentistry, Dr. Tichy competed in professional alpine ski racing — collecting national and international titles where success is measured in hundredths of a second. Today that same discipline shows up in a different arena: evidence-based, microscope-assisted dentistry.</p>
      <p>A graduate of Oregon Health &amp; Science University and an Oregonian of twenty years, Dr. Tichy is a husband and father of two who loves treating adults and kids alike — and teaching families how oral health connects to whole-body health.</p>
      <div class="pull">"Less invasive, more comfortable, and honest about what you actually need — that's the promise of the microscope."</div>
      <a class="btn btn-dark" href="meet-dr-tichy.html#team">Meet Dr. Tichy &amp; the Team</a>
    </div>
  </div>
</section>
<!-- reviews -->
<section class="reviews" id="reviews">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:100%;text-align:center;margin-left:auto;margin-right:auto">
      <span class="eyebrow">Patient Stories</span>
      <h2>What our West Linn patients are saying</h2>
    </div>
    <div class="featured-quote rv">
      <div class="stars">★★★★★</div>
      <p>"Dr. Tichy is an incredibly personable and warm dentist. He goes the extra mile to take great care of his patients and to make certain that they are both comfortable and that they understand their care. I even entrust him with my mom."</p>
      <cite>— Christopher B., Google review</cite>
    </div>
    <div class="plat-grid">
      <div class="plat google rv"><div class="logo">G</div><h3>Google Reviews</h3><div class="stars" role="img" aria-label="Rated 5 out of 5 on Google">★★★★★</div><div class="count">5.0 from 150+ Google reviews</div>
        <div class="links"><a class="read" href="''' + MAPS + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + GREVIEW + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
      <div class="plat yelp rv"><div class="logo">Y</div><h3>Yelp</h3><div class="count">See what neighbors say</div>
        <div class="links"><a class="read" href="''' + YELP + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + YELP + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
      <div class="plat facebook rv"><div class="logo">f</div><h3>Facebook</h3><div class="count">Recommendations from our community</div>
        <div class="links"><a class="read" href="''' + FB + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + FB + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
    </div>
    <div style="text-align:center;margin-top:34px"><a class="btn btn-ghost" href="testimonials.html">See all patient testimonials →</a></div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["index.html"] = shell(
    "West Linn Dentist | CEREC Crowns &amp; Clear Aligners | Tichy Dental",
    "Gentle, microscope-assisted dentistry in West Linn, OR. CEREC same-day crowns, 3M Clarity clear aligners, and family care. Book online today.",
    home_body)

# ---------------- GENERAL DENTISTRY ----------------
svc_items = [
 ("01","Comprehensive Dental Exams","A ceiling-mounted HD TV connected to the dental microscope lets patients experience exactly what Dr. Tichy observes during the examination.", None),
 ("02","Dental Fillings / Restorations","Dr. Tichy offers mercury-free fillings. Watch overhead as he restores teeth with tooth-colored composite restorative material.", None),
 ("03","Emergency Dentistry","We provide emergency dental care — here to lessen your dental pain or triage true emergency accidents that may require more definitive treatment.", "emergency-dentist.html"),
 ("04","Crown, Bridge &amp; CEREC","Dr. Tichy proudly offers same-day crowns. With CEREC we provide a wide variety of crowns — single-unit to multi-tooth bridges that restore edentulous areas of the arch.", "cerec-crowns.html"),
 ("05","Routine &amp; Surgical Extractions","Extractions can be stressful. Dr. Tichy and his staff help you through it, performing most extractions in-house and referring complex cases best suited for specialists.", None),
 ("06","Dental Hygiene","Regular prophylaxis cleanings help prevent gingivitis, and deeper scaling and root planing help eliminate periodontal disease and restore healthy gingival tissue.", None),
 ("07","Esthetic Veneers / Porcelain","Concerned with your appearance? Facial veneers or full-coverage porcelain crowns are great options to restore your front teeth.", None),
 ("08","Teeth Whitening","From gentle over-the-counter surface whitening to stronger in-office options for deeper stain removal — together we find the safest path to your best smile.", None),
 ("09","Root Canal Therapy","Dr. Tichy offers root canal therapy using the dental microscope — the practice standard for endodontists — and partners with specialists for the most difficult teeth.", None),
 ("10","Microscopic Dentistry","Every exam and procedure is performed under the dental operating microscope for more precise, conservative, and comfortable care.", "microscopically-assisted-dentistry.html"),
]
cards = ""
for num,title,desc,link in svc_items:
    inner = '<span class="num">'+num+'</span><h3>'+title+'</h3><p>'+desc+'</p>'
    if link: inner += '<p style="margin-top:12px"><a class="inline" href="'+link+'">Learn more →</a></p>'
    cards += '      <div class="item rv">'+inner+'</div>\n'
gd_body = TOPBAR + header(False) + subhero(
    "What We Do · Care For The Whole Family", "General &amp; Family Dentistry",
    "Tichy Dental provides a full range of dental services for your entire family — every exam and procedure performed under the dental operating microscope.",
    "General &amp; Family Dentistry") + '''
<section class="pagebody">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:720px">
      <span class="eyebrow">Services</span>
      <h2>Everything your family needs, in one office</h2>
    </div>
    <div class="svc-list">
''' + cards + '''    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["general-dentistry.html"] = shell(
    "General &amp; Family Dentistry | Tichy Dental, West Linn OR",
    "Comprehensive exams, mercury-free fillings, crowns, extractions, hygiene, veneers, whitening and root canal therapy — all under the microscope at Tichy Dental.",
    gd_body)

# ---------------- 3M CLARITY ALIGNERS ----------------
align_body = TOPBAR + header(False) + subhero(
    "Cosmetic · Clear Aligners", "3M&trade; Clarity&trade; Clear Aligners",
    "A clear, comfortable path to a well-aligned smile — now offered at Tichy Dental with nearly invisible 3M Clarity Aligners and digital, mess-free scanning.",
    "3M Clarity Aligners") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose">
      <p class="lead-para">Tichy Dental now offers 3M&trade; Clarity&trade; Aligners — a custom clear-aligner system of nearly invisible, removable trays that gradually and gently guide your teeth into place.</p>
      <p>With Dr. Tichy's CEREC digital scanner, the impressions for your aligners are captured without the goopy, traditional mess, then used to design a treatment plan tailored to your smile that Dr. Tichy reviews with you before you begin.</p>
      <h2>Why 3M&trade; Clarity&trade; Aligners</h2>
      <ul>
        <li><strong>Nearly invisible.</strong> Clear, low-profile trays designed to be discreet and comfortable to wear throughout your day.</li>
        <li><strong>Durable &amp; stain-resistant.</strong> The outer layer is developed to resist staining, tearing and scratches, and to stand up to hundreds of insertions and removals.</li>
        <li><strong>Removable.</strong> Take them out to eat, brush, and floss — nothing is off the menu, and keeping your mouth clean stays easy.</li>
      </ul>
      <h2>Two materials, one custom plan</h2>
      <p>3M Clarity Aligners come in two tray materials, and Dr. Tichy can use them together in a single treatment design — larger movements with one, comfort and fine detailing with the other.</p>
      <h3>Clarity&trade; Aligners Flex</h3>
      <p>A flexible, five-layer tray that is thinner and more pliable. Its flexibility suits the start of treatment — when there is more crowding — as well as rotations and finishing. 3M reports the Flex material retains about 75% of its force over a two-week period, with an outer layer developed to resist tearing, staining and scratches.</p>
      <h3>Clarity&trade; Aligners Force</h3>
      <p>A time-tested, more rigid tray built for larger movements — widening the arch, correcting deep bites, and delivering the torque needed to address vertical or horizontal discrepancies.</p>
      <p>Optimal oral health starts with well-aligned teeth that are not crowded or misaligned. Let Dr. Tichy show you how clear aligners can help — in more ways than you might imagine.</p>
      <p><strong>Start your clear-aligner journey</strong> by calling us at <a class="inline" href="tel:5036353588">503-635-3588</a> and request a free consult to discuss whether 3M Clarity Aligners are right for you.</p>
      <p>3M&trade; Clarity&trade; Aligners are manufactured by Solventum (formerly 3M Oral Care). <a class="inline" href="''' + CLARITY + '''" target="_blank" rel="noopener">Learn more about the manufacturer</a>.</p>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
align_body = align_body.replace('&trade;', '<sup class="tm">&trade;</sup>').replace('&reg;', '<sup class="tm">&reg;</sup>')
PAGES[ALIGN_PAGE] = shell(
    "3M Clarity Clear Aligners | Tichy Dental, West Linn OR",
    "3M Clarity Aligners at Tichy Dental in West Linn, OR — nearly invisible, stain-resistant clear aligners with mess-free digital scanning. Call for a free consult.",
    align_body)

# ---------------- CEREC ----------------
cerec_body = TOPBAR + header(False) + subhero(
    "Restorative · Same-Day Technology", "CEREC Same-Day Crowns",
    "3D photography and CAD/CAM technology that lets Dr. Tichy design, mill, and place a crown, bridge, inlay, onlay, or veneer in a single visit.",
    "CEREC Same-Day Crowns") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose wide">
      <p class="lead-para">Saving time with CEREC — a 3D photography and CAD/CAM system that allows a dentist to create same-day, single-visit crowns, bridges, inlays, onlays, veneers and more.</p>
      <h2>Why we chose CEREC for our patients</h2>
      <p>Traditional crowns are made in dental laboratories, which requires multiple visits, uncomfortable impressions, numerous injections, a temporary crown, and — most importantly — time away from family and work.</p>
      <p>The biggest advantage of CEREC is saving time. Many of our patients have busy daily schedules, and finding time for a dental visit can be a challenge. In most cases we can cut the number of visits to just one. This leading-edge technology creates high-quality, metal-free crowns right in our office. The advanced CAD/CAM system restores damaged teeth using ceramic blocks, making your new teeth stronger while keeping their natural look.</p>
      <h2>When we use CEREC</h2>
      <ul>
        <li>Crowns — posterior and anterior</li>
        <li>Bridges</li>
        <li>Onlays and inlays</li>
        <li>Veneers</li>
        <li>Clear aligner scans (3M Clarity Aligners)</li>
        <li>Nightguard scans</li>
      </ul>
      <h2>How does CEREC work?</h2>
      <p>First, just like with traditional crowns, Dr. Tichy prepares the tooth for a crown. Next, we take a digital impression to create an image of your tooth and its surrounding area, and send it to the CEREC computer where your new tooth is designed. Dr. Tichy navigates this 3D system to create a perfect replacement. You're welcome to watch as our computer-operated milling machine carves your new restoration from a single ceramic block in a matter of minutes. After milling, we polish and stain the tooth to match the color of your other teeth.</p>
      <p><em>Fun fact:</em> the tooth is purple at this stage, because the high-quality ceramic block is purple. Now it's time for baking — the purple tooth is placed in a high-temperature oven for 15 minutes, and comes out nice and white. The last step is bonding the finished crown to your tooth. And you're done!</p>
      <p>Dr. Tichy and his team always take time to walk you through the procedure beforehand and answer any questions you may have. Please call us at <a class="inline" href="tel:5036353588">503-635-3588</a> for your new patient exam.</p>
      <div class="figrow">
        <figure><img loading="lazy" src="''' + CEREC1 + '''" alt="Dr. Tichy designing a CEREC restoration on screen"><figcaption>Dr. Tichy working on restoration design after taking a digital impression via CEREC CAD/CAM.</figcaption></figure>
        <figure><img loading="lazy" src="''' + CEREC2 + '''" alt="CEREC milling unit carving a ceramic block"><figcaption>Milling process — a high-quality ceramic block is milled by two diamond burs to the shape of the restoration. Patients are welcome to watch; it takes about 15 minutes.</figcaption></figure>
      </div>
      <p>Learn more about the CEREC system in this <a class="inline" href="''' + JADA + '''" target="_blank" rel="noopener">Journal of the American Dental Association article</a>.</p>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["cerec-crowns.html"] = shell(
    "CEREC Same-Day Crowns | Tichy Dental, West Linn OR",
    "Dr. Tichy offers the latest in digital, same-day dental crowns with CEREC CAD/CAM — crowns, bridges, inlays, onlays and veneers in a single visit.",
    cerec_body)

# ---------------- MICROSCOPIC ----------------
micro_body = TOPBAR + header(False) + subhero(
    "Advanced Technology · The Tichy Difference", "Microscopic Dentistry",
    "Dr. Tichy is part of the rare 1% of general dentists who use a dental operating microscope for every procedure — the gold standard of dental care.",
    "Microscopic Dentistry") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="split">
      <div class="prose mt0">
        <h2>The Dental Operating Microscope</h2>
        <p>Dr. Michael Tichy is part of the rare 1% of general dentists who use a microscope for all procedures instead of dental loupes. The benefits of the dental operating microscope are numerous for both the patient and the dentist — it has truly redefined and elevated the standard of care.</p>
        <p>The microscope's superior optics allow far greater magnification than the loupes used by most dentists. Multiple magnification settings increase efficiency and give Dr. Tichy the ability to choose the optimal setting for each step.</p>
        <p>Its unmatched LED light source, combined with the magnification, reveals what usually cannot — or has never — been seen before. The mouth is a dark place; not anymore.</p>
        <p>Using a microscope over loupes allows far more precise and conservative treatment. Seeing better means keeping more healthy tooth when removing decay.</p>
        <p>The scope is also unmatched for ergonomics. It allows Dr. Tichy to remain upright, looking straight ahead, while the optics do all the "bending over" — protecting his health so he can care for yours for years to come.</p>
        <p>A camera attaches to the microscope and relays a simultaneous video feed to HD TVs mounted on the ceiling and wall for patient viewing and education. During every exam and procedure, the doctor discusses findings and treatment options while you watch above in real time.</p>
        <h3>Further reading</h3>
        <ul>
          <li><a class="inline" href="''' + MICRO1 + '''" target="_blank" rel="noopener">The value of the dental operating microscope</a></li>
          <li><a class="inline" href="''' + MICRO2 + '''" target="_blank" rel="noopener">Global dental microscope benefits</a></li>
          <li><a class="inline" href="''' + MICRO3 + '''" target="_blank" rel="noopener">NCBI / PubMed article</a></li>
        </ul>
        <p>If the above sounds great to you, give us a call at <a class="inline" href="tel:5036353588">503-635-3588</a> or book an appointment below to see how technology at Tichy Dental can help your entire family.</p>
      </div>
      <div class="media">
        <img loading="lazy" src="''' + SCOPE + '''" alt="Dr. Michael Tichy practices with a dental microscope, remaining upright while the optics do the work">
      </div>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["microscopically-assisted-dentistry.html"] = shell(
    "Microscopic Dentistry | Tichy Dental, West Linn OR",
    "Microscopically assisted dentistry is the gold standard of care. Dr. Tichy uses a dental operating microscope for every procedure at Tichy Dental.",
    micro_body)

# ---------------- TEAM (6 slots, data in team.json) ----------------
SILHOUETTE = ('<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4">'
              '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>')

def team_section():
    team = json.load(open(os.path.join(HERE, "team.json"), encoding="utf-8"))
    def _esc(s): return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    cards = ""
    for m in team:
        if m.get("name"):
            photo = ('<img class="photo" src="' + m["photo"] + '" alt="' + _esc(m["name"]) + '" loading="lazy">'
                     if m.get("photo") else '<div class="photo empty" aria-hidden="true">' + SILHOUETTE + '</div>')
            cards += ('      <article class="member rv">' + photo + '<div class="body"><span class="role">' + _esc(m.get("role")) +
                      '</span><h3>' + _esc(m["name"]) + '</h3><p>' + _esc(m.get("bio")) + '</p></div></article>\n')
        elif SHOW_EMPTY_TEAM_SLOTS:   # empty slot: placeholder card until a photo and bio are added
            cards += ('      <article class="member empty rv"><div class="photo empty" aria-hidden="true">' + SILHOUETTE + '</div>'
                      '<div class="body"><span class="role">Coming soon</span><h3>Team member</h3>'
                      '<p>Photo and bio coming soon.</p></div></article>\n')
    return """<section class="team" id="team">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">The People Behind Your Smile</span>
      <h2>Meet the team</h2>
      <p class="lede">The friendly faces who will greet you, care for your teeth, and look after your whole family.</p>
    </div>
    <div class="team-grid">
""" + cards + """    </div>
  </div>
</section>
"""

# ---------------- MEET DR TICHY ----------------
meet_body = TOPBAR + header(False) + subhero(
    "Meet Your Dentist", "Meet Dr. Michael Tichy, D.M.D.",
    "A kind and gifted dentist who loves providing gentle care for adults and children — and educating families about preventive care.",
    "Meet Dr. Tichy") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="split rev">
      <div class="about-photo rv" style="justify-self:start">
        <img class="portrait" loading="lazy" src="''' + PORTRAIT + '''" alt="Dr. Michael Tichy, D.M.D.">
        <img class="ski" loading="lazy" src="''' + SKI + '''" alt="Dr. Michael Tichy alpine ski racing">
      </div>
      <div class="prose mt0">
        <p class="lead-para">Dr. Tichy grew up in Canada but has called Oregon home for the past twenty years. His first career was in professional alpine ski racing and coaching, where he collected multiple national and international titles and records.</p>
        <p>Once retired from skiing, Dr. Tichy earned his undergraduate degree from Portland State University, followed by his Doctor of Dental Medicine degree from Oregon Health &amp; Science University. He belongs to a unique group of dental practitioners who use a dental microscope for the majority of their procedures — a technique that allows highly accurate, evidence-based dentistry with a less invasive approach that is more comfortable for patients.</p>
        <p>Dr. Tichy is a kind and gifted dentist who loves to provide gentle care for adults and children, and to educate the entire family about the importance of preventive care and how it relates to overall health. As a husband and father of two young daughters, he understands how to work with adults and children alike.</p>
        <div class="pull">From his first day in West Linn, Dr. Tichy has wanted to be an active, responsible part of this community — so please stop by and say hello.</div>
        <p>Dr. Tichy is committed to providing quality dental care. He can be reached at <a class="inline" href="tel:5036353588">503-635-3588</a> or by email at <a class="inline" href="mailto:info@tichydental.com">info@tichydental.com</a>. His team is here for you and looks forward to seeing you around the neighborhood.</p>
      </div>
    </div>
  </div>
</section>
''' + team_section() + book_band() + FOOTER
PAGES["meet-dr-tichy.html"] = shell(
    "Meet Dr. Michael Tichy, D.M.D. | Tichy Dental, West Linn OR",
    "Meet Dr. Michael Tichy, D.M.D. — OHSU-trained, microscope-assisted dentist and former alpine ski racer serving families in West Linn, Oregon.",
    meet_body)

# ---------------- TESTIMONIALS ----------------
reviews = json.load(open(os.path.join(HERE, "reviews.json"), encoding="utf-8"))
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
rev_html = ""
for r in reviews:
    if r["name"] == "Christopher B.":   # already featured above the grid
        continue
    rev_html += ('      <figure class="rev rv"><span class="stars" role="img" aria-label="5 out of 5 stars">★★★★★</span>'
                 '<blockquote>' + esc(r["text"]) + '</blockquote><figcaption>— ' + esc(r["name"]) + ' · Google review' + ((' · ' + r['date']) if r.get('date') else '') + '</figcaption></figure>\n')
test_body = TOPBAR + header(False) + subhero(
    "Patient Stories", "Patient Testimonials",
    "Real reviews from Tichy Dental patients across West Linn and the surrounding communities.",
    "Testimonials") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="featured-quote rv">
      <div class="stars">★★★★★</div>
      <p>"Dr. Tichy is an incredibly personable and warm dentist. He goes the extra mile to take great care of his patients and to make certain that they are both comfortable and that they understand their care. I even entrust him with my mom and would recommend him to anyone who is looking for a caring and competent dentist."</p>
      <cite>— Christopher B., Google review</cite>
    </div>
    <div class="sec-head rv" style="max-width:100%;text-align:center;margin:0 auto 28px">
      <span class="eyebrow">Rated Across The Web</span>
      <h2>Find us on Google, Yelp &amp; Facebook</h2>
    </div>
    <div class="plat-grid" style="margin-bottom:46px">
      <div class="plat google rv"><div class="logo">G</div><h3>Google Reviews</h3><div class="stars" role="img" aria-label="Rated 5 out of 5 on Google">★★★★★</div><div class="count">5.0 from 150+ Google reviews</div>
        <div class="links"><a class="read" href="''' + MAPS + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + GREVIEW + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
      <div class="plat yelp rv"><div class="logo">Y</div><h3>Yelp</h3><div class="count">See what neighbors say</div>
        <div class="links"><a class="read" href="''' + YELP + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + YELP + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
      <div class="plat facebook rv"><div class="logo">f</div><h3>Facebook</h3><div class="count">Recommendations from our community</div>
        <div class="links"><a class="read" href="''' + FB + '''" target="_blank" rel="noopener">Read our reviews</a><a class="leave" href="''' + FB + '''" target="_blank" rel="noopener">Leave a review</a></div></div>
    </div>
    <div class="sec-head rv" style="max-width:100%;text-align:center;margin:0 auto 28px">
      <span class="eyebrow">In Their Own Words</span>
      <h2>Reviews from our patients</h2>
    </div>
    <div class="rev-grid">
''' + rev_html + '''    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["testimonials.html"] = shell(
    "Patient Testimonials | Tichy Dental, West Linn OR",
    "Read real patient testimonials and reviews for Tichy Dental in West Linn, Oregon.",
    test_body)

# ---------------- INSURANCE ----------------
insurers = [
    ("Delta Dental / Moda", [("Delta Dental", "delta-dental.svg"), ("Moda Health", "moda.svg")]),
    ("Regence BlueCross BlueShield", [("Regence BlueCross BlueShield", "regence.svg")]),
    ("DenteMax", [("DenteMax", "dentemax.png")]),
    ("MetLife", [("MetLife", "metlife.svg")]),
    ("United Concordia", [("United Concordia", "united-concordia.png")]),
    ("Cigna Dental", [("Cigna", "cigna.png")]),
]
ins_cards = ""
for name, logos in insurers:
    imgs = "".join('<img src="assets/img/insurers/' + f + '" alt="' + alt + ' logo" loading="lazy">' for alt, f in logos)
    ins_cards += ('      <div class="ins rv"><div class="logos">' + imgs + '</div>'
                  '<span class="insname">' + name + '</span></div>\n')
ins_body = TOPBAR + header(False) + subhero(
    "Patient Info · Insurance &amp; Billing", "Insurance &amp; Billing",
    "We accept many insurance companies and are preferred providers for the plans below. Not sure about yours? Just give us a call.",
    "Insurance &amp; Billing") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose wide mt0">
      <h2 class="mt0">Preferred providers</h2>
      <p>We are preferred providers for the following insurance companies:</p>
    </div>
    <div class="ins-grid">
''' + ins_cards + '''    </div>
    <div class="ins-note">
      <p style="margin:0 0 10px"><strong>Don't see your plan?</strong> We accept many more insurance companies — please call us at <a class="inline" href="tel:5036353588">(503) 635-3588</a> to ask if we accept yours.</p>
      <p style="margin:0">Note: Dentemax is not an insurance company itself, but has hundreds of insurance companies under its umbrella — so call and ask if you may be covered under the Dentemax umbrella.</p>
    </div>
    <p class="ins-updated">List last updated October 2026. Coverage and benefits vary by plan, so please also confirm your benefits with your insurance company.</p>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["insurance.html"] = shell(
    "Insurance &amp; Billing | Tichy Dental, West Linn OR",
    "Dental insurances accepted at Tichy Dental — preferred providers include Delta Dental/Moda, Regence, Dentemax, MetLife, United Concordia and Cigna.",
    ins_body)

# ---------------- FAQ ----------------
FAQ_DATA = []
def qa(q, answer_html, template=False):
    if not template:   # template answers stay out of FAQPage structured data until filled in
        FAQ_DATA.append((q, answer_html))
    return '      <details class="qa"><summary>'+q+'</summary><div class="a">'+answer_html+'</div></details>\n'
faq_items = ""
faq_items += qa("How can I schedule an appointment with Tichy Dental?",
    '<ul><li>Visit our <a class="inline" href="'+LOGIN+'" target="_blank" rel="noopener">Patient Portal</a> and request an appointment with your desired dates and times.</li><li>Call Laura at <a class="inline" href="tel:5036353588">503-635-3588</a> and ask for appointment availability.</li></ul>')
faq_items += qa("What do I need to do before my first appointment?",
    '<p>Visit our <a class="inline" href="'+REG+'" target="_blank" rel="noopener">Patient Portal</a> and complete the patient registration. It includes several forms with signatures for HIPAA, general consent and health history, insurance info, smile analysis, and patient information.</p>')
faq_items += qa("What should I bring with me to my first appointment?",
    '<ul><li>If the patient registration was completed online, we do not need anything at all.</li><li>It is helpful to bring your medication and allergy list if it is extensive.</li></ul>')
faq_items += qa("What can I expect during my first appointment?",
    '<p>The first appointment is a comprehensive exam in which the doctor examines all aspects of your oral health. Most often this includes taking needed radiographs and examining the findings. The doctor reviews your oral health, determines your periodontal health, and examines your teeth. He then takes everything into consideration and presents you with the best treatment plans.</p>')
faq_items += qa("What do the overhead monitors during the exam mean?",
    '<p>Dr. Tichy is part of the rare 1% of general dentists who use a microscope for all procedures, which allows him to connect an HD camera. The camera feeds directly to overhead monitors for real-time video — so you can see and watch everything the doctor sees. During this time the doctor reviews findings, takes intra-oral pictures for later review, and explains the best options to you.</p>')
faq_items += qa("Can I expect a cleaning during my first appointment?",
    '<p>The doctor makes every attempt to provide a cleaning. However, not every patient has healthy gums and can receive a simple prophy cleaning. Some patients need considerable treatment planning; those who present with periodontal disease may need extensive planning and prior insurance approval for deep cleanings (scaling and root planing).</p>')
faq_items += qa("Do you see children?",
    '<p>Yes. Dr. Tichy cares for adults and children alike, and our team works to keep young patients comfortable. Call <a class="inline" href="tel:5036353588">(503) 635-3588</a> to book visits for the whole family.</p>')
faq_items += qa("What should I do in a dental emergency?",
    '<p>Call us right away at <a class="inline" href="tel:5036353588">(503) 635-3588</a> during office hours (Monday–Thursday, 8am–5pm). Our <a class="inline" href="emergency-dentist.html">Emergency Dental Care</a> page explains what to do for a knocked-out tooth, toothache or broken tooth, and when to go to an emergency room instead.</p>')
faq_items += qa("Is the office wheelchair accessible?",
    '<p>Yes. Our office has a wheelchair-accessible entrance, parking and restroom. If you need any other assistance during your visit, let us know when you call.</p>')
faq_items += qa("Where do I park?",
    '<p>We have a parking lot at the office, including accessible parking. We\'re at 18607 Willamette Dr. in West Linn — <a class="inline" href="' + DIRECTIONS + '" target="_blank" rel="noopener">get directions</a>.</p>')
faq_items += qa("What forms of payment do you accept?",
    '<p>We accept credit cards, debit cards and contactless mobile payments, as well as many dental insurance plans (see <a class="inline" href="insurance.html">Insurance &amp; Billing</a>). For questions about your balance or payment options, call our front desk at <a class="inline" href="tel:5036353588">(503) 635-3588</a>.</p>')
faq_items += qa("Do you offer financing or payment plans?",
    '<p><span class="tbd">[Template — complete before going live: describe payment plans or financing options the office offers, or remove this question.]</span></p>', template=True)
faq_items += qa("What is your cancellation policy?",
    '<p><span class="tbd">[Template — complete before going live: how much notice is needed to cancel or reschedule (for example, 24 or 48 hours) and any missed-appointment fee.]</span></p>', template=True)
faq_items += qa("What insurance does Tichy Dental accept?",
    '<p>We accept many insurance companies and are preferred providers for: Delta Dental/Moda, Regence BlueCross BlueShield, Dentemax, MetLife, United Concordia, and Cigna. Please call us to ask if we accept your insurance. Dentemax is not an insurance company but has hundreds of insurance companies under its umbrella — so call and ask if you may be covered. See our <a class="inline" href="insurance.html">Insurance &amp; Billing</a> page for more.</p>')
faq_body = TOPBAR + header(False) + subhero(
    "Patient Info · FAQ", "Frequently Asked Questions",
    "Everything you need to know about your first visit, our technology, cleanings, and insurance.",
    "FAQ") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="faq-group">
      <div class="glabel">First Visit to the Office</div>
''' + faq_items + '''    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["faq.html"] = shell(
    "FAQ | Tichy Dental, West Linn OR",
    "Frequently asked questions about Tichy Dental — scheduling, first visits, overhead monitors, cleanings, and accepted insurance.",
    faq_body)

# ---------------- EMERGENCY DENTAL CARE ----------------
emerg_body = TOPBAR + header(False) + subhero(
    "Emergency Dental Care · West Linn", "Dental emergency? <em>Call us first.</em>",
    "A broken tooth, sudden toothache, or knocked-out tooth? Call <span class='nowrap'>(503) 635-3588</span> and we'll help you with the next step.",
    "Emergency Dental Care") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose">
      <div class="em-alert" role="note"><strong>Go to an emergency room or call 911</strong>if you have swelling that is spreading toward your eye or neck or making it hard to breathe or swallow, bleeding that won't stop, or a jaw injury from an accident or a blow to the head.</div>
      <div class="em-call">
        <a class="btn btn-amber" href="tel:5036353588">Call (503) 635-3588</a>
        <a class="btn btn-ghost" href="''' + APPT + '''" target="_blank" rel="noopener">Request Appointment</a>
      </div>
      <p class="lead-para">We provide emergency dental care to relieve pain and to triage accidents that may need more definitive treatment. Call as early as you can and we'll do our best to see you quickly.</p>
      <p>Our office is open Monday–Thursday, 8am–5pm. If a problem starts while we're closed and it isn't one of the situations above, call us first thing on our next business day.</p>
      <h2>What to do until you see us</h2>
      <h3>Knocked-out adult tooth</h3>
      <p>Pick the tooth up by the crown (the chewing surface), not the root. If it's dirty, rinse it gently with water and don't scrub it. If you can, place it back in the socket and hold it there; otherwise keep it in a small container of milk. Call us right away, because the sooner you're seen, the better the chance of saving the tooth.</p>
      <h3>Toothache</h3>
      <p>Rinse with warm water and gently floss to remove anything caught between your teeth. A cold compress on the outside of your cheek can ease swelling. Don't put aspirin directly on the gum or tooth.</p>
      <h3>Chipped or broken tooth</h3>
      <p>Save any pieces, rinse your mouth with warm water, and use a cold compress to reduce swelling.</p>
      <h3>Lost filling or crown</h3>
      <p>Keep the crown if you have it and bring it with you. Avoid chewing on that side until we can see you.</p>
      <h2>A patient's experience</h2>
      <div class="pull">"I had broken a tooth and he was able to get me in first thing the next morning. Even though it was snowing and the roads were bad his staff still came in and took care of me." — Linda R., Google review</div>
      <p class="ins-updated">This page is general information, not a diagnosis. If you're not sure whether it's an emergency, call us.</p>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["emergency-dentist.html"] = shell(
    "Emergency Dentist in West Linn, OR | Tichy Dental",
    "Dental emergency in West Linn? Call Tichy Dental at (503) 635-3588. What to do for a knocked-out tooth, toothache or broken tooth, and when to go to the ER.",
    emerg_body)

# ---------------- NOTICE OF PRIVACY PRACTICES (template) ----------------
def tbd(text):
    return '<span class="tbd">[' + text + ']</span>'
npp_body = TOPBAR + header(False) + subhero(
    "Patient Info · HIPAA", "Notice of Privacy Practices",
    "How Tichy Dental may use and share your health information, and your rights to access and control it.",
    "Notice of Privacy Practices") + """
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose">
      <div class="tbd-banner" role="note"><strong>Template — complete before going live.</strong> Replace every highlighted field with the practice's information and have the practice's privacy officer or compliance advisor approve the final notice. Structure follows the HHS model Notice of Privacy Practices for health care providers.</div>
      <p class="ins-updated" style="margin-top:0">Effective date: """ + tbd("Month Day, Year") + """</p>
      <p class="lead-para">This notice describes how medical information about you may be used and disclosed and how you can get access to this information. Please review it carefully.</p>

      <h2>Your rights</h2>
      <p>When it comes to your health information, you have certain rights:</p>
      <ul>
        <li><strong>Get a copy of your dental and health records.</strong> Ask us to see or get a copy of your records. We will provide a copy or a summary within """ + tbd("number") + """ days of your request. We may charge a reasonable, cost-based fee.</li>
        <li><strong>Ask us to correct your records</strong> if you think they are incorrect or incomplete. We may say "no," but we'll tell you why in writing within 60 days.</li>
        <li><strong>Request confidential communications.</strong> Ask us to contact you in a specific way (for example, home or office phone) or to send mail to a different address.</li>
        <li><strong>Ask us to limit what we use or share.</strong> If you pay for a service in full out of pocket, you can ask us not to share that information with your health insurer.</li>
        <li><strong>Get a list of those with whom we've shared information</strong> for up to six years before the date you ask.</li>
        <li><strong>Get a copy of this notice</strong> at any time, even if you have agreed to receive it electronically.</li>
        <li><strong>Choose someone to act for you,</strong> such as a medical power of attorney or legal guardian.</li>
        <li><strong>File a complaint</strong> if you feel your rights are violated — see "Contact" below. We will not retaliate against you for filing a complaint.</li>
      </ul>

      <h2>Your choices</h2>
      <p>You can tell us your choices about what we share in these situations: sharing with your family, close friends or others involved in your care, and sharing in a disaster-relief situation. We never share your information for marketing purposes or sell it unless you give us written permission.</p>
      <p>""" + tbd("Describe any appointment-reminder, text-message or email practices and how patients can opt out") + """</p>

      <h2>Our uses and disclosures</h2>
      <p>We typically use or share your health information to <strong>treat you</strong>, to <strong>run our practice</strong>, and to <strong>bill for your services</strong> and receive payment from health plans or other entities.</p>
      <p>We are also allowed or required to share your information in other ways — usually to contribute to the public good, such as public health and research — including to help with public health and safety issues, comply with the law, respond to organ and tissue donation requests, work with a medical examiner or funeral director, address workers' compensation, law enforcement and other government requests, and respond to lawsuits and legal actions.</p>
      <p>""" + tbd("Add any state-specific (Oregon) requirements identified by the practice's advisor") + """</p>

      <h2>Our responsibilities</h2>
      <ul>
        <li>We are required by law to maintain the privacy and security of your protected health information.</li>
        <li>We will let you know promptly if a breach occurs that may have compromised the privacy or security of your information.</li>
        <li>We must follow the duties and privacy practices described in this notice and give you a copy of it.</li>
        <li>We will not use or share your information other than as described here unless you tell us we can in writing. You may change your mind at any time by letting us know in writing.</li>
      </ul>

      <h2>Changes to the terms of this notice</h2>
      <p>We can change the terms of this notice, and the changes will apply to all information we have about you. The new notice will be available on request, in our office, and on our website.</p>

      <h2>Contact</h2>
      <p>Privacy Officer: """ + tbd("Name") + """ · Tichy Dental LLC, 18607 Willamette Dr., West Linn, OR 97068 · <a class="inline" href="tel:5036353588">(503) 635-3588</a> · """ + tbd("Email") + """</p>
      <p>You can also file a complaint with the U.S. Department of Health and Human Services Office for Civil Rights at <a class="inline" href="https://www.hhs.gov/ocr/complaints/index.html" target="_blank" rel="noopener">hhs.gov/ocr/complaints</a>.</p>
    </div>
  </div>
</section>
""" + book_band() + FOOTER
PAGES["notice-of-privacy-practices.html"] = shell(
    "Notice of Privacy Practices | Tichy Dental, West Linn OR",
    "HIPAA Notice of Privacy Practices for Tichy Dental in West Linn, Oregon.",
    npp_body)

# ---------------- LEGAL PAGES (drafts — review before publishing) ----------------
DRAFT_NOTE = ''
_OLD_DRAFT_NOTE = ('<p class="ins-note" style="margin:0 0 24px"><strong>Draft for review.</strong> '
              'This page is a starting template. The practice and its legal or compliance advisor '
              'must review it before it is published.</p>')

privacy_body = TOPBAR + header(False) + subhero(
    "Patient Info · Privacy", "Privacy Policy",
    "How Tichy Dental handles information connected to this website.",
    "Privacy Policy") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose">
      ''' + DRAFT_NOTE + '''
      <p class="ins-updated" style="margin-top:0">Effective October 13, 2026 · Last updated October 13, 2026</p>
      <h2>Information we collect</h2>
      <p>This website does not collect personal or health information directly, and it does not use advertising or tracking cookies. Appointment requests, patient registration, and consent forms are completed through our secure patient portal, which is operated by our practice-management provider and protected under HIPAA. Read the ''' + '<a class="inline" href="' + PORTAL_PRIVACY_URL + '" target="_blank" rel="noopener">patient portal privacy policy</a>' + '''.</p>
      <p>If you call or email us, we use what you share only to respond to you and to provide care. Please don't send medical details or other sensitive information by email; use the secure patient portal instead.</p>
      <h2>Third-party services</h2>
      <p>Fonts are hosted on this website. The office map loads from Google Maps only when you choose to open it. Links to Google, Yelp, Facebook, Instagram, X, and product manufacturers take you to sites governed by their own privacy policies.</p>
      <h2>Your health information</h2>
      <p>Our Notice of Privacy Practices explains how protected health information is used and disclosed under HIPAA. ''' + (('<a class="inline" href="' + NPP_URL + '" target="_blank" rel="noopener">Read the Notice of Privacy Practices</a>, or ask') if NPP_URL else 'Ask') + ''' our front desk for a copy, or call <a class="inline" href="tel:5036353588">(503) 635-3588</a>.</p>
      <h2>Contact</h2>
      <p>Questions about this policy: <a class="inline" href="mailto:info@tichydental.com">info@tichydental.com</a> · 18607 Willamette Dr., West Linn, OR 97068.</p>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["privacy.html"] = shell(
    "Privacy Policy | Tichy Dental, West Linn OR",
    "Privacy policy for the Tichy Dental website in West Linn, Oregon.",
    privacy_body)

a11y_body = TOPBAR + header(False) + subhero(
    "Patient Info · Accessibility", "Accessibility Statement",
    "We want everyone to be able to use this website and reach our office.",
    "Accessibility") + '''
<section class="pagebody tight">
  <div class="wrap">
    <div class="prose">
      ''' + DRAFT_NOTE + '''
      <h2>Our commitment</h2>
      <p>Tichy Dental aims to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA across this website.</p>
      <h2>What we have done</h2>
      <ul>
        <li>Text and buttons meet AA color-contrast requirements.</li>
        <li>Every page has a clear heading structure and a main content landmark.</li>
        <li>Images have text alternatives, and patient reviews are published as text.</li>
        <li>The site works with a keyboard, and animation is reduced when your device asks for reduced motion.</li>
      </ul>
      <h2>Need help or found a problem?</h2>
      <p>If anything on this site is hard to use, call <a class="inline" href="tel:5036353588">(503) 635-3588</a> or email <a class="inline" href="mailto:info@tichydental.com">info@tichydental.com</a>. We will help you directly and work to fix the issue.</p>
    </div>
  </div>
</section>
''' + book_band() + FOOTER
PAGES["accessibility.html"] = shell(
    "Accessibility Statement | Tichy Dental, West Linn OR",
    "Accessibility statement for the Tichy Dental website in West Linn, Oregon.",
    a11y_body)

# ---------------- SEO head extras, image post-processing ----------------
import re as _re
from PIL import Image as _Image

SITE = "https://www.tichydental.com"   # canonical domain; paths below are extensionless (/faq)
ASSET_BASE = SITE if LIVE else "https://rainmanjam.github.io/tichy-dental-concept"   # where the files are hosted

def live_path(name):
    return "/" if name == "index.html" else "/" + name[:-5]

import html as _html, datetime as _dt
TODAY = _dt.date.today().isoformat()
DENTIST_ID = SITE + "/#dentist"
DOCTOR_ID = SITE + "/meet-dr-tichy#dr-tichy"
SERVICE_PAGES = {
    "general-dentistry.html": "General & Family Dentistry",
    "clarity-aligners.html": "3M Clarity Clear Aligners",
    "cerec-crowns.html": "CEREC Same-Day Crowns",
    "microscopically-assisted-dentistry.html": "Microscope-Assisted Dentistry",
    "emergency-dentist.html": "Emergency Dental Care",
}
SAME_AS = [GOOGLE_CID_URL, FB, IG, TW] + ([YELP_URL] if YELP_URL else [])

def page_schema(name, title, desc, url):
    """One @graph per page: the practice, Dr. Tichy, the page itself, plus breadcrumb/service/FAQ where relevant."""
    title, desc = _html.unescape(title), _html.unescape(desc)
    graph = [
        {"@type": "Dentist", "@id": DENTIST_ID, "name": "Tichy Dental", "url": SITE + "/",
         "telephone": "+1-503-635-3588", "email": "info@tichydental.com",
         "image": ASSET_BASE + "/assets/img/og-image.jpg",
         "logo": ASSET_BASE + "/assets/img/apple-touch-icon.png",
         "address": {"@type": "PostalAddress", "streetAddress": "18607 Willamette Dr.",
                     "addressLocality": "West Linn", "addressRegion": "OR",
                     "postalCode": "97068", "addressCountry": "US"},
         "geo": {"@type": "GeoCoordinates", "latitude": 45.3912526, "longitude": -122.6463701},
         "hasMap": GOOGLE_CID_URL,
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
                                        "opens": "08:00", "closes": "17:00"}],
         "areaServed": ["West Linn", "Lake Oswego", "Oregon City"],
         "sameAs": SAME_AS,
         "founder": {"@id": DOCTOR_ID}, "employee": {"@id": DOCTOR_ID}},
        {"@type": "Person", "@id": DOCTOR_ID, "name": "Dr. Michael Tichy", "honorificSuffix": "D.M.D.",
         "jobTitle": "Dentist", "url": SITE + "/meet-dr-tichy",
         "image": ASSET_BASE + "/assets/img/f9995c_119eb82f2552473c929929d883e91d19.webp",
         "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Oregon Health & Science University"},
                      {"@type": "CollegeOrUniversity", "name": "Portland State University"}],
         "worksFor": {"@id": DENTIST_ID}},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title,
         "description": desc, "about": {"@id": DENTIST_ID}, "dateModified": TODAY},
    ]
    if name != "index.html":
        graph[-1]["breadcrumb"] = {"@id": url + "#breadcrumb"}
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": title.split(" | ")[0], "item": url}]})
    if name in SERVICE_PAGES:
        graph.append({"@type": "Service", "name": SERVICE_PAGES[name], "serviceType": SERVICE_PAGES[name],
                      "url": url, "provider": {"@id": DENTIST_ID}, "areaServed": "West Linn, OR"})
    if name == "faq.html" and FAQ_DATA:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": _html.unescape(q),
             "acceptedAnswer": {"@type": "Answer",
                                "text": _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", " ", a))).strip()}}
            for q, a in FAQ_DATA]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")

def head_extras(name, html):
    title = _re.search(r"<title>(.*?)</title>", html).group(1)
    desc = _re.search(r'name="description" content="([^"]*)"', html).group(1)
    url = SITE + live_path(name)
    return ('<link rel="canonical" href="' + url + '">\n'
            '<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">\n'
            '<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:site_name" content="Tichy Dental">\n'
            '<meta property="og:title" content="' + title + '">\n'
            '<meta property="og:description" content="' + desc + '">\n'
            '<meta property="og:url" content="' + url + '">\n'
            '<meta property="og:image" content="' + ASSET_BASE + '/assets/img/og-image.jpg">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<script type="application/ld+json">' + page_schema(name, title, desc, url) + '</script>\n'
            + ('' if LIVE else '<meta name="robots" content="noindex">\n'))

def img_size(path):
    full = os.path.join(PROJECT, path)
    if path.endswith(".svg"):
        s = open(full, encoding="utf-8", errors="replace").read(4000)
        tag = _re.search(r"<svg[^>]*>", s)
        tag = tag.group(0) if tag else ""
        w = _re.search(r'\bwidth="([\d.]+)(?:px)?"', tag)
        h = _re.search(r'\bheight="([\d.]+)(?:px)?"', tag)
        if w and h:
            return round(float(w.group(1))), round(float(h.group(1)))
        vb = _re.search(r'viewBox="[\d.\-]+[ ,]+[\d.\-]+[ ,]+([\d.]+)[ ,]+([\d.]+)"', tag)
        return (round(float(vb.group(1))), round(float(vb.group(2)))) if vb else None
    with _Image.open(full) as im:
        return im.size

def fix_imgs(html):
    def repl(m):
        tag, src = m.group(0), m.group(1)
        webp = _re.sub(r"\.(jpe?g|png)$", ".webp", src)
        if webp != src and "/insurers/" not in src and os.path.exists(os.path.join(PROJECT, webp)):
            tag = tag.replace('src="' + src + '"', 'src="' + webp + '"')
            src = webp
        if "width=" not in tag:
            wh = img_size(src)
            if wh:
                tag = tag.replace("<img ", '<img width="%d" height="%d" ' % wh, 1)
        if "srcset=" not in tag and src.endswith(".webp") and "/insurers/" not in src:
            w = img_size(src)[0]
            if w > 900:   # add a 600px variant so phones don't download the 1200px file
                small = src[:-5] + "-600.webp"
                if not os.path.exists(os.path.join(PROJECT, small)):
                    with _Image.open(os.path.join(PROJECT, src)) as im:
                        im.resize((600, round(im.height * 600 / im.width)), _Image.LANCZOS).save(
                            os.path.join(PROJECT, small), "WEBP", quality=80, method=6)
                tag = tag.replace("<img ", '<img srcset="%s 600w, %s %dw" sizes="(max-width: 760px) 100vw, 50vw" ' % (small, src, w), 1)
        if 'class="office"' in tag:   # hero image is the LCP element — load it first
            tag = tag.replace('loading="lazy"', 'loading="eager" fetchpriority="high"')
        return tag
    return _re.sub(r'<img [^>]*src="(assets/[^"]+)"[^>]*>', repl, html)

# ---- write all ----
for name, htmlstr in PAGES.items():
    htmlstr = htmlstr.replace('<link rel="stylesheet" href="assets/css/site.css">',
                              '<link rel="stylesheet" href="assets/css/site.css">\n' + head_extras(name, htmlstr), 1)
    htmlstr = fix_imgs(htmlstr)
    with open(os.path.join(PROJECT, name), "w", encoding="utf-8") as f:
        f.write(htmlstr)
    print(f"wrote {name:46s} {len(htmlstr):7d} bytes")

with open(os.path.join(PROJECT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for name in PAGES:
        f.write("  <url><loc>" + SITE + live_path(name) + "</loc><lastmod>" + TODAY + "</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(PROJECT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: " + SITE + "/sitemap.xml\n")
print("wrote sitemap.xml and robots.txt")
