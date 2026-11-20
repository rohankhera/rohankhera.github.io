# rohankhera.com — maintenance notes

Personal site for Rohan Khera, MD, MS. Static, single page, hosted on GitHub Pages from `main` with the custom domain in `CNAME`. No build step, no framework, no JavaScript beyond JSON-LD.

## Files
- `index.html` — the whole site (markup + inline CSS).
- `headshot.jpg` — 640×640 portrait used on the page and in JSON-LD.
- `og-image.jpg` — 1200×630 social share card (photo right, name left). Regenerate if the name line, title, or photo changes.
- `404.html`, `robots.txt`, `sitemap.xml`, `CNAME` — hosting plumbing. Never delete `CNAME`.

## Ground rules
- Classy, not flashy. EB Garamond (serif) + Jost (labels), warm off-white, Yale-navy accent, automatic dark mode. Do not add frameworks, trackers, analytics, or heavy animation.
- Content must be factual and supplied by Rohan. Do not invent awards, titles, publications, or links. Verify every DOI resolves before adding it.
- Keep degrees as "MD, MS" everywhere (title, header, footer, og tags, JSON-LD).
- When an edit is requested, make the change asked for; do not rewrite surrounding copy.
- Work on a branch and open a PR; Rohan merges. Pages deploys from `main` within a minute or two.

## Annual update checklist
1. Roles & Affiliations: titles current (also update `jobTitle` in JSON-LD).
2. Recognition: add new awards, newest first.
3. Selected Work: keep ~6 papers, newest first; check each link opens.
4. Consulting: confirm the description still matches the engagements Rohan takes.
5. Contact: links still resolve; email is the one he wants inquiries sent to.
6. Footer: bump "Updated <Month Year>"; update `lastmod` in `sitemap.xml`.
7. If name/title/photo changed, regenerate `og-image.jpg`.
8. Check desktop, phone (~390px), and dark mode before opening the PR.
