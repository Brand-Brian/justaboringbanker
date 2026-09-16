# CLAUDE.md — Just a Boring Banker

Read this first. Then read the doc relevant to your task before touching anything:
- Writing copy → `docs/BRAND.md` + `docs/CONTENT.md`
- Building/styling pages → `docs/DESIGN.md`
- Checking status or what's next → `docs/ROADMAP.md`

## What this is

The website for **Ryan Garneau's "Just a Boring Banker"** — a personal finance education
persona. Positioning: *Financial clarity for the rest of us.* Boring is the edge:
excitement in finance is usually expensive.

Think Bill Nye the Science Guy, but for money — enthusiastic about unsexy fundamentals,
visual, funny, never condescending. Alex (the green avatar) is the recurring mascot.

## Tech constraints — do not deviate

- **Static HTML/CSS/JS only.** No frameworks, no build step. One stylesheet:
  `assets/css/style.css`.
- **Mobile-first and responsive.** Every page and every calculator must work at 360px.
- **Deploys on Netlify from GitHub `main`.** Config lives in `netlify.toml`.
- Fonts: Fraunces + IBM Plex Sans via Google Fonts. Nothing else.
- Forms use Netlify Forms (`data-netlify="true"`), no backend.

## Hard rules

1. **Never fabricate credentials.** Ryan's bio, years of experience, and certifications
   in `about.html` use `[PLACEHOLDER]` markers until Ryan supplies real facts. EEAT
   depends on them being true. Ryan does not want his 23 years named as TD Wealth —
   use "one of Canada's large wealth management firms" instead. Total career: 30 years
   (23 in wealth management + 10 teaching Financial Planning at BCIT — these overlap).
2. **Every page with financial content carries the disclaimer** (in the footer):
   educational content, not financial advice.
3. **Never strip Alex or the "boring" framing.** They are the brand.
4. **Never make it sound like a bank.** No "unlock your wealth potential," no hype,
   no jargon. Voice rules live in `docs/BRAND.md`.
5. **Don't break the calculators.** The six HTML tools in `/tools/html_machines/` are
   restyled/rebuilt in-brand (Sept 10) since Ryan's original source wasn't available at
   the time. Ryan has since sent his real four calculators (Plotly + noUiSlider,
   real S&P 500 data), but the zip only contained the HTML shells — the data files
   `allocation_data.js` and `hindsight_data.json` they depend on were not included.
   **Do not swap in the new shells until those two files are supplied** — they'd ship
   broken (undefined data, failed fetch). Once supplied, wrap them in the site header/
   footer and brand CSS variables, but preserve Ryan's logic as-is per rule below.
6. **Global positioning (Sept 16):** JBB is for everyone, not just Canadians. Default
   to "tax-free account (TFSA, Roth IRA)" / "tax-deferred account (RRSP, IRA, 401(k))"
   framing rather than TFSA/RRSP alone. Country-specific guides (FHSA, RESP) stay
   Canada-rooted but name the closest equivalent elsewhere (US state first-home
   programs, 529 Plans). Ryan's teaching example throughout is still Canadian — that's
   fine, just don't imply the site itself is Canada-only.
7. Primary conversion is **YouTube subscribe**; secondary is **The Boring Brief**
   email signup. Don't add other CTAs without checking `docs/ROADMAP.md`.

## Deploy

Push to `main` → Netlify auto-deploys. Local preview: open `index.html` in a browser
or `npx serve .`
