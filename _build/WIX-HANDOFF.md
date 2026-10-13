# Wix handoff — Tichy Dental

Rebuild spec for moving the GitHub Pages site into the **classic Wix Editor** on tichydental.com.
The live preview is the visual reference: https://rainmanjam.github.io/tichy-dental-concept/

## 1. Design tokens (Site Design → Colors / Text)
| Token | Value | Use |
|---|---|---|
| Ink | `#0E3A47` | Headings, dark sections, footer |
| Teal | `#155E75` | Eyebrow labels, links, icons |
| Teal soft | `#E8F4F8` | Icon tiles, soft backgrounds |
| Teal mist | `#F4F9FB` | Alternate section background |
| Amber (buttons) | `#9A6A14` (hover `#7F560F`) | Primary buttons — white text passes WCAG AA |
| Amber (accents) | `#C8892B` | Stars, dots, borders only (not text) |
| Muted text | `#5B7681` | Body copy on white |
| Line | `#D8E6EC` | Card borders |
| Page | `#FDFEFE` | Background |

**Fonts:** Fraunces (headings; weights 400/560/640 + italic) and Figtree (body; 400–700). Both are Google Fonts
(SIL OFL) — available in Wix's font list; if not, upload the files in `assets/fonts/`.
**Radius:** 18px cards, 999px pill buttons. **Shadow:** soft, `0 18px 50px -18px rgba(14,58,71,.25)`.

## 2. Pages, URLs and SEO text (Page Settings → SEO basics)
Keep every existing URL. The only change is `/invisalign` → `/clarity-aligners`; `/emergency-dentist`,
`/privacy` and `/accessibility` are new.

| URL slug | H1 (exactly one per page) | SEO title | Meta description |
|---|---|---|---|
| `/` | Family & cosmetic dentistry, seen up close. | West Linn Dentist | CEREC Crowns & Clear Aligners | Tichy Dental | Gentle, microscope-assisted dentistry in West Linn, OR. CEREC same-day crowns, 3M Clarity clear aligners, and family care. Book online today. |
| `/general-dentistry` | General & Family Dentistry | General & Family Dentistry | Tichy Dental, West Linn OR | Comprehensive exams, mercury-free fillings, crowns, extractions, hygiene, veneers, whitening and root canal therapy — all under the microscope at Tichy Dental. |
| `/emergency-dentist` | Dental emergency? Call us first. | Emergency Dentist in West Linn, OR | Tichy Dental | Dental emergency in West Linn? Call Tichy Dental at (503) 635-3588. What to do for a knocked-out tooth, toothache or broken tooth, and when to go to the ER. |
| `/clarity-aligners` | 3M™ Clarity™ Clear Aligners | 3M Clarity Clear Aligners | Tichy Dental, West Linn OR | 3M Clarity Aligners at Tichy Dental in West Linn, OR — nearly invisible, stain-resistant clear aligners with mess-free digital scanning. Call for a free consult. |
| `/cerec-crowns` | CEREC Same-Day Crowns | CEREC Same-Day Crowns | Tichy Dental, West Linn OR | Dr. Tichy offers the latest in digital, same-day dental crowns with CEREC CAD/CAM — crowns, bridges, inlays, onlays and veneers in a single visit. |
| `/microscopically-assisted-dentistry` | Microscopic Dentistry | Microscopic Dentistry | Tichy Dental, West Linn OR | Microscopically assisted dentistry is the gold standard of care. Dr. Tichy uses a dental operating microscope for every procedure at Tichy Dental. |
| `/meet-dr-tichy` | Meet Dr. Michael Tichy, D.M.D. | Meet Dr. Michael Tichy, D.M.D. | Tichy Dental, West Linn OR | Meet Dr. Michael Tichy, D.M.D. — OHSU-trained, microscope-assisted dentist and former alpine ski racer serving families in West Linn, Oregon. |
| `/testimonials` | Patient Testimonials | Patient Testimonials | Tichy Dental, West Linn OR | Read real patient testimonials and reviews for Tichy Dental in West Linn, Oregon. |
| `/insurance` | Insurance & Billing | Insurance & Billing | Tichy Dental, West Linn OR | Dental insurances accepted at Tichy Dental — preferred providers include Delta Dental/Moda, Regence, Dentemax, MetLife, United Concordia and Cigna. |
| `/faq` | Frequently Asked Questions | FAQ | Tichy Dental, West Linn OR | Frequently asked questions about Tichy Dental — scheduling, first visits, overhead monitors, cleanings, and accepted insurance. |
| `/privacy` | Privacy Policy | Privacy Policy | Tichy Dental, West Linn OR | Privacy policy for the Tichy Dental website in West Linn, Oregon. |
| `/accessibility` | Accessibility Statement | Accessibility Statement | Tichy Dental, West Linn OR | Accessibility statement for the Tichy Dental website in West Linn, Oregon. |

## 3. Redirects (SEO → URL Redirect Manager)
See `wix-redirects.csv`. Wix creates the `/invisalign` redirect automatically when you rename that page's
URL — confirm it appears in the Redirect Manager, then test it on the live site.

## 4. Component map (GitHub site → Wix)
| Site component | Build in Wix with |
|---|---|
| Top utility bar + sticky header + dropdown menu | Header (global): text links, Wix menu with sub-pages, button |
| Hero with photo, "1%" chip and round microscope inset | Strip with image, text box overlay, circle-cropped image |
| Service cards (home), service list (General Dentistry) | Repeater, or 4 / 10 boxes with icon + title + text + link |
| Microscope band (dark) | Dark strip, circle-cropped image, 3 stat boxes |
| Team (6 slots) | **CMS collection `Team`** (name, role, photo, bio) + Repeater; hide items without a name |
| Testimonials | **CMS collection `Reviews`** (name, text, date) + Repeater; source: `reviews.json` |
| Insurance logos | **CMS collection `Insurers`** (name, logo) + Repeater; Delta Dental / Moda share one card |
| FAQ accordion | Wix FAQ app, or collapsible text boxes; source: `faq.html` |
| Booking band | Gradient strip + 3 buttons (portal links below) |
| Footer with hours, map, socials | Footer (global); Wix Google Maps element |

## 5. Links that must stay exactly the same
| Purpose | URL |
|---|---|
| Request Appointment | https://tch.identalcloud.com/TichyDental/Patient/_practice/1/Appointment |
| New Patient Forms | https://tch.identalcloud.com/TichyDental/Patient/_practice/1/Registration |
| Patient Login | https://tch.identalcloud.com/TichyDental/Patient/_practice/1 |
| Yelp | https://www.yelp.com/biz/tichy-dental-west-linn |
| Facebook / Instagram / X | facebook.com/TichyDental · instagram.com/tichydental · x.com/MichaelTichyDMD |

## 6. SEO and structured data
- Home page → Page Settings → SEO → **Advanced SEO → Structured Data Markup**: paste the `@graph` JSON from
  `index.html` (the `<script type="application/ld+json">` block). Paste each page's own block on that page
  (service pages carry a `Service` node, the FAQ carries `FAQPage`).
- Before pasting, rebuild with `LIVE = True` in `generate_site.py` so image URLs point at tichydental.com.
- Do **not** port `sitemap.xml` or `robots.txt` — Wix generates both. Do not copy the `noindex` tag.
- Set the site-wide social share image to `assets/img/og-image.jpg`.
- Business Info: change the category from "Services Maintenance" to a dentist/health category and add a short description.
- Connect Bing Webmaster Tools; link Google Search Console data in the SEO dashboard.

## 7. Accessibility checklist for the Wix build
- One H1 per page; use H2/H3 in order (set the heading tag on each text box).
- Alt text on every image (copy from the GitHub HTML `alt` attributes).
- Button text must contrast with its background (use the button amber, not the accent amber).
- Run the Wix Accessibility Wizard before publishing; check the mobile layout of every page.

## 8. Launch QA
- [ ] Every page reachable from the menu on desktop and mobile
- [ ] All portal links open the correct identalcloud page
- [ ] `/invisalign` redirects to `/clarity-aligners`
- [ ] Phone number taps to call on mobile
- [ ] Structured data passes Google's Rich Results Test
- [ ] Sitemap submitted in Google Search Console and Bing Webmaster Tools
- [ ] GitHub Pages preview kept `noindex` (or taken down)
