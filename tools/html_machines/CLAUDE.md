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
5. **Don't break the calculators.** Four of the six tools in `/tools/html_machines/` —
   `Allocation_in_Action.html`, `Withdrawal_Scenarios.html`, `action_versus_consequences.html`,
   `The_Hindsight_Machine.html` — are now Ryan's real Plotly + noUiSlider builds on real
   weekly S&P 500 data (1988–2026, `allocation_data.js` + `hindsight_data.json`, received
   Sept 18), wrapped in the site header/footer with his own `<style>` block scoped under
   `.rg-machine` (so it can't leak onto the site nav/buttons) and its `--jbb-*` variables
   remapped to the brand palette. **His JS logic is verbatim — never edit the inline
   `<script>` in these four files.** The Fee Machine and The Debt Machine have no "real"
   Ryan version and stay as the in-brand rebuilds (shared `data.js`/`engine.js`).
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
