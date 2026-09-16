# ROADMAP.md — Status and next steps

_Last updated: 16 Sept 2026_

## Done

- [x] Repo scaffold, docs (CLAUDE / BRAND / CONTENT / DESIGN / ROADMAP)
- [x] Design system stylesheet (`assets/css/style.css`)
- [x] Home (`index.html`) — hero, pillars, machines, series teaser, Boring Brief signup
- [x] About (`about.html`) — structure + Person schema, **credentials are placeholders**
- [x] Series hub (`series/index.html`) — channel CTA + placeholder episode grid
- [x] Machines hub (`tools/index.html`)
- [x] `netlify.toml`, `robots.txt`, `sitemap.xml`, 404 page
- [x] Boring Brief form wired to Netlify Forms
- [x] Blind mode on both trading games (Sept 10): random hidden stretch of history, unlabeled years (Y1, Y2...), panic shading off, reveal at the end — preserves the original site's you-can't-see-what's-coming mechanic; Actions vs Consequences defaults to blind
- [x] Two new machines (Sept 10): The Fee Machine (MER drag, twin-run comparison) and The Debt Machine (avalanche vs snowball race, budget-based amortization) — grid now 6, balanced
- [x] Mobile pass: 16px input floor (stops iOS zoom), 44px checkbox tap targets, viewport verified on all 21 pages, every internal link audited and resolving
- [x] The Toolkit (Sept 10): curated, link-verified official Canadian resources (FCAC/canada.ca calculators, CRA + Service Canada accounts, CIRO AdvisorReport, OBSI, free credit reports, CDIC) — new nav tab
- [x] Site-wide footer site map: every machine + learn section linked from every page
- [x] Resources library (Sept 10): hub + 8 Canadian evergreen guides (budget, debt, TFSA/RRSP, FHSA, emergency fund, fees, panic protocol, new investor), all in-brand with checklists; Resources added to nav site-wide
- [x] CTA fix: nav-button specificity bug (black-on-green) fixed; YouTube icon added to all subscribe CTAs
- [x] All four machines rebuilt in-brand (Sept 10): shared engine + approx. annual historical data, GIC framing, mobile-friendly, same filenames as original for URL continuity

## Blocked on Ryan (before launch)

- [x] About rebuilt (Sept 10) with real story, updated Sept 16 to drop TD Wealth naming; nav renamed "Meet the Banker"
- [ ] Optional from Ryan: professional designations/licences to strengthen EEAT further
- [x] Real Alex in header + favicon (extracted from original banner, Sept 10); homepage hero now Ryan's portrait
- [ ] Nice-to-have from Ryan: high-res/vector Alex for large-size use (current extraction is 100px — fine at header size, too soft for heroes)
- [ ] **Blocking, new (Sept 16):** Ryan sent his real four calculators (`html_machines.zip` — Plotly + noUiSlider, real S&P 500 data), but the zip only had the HTML shells. `Allocation_in_Action.html`, `Withdrawal_Scenarios.html`, and `action_versus_consequences.html` all load a missing `allocation_data.js`; `The_Hindsight_Machine.html` fetches a missing `hindsight_data.json`. **Need both files from Ryan** before the real calculators can replace the in-brand rebuilds. Once received: wrap in site header/footer + brand CSS variables, keep his logic verbatim per CLAUDE.md rule 5.
- [ ] Confirm conversion hierarchy: YouTube primary, Boring Brief secondary (working assumption)
- [ ] Contact email for footer

## Next build phases

1. Swap in Ryan's real calculators once `allocation_data.js` + `hindsight_data.json` arrive; consider weekly-granularity data at that point too (Ryan wants more chart detail than the current annual series gives)
2. **Episode rollout** — real episode cards + VideoObject schema as videos ship (now: Wealth Building Blocks / Forward Looking Cash Flow / Taxes in Plain Language / Debt Repayment)
3. **Privacy policy page** — required before adding analytics
4. **Article template** — author byline + schema, for future written content
5. **Lighthouse pass** — target 95+ across the board before announcing

## Decisions log

- Static HTML, no framework — keeps Ryan's calculators portable, zero build step
- Fraunces + IBM Plex Sans — ledger-with-a-wink, both free
- Newsletter named "The Boring Brief" — on-brand, confirm with Ryan
- **Sept 16 — Ryan's full feedback pass incorporated:** homepage pillars rewritten as the
  Wealth Building Blocks (Understanding / Actions / Protect and Grow / Goals and Legacy);
  About page drops "TD Wealth" for generic framing, adds BCIT teaching + speaking-tour
  ambition, drops fee-focused/industry-bashing tone; Series "what's coming" now matches
  Ryan's real upcoming episodes; site repositioned as global rather than Canada-only
  (tax-free/tax-deferred framing site-wide); Resources reordered per Ryan (Budget,
  Emergency Fund, Panic Protocol, New Investor Checklist, Debt Repayment, Tax-Free vs
  Tax-Deferred, Saving for a Home, Children's Education, Fee Check); Fee Check trims the
  "what 2% costs" math section; Boring Budget rewritten around Forward Looking Cash Flow
  (timing-based expense mapping, pay-period drift example, buffer amount) instead of
  50/30/20; timeline slider on Allocation in Action / Actions vs Consequences now locks
  against backdating once a trade is made.
