# Build system — Tichy Dental concept site

The 9 pages in the repo root are **generated**. Edit the source here, not the HTML directly,
so the shared header/footer/CSS stay in sync across every page.

## Files
- `make_assets.py` — writes `assets/css/site.css` (design system) and `assets/js/site.js`.
- `generate_site.py` — writes all 9 `*.html` pages. Holds the shared topbar/header/footer,
  per-page content, image paths, and outbound links (constants at the top).
- `page_images.json` — per-page image inventory used by the generator (from the original spider).
- `reviews.json` — patient reviews (transcribed from Google review screenshots) shown on the Testimonials page.

The generator also writes `sitemap.xml`, `robots.txt`, canonical/Open Graph tags and Dentist
structured data, swaps photos to their `.webp` versions, and adds image width/height automatically.
`SITE` near the bottom of `generate_site.py` sets the live domain used in those URLs.

## Regenerate
```bash
cd _build
python3 make_assets.py      # run this first (writes site.css + site.js)
python3 generate_site.py    # then this (writes the 9 HTML pages)
```
Paths are relative to the repo, so it works wherever the repo lives.

## Common edits
- Change a phone number / address / hours → edit the `TOPBAR` / `FOOTER` strings in `generate_site.py`.
- Change an outbound link (booking, portal, 3M, etc.) → edit the constants near the top of `generate_site.py`.
- Change colors / spacing → `make_assets.py` (base design system is inherited verbatim from the
  original `index.html` concept, with a components block appended for interior pages).

## Notes
- Images live in `assets/img/` (site photos) and `assets/img/insurers/` (insurer logos).
- Fonts (Fraunces + Figtree) load from Google Fonts CDN — the site is not fully offline.
- These pages are a design concept, not the live site.
