# ROADMAP.md — Status and next steps

_Last updated: 10 Sept 2026 (initial build)_

## Done

- [x] Repo scaffold, docs (CLAUDE / BRAND / CONTENT / DESIGN / ROADMAP)
- [x] Design system stylesheet (`assets/css/style.css`)
- [x] Home (`index.html`) — hero, pillars, machines, series teaser, Boring Brief signup
- [x] About (`about.html`) — structure + Person schema, **credentials are placeholders**
- [x] Series hub (`series/index.html`) — channel CTA + placeholder episode grid
- [x] Machines hub (`tools/index.html`)
- [x] `netlify.toml`, `robots.txt`, `sitemap.xml`, 404 page
- [x] Boring Brief form wired to Netlify Forms

## Blocked on Ryan (before launch)

- [ ] Replace every `[PLACEHOLDER]` in `about.html` with real bio/credentials — EEAT-critical, do not invent
- [ ] Supply real assets → `assets/icons/` and `assets/images/` (Alex SVG, headshot, banner); placeholder Alex is a stand-in
- [ ] Copy the four calculator HTML files from the current site into `/tools/` (links currently point at the live justaboringbanker.com URLs so nothing breaks meanwhile)
- [ ] Confirm conversion hierarchy: YouTube primary, Boring Brief secondary (working assumption)
- [ ] Contact email for footer

## Next build phases

1. **Calculator restyle** — wrap each tool in the new shell, audit at 360px
2. **Episode rollout** — real episode cards + VideoObject schema as videos ship
3. **Privacy policy page** — required before adding analytics
4. **Article template** — author byline + schema, for future written content
5. **Lighthouse pass** — target 95+ across the board before announcing

## Decisions log

- Static HTML, no framework — keeps Ryan's calculators portable, zero build step
- Fraunces + IBM Plex Sans — ledger-with-a-wink, both free
- Newsletter named "The Boring Brief" — on-brand, confirm with Ryan
