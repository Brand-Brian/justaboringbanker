# Just a Boring Banker — justaboringbanker.com

World-class rebuild of Ryan Garneau's personal finance education site.
Static HTML/CSS/JS, deployed on Netlify from GitHub.

**Start here:** `CLAUDE.md` (project rules) → `docs/` (brand, content, design, roadmap).

## Deploy (first time, ~10 minutes)

1. **GitHub:** create a repo (e.g. `justaboringbanker`), then from this folder:
   ```
   git init && git add -A && git commit -m "Initial rebuild"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/justaboringbanker.git
   git push -u origin main
   ```
2. **Netlify:** Add new site → Import from GitHub → pick the repo. No build command,
   publish directory `.` (already set in `netlify.toml`). Deploy.
3. **Forms:** in Netlify → Forms, confirm `boring-brief` was detected. Add an email
   notification so Ryan sees signups.
4. **Domain:** Netlify → Domain settings → add `justaboringbanker.com`, update DNS
   at the registrar. HTTPS is automatic.

## Before pointing the domain (launch checklist)

- [ ] Replace all `[PLACEHOLDER]` text in `about.html` with Ryan's real bio/credentials
- [ ] Drop real assets into `assets/` (Alex SVG, headshot, banner) and swap the
      `alex-placeholder.svg` references
- [ ] Copy the four calculator HTML files from the current site into
      `/tools/html_machines/` and switch the machine links to relative paths
- [ ] Fix/confirm social URLs in the footers (X handle, Facebook page)
- [ ] Add a contact email to the footer

Full status: `docs/ROADMAP.md`.

## Local preview

Open `index.html` in a browser, or `npx serve .`
