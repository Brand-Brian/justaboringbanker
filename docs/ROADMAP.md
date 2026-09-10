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
- [x] The Toolkit (Sept 10): curated, link-verified official Canadian resources (FCAC/canada.ca calculators, CRA + Service Canada accounts, CIRO AdvisorReport, OBSI, free credit reports, CDIC) — new nav tab
- [x] Site-wide footer site map: every machine + learn section linked from every page
- [x] Resources library (Sept 10): hub + 8 Canadian evergreen guides (budget, debt, TFSA/RRSP, FHSA, emergency fund, fees, panic protocol, new investor), all in-brand with checklists; Resources added to nav site-wide
- [x] CTA fix: nav-button specificity bug (black-on-green) fixed; YouTube icon added to all subscribe CTAs
- [x] All four machines rebuilt in-brand (Sept 10): shared engine + approx. annual historical data, GIC framing, mobile-friendly, same filenames as original for URL continuity

## Blocked on Ryan (before launch)

- [x] About rebuilt (Sept 10) with real story: 23 years at TD Wealth, Ryan's mission quote, both headshots; nav renamed "Meet the Banker"
- [ ] Optional from Ryan: professional designations/licences to strengthen EEAT further
- [x] Real Alex in header + favicon (extracted from original banner, Sept 10); homepage hero now Ryan's portrait
- [ ] Nice-to-have from Ryan: high-res/vector Alex for large-size use (current extraction is 100px — fine at header size, too soft for heroes)
- [ ] Ryan to sanity-check the rebuilt machines against his originals (logic was rebuilt from behaviour, not copied — his source wasn't retrievable)
- [ ] Confirm conversion hierarchy: YouTube primary, Boring Brief secondary (working assumption)
- [ ] Contact email for footer

## Next build phases

1. ~~Calculator restyle~~ — done; next: consider monthly-granularity data + TSX index option
2. **Episode rollout** — real episode cards + VideoObject schema as videos ship
3. **Privacy policy page** — required before adding analytics
4. **Article template** — author byline + schema, for future written content
5. **Lighthouse pass** — target 95+ across the board before announcing

## Decisions log

- Static HTML, no framework — keeps Ryan's calculators portable, zero build step
- Fraunces + IBM Plex Sans — ledger-with-a-wink, both free
- Newsletter named "The Boring Brief" — on-brand, confirm with Ryan
