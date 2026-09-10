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
2. Why boring wins — the four pillars as ledger line items
3. The Machines — four calculator cards (Ryan's existing tools)
4. The series — teaser + YouTube subscribe
5. The Boring Brief — email capture
6. Footer — disclaimer, socials, contact

### about.html — About Ryan
The EEAT workhorse. Real headshot, real bio, credentials list, "why boring"
origin story, Person schema. CTA: watch the series.

### series/index.html — The show
Hub for the YouTube series in development. Channel embed/link, episode cards
(placeholder until episodes ship), subscribe CTA, VideoObject schema per episode
once live.

### tools/index.html — The Machines
Hub listing the four calculators with one-line descriptions of what each teaches:
- The Hindsight Machine — what your money would have done
- Withdrawal Scenarios — how long the money lasts
- Allocation in Action — what your mix actually does
- Actions vs Consequences — the cost of emotional decisions

Calculator HTML files are Ryan's existing work — copy them into `/tools/` from the
current site, restyle the shell only, audit each at 360px width.

## Content Ryan must supply (blocking)

1. Bio facts + credentials for About
2. Real headshot + Alex SVG + banner assets
3. Episode titles/dates as the series ships
4. Confirmation of the conversion hierarchy above
