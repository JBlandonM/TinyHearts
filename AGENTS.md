# AGENTS.md — Tiny Hearts 0130

## Stack
- **Pure vanilla HTML5 + CSS3 + JS (ES6).** No framework, bundler, or package manager.
- No package.json, no npm scripts. No lint/typecheck/format tools.
- Local dev: open `index.html` directly or any static server.

## Deploy
- Push to `main` → GitHub Actions auto-deploys to GitHub Pages.
- CI minifies HTML/CSS/JS in `dist/` using `html-minifier`, `csso`, `terser`. Do **not** manually minify before commit.
- CI copies `email-templates/` into the deploy.

## EmailJS (form backend)
- Keys/IDs live in `main.js:CONFIG` (not env vars).
  - `EMAILJS_PUBLIC_KEY`, `SERVICE_ID`, `TEMPLATE_NOTIFY`, `TEMPLATE_CONFIRM`
- On submit, sends two parallel emails: notify business + confirm client.
- Honeypot field (`#website`) rejects bots client-side.

## Themes
- 4 color variants via `data-theme` attribute on `<html>`: default, `brisa`, `dulce`, `paraiso`.
- CSS variables + blob gradient backgrounds change per theme.

## Testing
- **Python Playwright** (not Node.js). Requires Python 3 + `playwright` installed.
- Launcher: `.\tests\run_tester.ps1` (uses hardcoded Python 3.14 path) or `python tests/tester_agent.py`.
- Spins its own local HTTP server on port 8000. Tests Chromium + Firefox + WebKit.
- Screenshots output to `tests/screenshots/` (gitignored).

## Project conventions
- All code in 3 files: `index.html` (SPA sections), `style.css` (all styles), `main.js` (all JS, loaded via `defer`).
- Navigation: same-page anchor links with `scroll-behavior: smooth`.
- Docs in `docs/` are in Spanish.
- `.agents/skills/` contains OpenCode skill definitions — do not delete.

## Pending Tasks

These tasks are blocked pending the user providing a custom domain. Execute all at once when domain is ready.

- [ ] Replace all `https://jblandonm.github.io/TinyHearts/` with `https://[new-domain]/` across:
  - `index.html` (~14 URLs: OG, Twitter, canonical, JSON-LD)
  - `privacy-policy.html` (canonical + JSON-LD url)
  - `terms-of-service.html` (canonical)
  - `sitemap.xml` (3 `<loc>` entries)
  - `robots.txt` (Sitemap URL)
- [ ] Add hreflang tags (`en` + `x-default`) to `<head>` of all 3 HTML pages
- [ ] Replace `google-site-verification` placeholder with real Search Console code in `index.html`
- [ ] Update `lastmod` in `sitemap.xml`
