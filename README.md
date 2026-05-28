# Tiny Hearts 0130 — Landing Page

Mobile childcare services landing page for Tiny Hearts 0130, Costa Rica.

## Deploy

Push to `main` branch → GitHub Pages auto-deploys from `https://jblandonm.github.io/TinyHearts/`.

### Before deploy

Minify CSS and JS for production using [minifier.org](https://minifier.org):

1. Open https://minifier.org
2. Paste `style.css` content → copy minified output → save as `style.css`
3. Paste `main.js` content → copy minified output → save as `main.js`
4. Commit and push

> Alternatively, use a local tool: `npx cssnano style.css style.css && npx terser main.js -o main.js`

## Project structure

```
├── index.html              Main landing page
├── 404.html                Custom 404 page
├── style.css               All styles (single file)
├── main.js                 All scripts (single file)
├── privacy-policy.html     Privacy policy
├── terms-of-service.html   Terms of service
├── robots.txt              Crawler rules
├── sitemap.xml             XML sitemap
├── paletas.svg             Color palette reference for client
├── .gitignore
├── docs/                   Documentation
├── email-templates/        EmailJS HTML templates
└── tests/                  Playwright E2E tests
```
