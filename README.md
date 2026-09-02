# Tiny Hearts 0130 — Landing Page

Mobile childcare services landing page for Tiny Hearts 0130, Costa Rica.

## Deploy

Push to `main` branch → GitHub Actions auto-deploys to `https://tinyhearts0130.com/`.

**Note on Minification:** Do **not** manually minify HTML, CSS, or JS before committing. GitHub Actions (CI) automatically minifies the files into the `dist/` folder during the deployment process using `html-minifier`, `csso`, and `terser`.

## Project structure

```text
├── index.html              Main landing page
├── 404.html                Custom 404 page
├── style.css               All styles (single file)
├── main.js                 All scripts (single file)
├── privacy-policy.html     Privacy policy
├── terms-of-service.html   Terms of service
├── robots.txt              Crawler rules
├── sitemap.xml             XML sitemap
└── .gitignore
```
