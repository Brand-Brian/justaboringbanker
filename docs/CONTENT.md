# CONTENT.md — Page-by-page content strategy + EEAT

## EEAT requirements (site-wide)

Google's Experience, Expertise, Authoritativeness, Trust — critical for a finance
site (YMYL category, held to the highest standard).

- **Experience/Expertise:** Real bio on `about.html` with Ryan's actual banking
  career, years, and credentials. All `[PLACEHOLDER]` markers must be replaced by
  Ryan with true facts — never invented.
- **Authoritativeness:** `Person` schema on About, `ItemList`/`VideoObject` schema
  on Series, `sameAs` links to the verified YouTube channel and socials. Author
  attribution on any future articles.
- **Trust:** Educational disclaimer in every footer. Working contact method.
  HTTPS (Netlify default). Privacy policy before any analytics are added.

## Conversion map

Primary: **Subscribe on YouTube** (the series is the engine).
Secondary: **The Boring Brief** email signup (Netlify Forms) — owns the audience
long-term.

Every page has exactly one primary CTA. Don't stack competing asks.

## Pages

### index.html — Home
Job: explain the premise in 5 seconds, route people to the series or the machines.
1. Hero — "Boring builds wealth." + Alex + two CTAs (Watch / Try the machines)
2. The Wealth Building Blocks — four pillars, in order: Understanding, Actions, Protect
   and Grow, Goals and Legacy (matches Ryan's video framework — keep the naming and order
   exact if this section changes again)
3. The Machines — six calculator cards
4. The series — teaser + YouTube subscribe
5. The Boring Brief — email capture
6. Footer — disclaimer, socials, contact

Site positioning is global, not Canada-only (confirmed by Ryan Sept 16): default to
tax-free / tax-deferred account language (TFSA/Roth IRA, RRSP/IRA/401(k)) rather than
Canadian terms alone. Ryan's own examples and career are Canadian — that's fine — but
the site's framing shouldn't read as Canada-exclusive.

### about.html — About Ryan
The EEAT workhorse. Real headshot, real bio, credentials list, "why boring"
origin story, Person schema. CTA: watch the series.

### series/index.html — The show
Hub for the YouTube series in development. Channel embed/link, episode cards
(placeholder until episodes ship), subscribe CTA, VideoObject schema per episode
once live.

### tools/index.html — The Machines
Hub listing six calculators with one-line descriptions of what each teaches:
- The Hindsight Machine — what your money would have done
- Withdrawal Scenarios — how long the money lasts
- Allocation in Action — what your mix actually does
- Actions vs Consequences — the cost of emotional decisions
- The Fee Machine — MER drag over time
- The Debt Machine — avalanche vs snowball

The first four were rebuilt in-brand from behaviour (Ryan's original source wasn't
retrievable at the time). Ryan has since sent the real HTML for those four — restyle
the shell only, keep his Plotly/noUiSlider logic as-is — but the data files those
files depend on (`allocation_data.js`, `hindsight_data.json`) are still missing; see
`docs/ROADMAP.md`. On every game with Buy/Sell, the timeline's "today" handle must
lock against backdating once a trade is made — don't regress this.

### resources/index.html — The Boring Library
Order (per Ryan, Sept 16): Budget, Emergency Fund, Panic Protocol, New Investor
Checklist, Debt Repayment, Tax-Free vs Tax-Deferred, Saving for a Home, Children's
Education, Fee Check. FHSA/RESP guides are Canada-rooted (accurate — Ryan's real
expertise) but name each country's closest equivalent (US state first-home programs,
529 Plans) rather than presenting as Canada-only.

## Content Ryan must supply (blocking)

1. Bio facts + credentials for About
2. Real headshot + Alex SVG + banner assets
3. Episode titles/dates as the series ships
4. Confirmation of the conversion hierarchy above

## SEO/GEO layer (Sept 10)
- Person schema: Vancouver/BC/CA address, Canadian knowsAbout terms; visible "based in Vancouver" line on About (CONFIRM with Ryan)
- FAQPage schema + visible FAQ on homepage; Article schema + byline on every guide
- llms.txt at root for AI answer engines; en-CA locale; og:image = Ryan portrait
- Titles carry "Canadian" qualifiers on hub pages; guides stay topic-first
- BIGGEST remaining lever: point justaboringbanker.com at Netlify — canonicals already reference the real domain
