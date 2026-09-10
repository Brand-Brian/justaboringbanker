# DESIGN.md — Design system

Concept: **a bank statement that came alive.** Quiet, precise, institutional — with
one playful device (the highlighter annotation) carrying the personality.

## Tokens (source of truth: `assets/css/style.css` `:root`)

Color
- `--ink: #10201A` — green-cast near-black, all text
- `--vault: #1D4D3B` — banker's green, buttons/accents
- `--mint-1: #7BE0A8` / `--mint-2: #2FA872` — the Alex gradient
- `--paper: #FAFAF7` — background
- `--highlight: #F5D547` — highlighter yellow, annotation + focus states
- `--rule: #D9E0DA` — ledger rule lines

Type
- Display: **Fraunces** (500–700). Hero uses `clamp(2.4rem, 6vw, 4.2rem)`.
- Body: **IBM Plex Sans** (400/500/600), 1.0625rem, line-height 1.65.
- Left-aligned throughout. Line length ≤ 70ch.

Layout
- Content max-width 1060px, 24px side padding on mobile.
- Section rhythm: 96px desktop / 64px mobile.
- **Ledger rules** (1px `--rule` horizontal lines) structure list content — they
  encode "statement," they are not decoration.
- **Cards only for the calculators** — they're distinct interactive tools. Radius
  14px, border `--rule`, no drop shadows.

## The annotation device

A hand-drawn highlighter underline (inline SVG stroke, `--highlight`) under one
word per page. It's the teacher's marker on your statement. One per page, max.

## Motion

One moment: hero fades up on load. Nothing else animates uninvited.
`prefers-reduced-motion` disables it. Hover states change color/border only.

## Accessibility floor

- Contrast ≥ 4.5:1 for text (ink on paper passes everywhere)
- Visible keyboard focus (highlighter yellow outline)
- Semantic HTML: one `h1` per page, landmarks, alt text on all images
- Touch targets ≥ 44px; nav collapses to a toggle below 760px

## Anti-patterns (never)

Gradient washes as decoration · identical rounded cards for everything ·
all-caps eyebrow labels · scroll-triggered animation on every section ·
"→" appended to links · stock finance photography (charts going up, handshakes)
