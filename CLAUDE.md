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
   depends on them being true.
2. **Every page with financial content carries the disclaimer** (in the footer):
   educational content, not financial advice.
3. **Never strip Alex or the "boring" framing.** They are the brand.
4. **Never make it sound like a bank.** No "unlock your wealth potential," no hype,
   no jargon. Voice rules live in `docs/BRAND.md`.
5. **Don't break the calculators.** The four HTML tools in `/tools/` are Ryan's
   existing work — restyle their shell, don't rewrite their logic.
6. Primary conversion is **YouTube subscribe**; secondary is **The Boring Brief**
   email signup. Don't add other CTAs without checking `docs/ROADMAP.md`.

## Deploy

Push to `main` → Netlify auto-deploys. Local preview: open `index.html` in a browser
or `npx serve .`
