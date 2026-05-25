# Audit Checklist & Procedures

Detailed step‑by‑step verification for each of the four audit areas defined in the
main SKILL.md. Perform these checks after every major site update and at least monthly.

---

## 1. TECHNICAL DIAGNOSTICS

### 1.1 Core Web Vitals (via PageSpeed Insights)
1. Open [PageSpeed Insights](https://pagespeed.web.dev).
2. Enter the URL of the homepage and run the test.
3. Record the **Lab Data** for LCP, INP (or TBT as fallback), and CLS.
4. If any metric exceeds the target:
   - **LCP > 2.5s**: Look at “Opportunities” → properly size images, enable text
     compression, remove render‑blocking resources.
   - **INP > 200ms**: Identify long tasks in Lighthouse → break up long JavaScript,
     defer third‑party scripts.
   - **CLS > 0.1**: Locate elements without dimensions; set explicit `width`/`height`
     on images, embeds, and ad slots.
5. Repeat for key internal pages (product, service, blog, contact).

### 1.2 Google Search Console – Coverage & Core Web Vitals
1. Go to **Google Search Console** → **Indexing** → **Pages**.
2. Filter by “Error” and “Warning”. Investigate and fix any URLs that are:
   - Blocked by `robots.txt` (if they should be indexed).
   - Returning 5xx or 4xx status codes.
   - Marked as “Crawled – currently not indexed” (improve content/internal linking).
3. In **Experience** → **Core Web Vitals**, review both desktop and mobile reports.
   Prioritise fixing issues for groups of pages marked “Poor”.

### 1.3 Manual Checks
- [ ] Browse the site in a private window – does every page load over `https://`?
- [ ] Visit `https://yoursite.com/robots.txt` – ensure critical CSS/JS paths are not
  `Disallow`ed.
- [ ] Visit `https://yoursite.com/sitemap.xml` – verify it lists all important pages
  and is not empty. Submit URL to Search Console if new.

---

## 2. ON‑PAGE ANALYSIS

### 2.1 Batch Audit with Semrush / Ahrefs
1. Create a project in Semrush/Ahrefs for the domain.
2. Run the **Site Audit** tool. Under “Issues”, filter by “Errors” and “Warnings”.
3. Focus on:
   - **Missing or duplicate title tags / meta descriptions**.
   - **H1 issues** (multiple, missing, too long).
   - **Low word count** pages (add substantive content where missing).
4. Export the list of affected URLs and assign fixes.

### 2.2 Manual Review of Top 20 Pages
For each important page:
1. **Title & Description**: View page source or use an SEO extension. Confirm title
   is between 50‑60 characters, description 120‑160, both unique and keyword‑rich.
2. **Heading Hierarchy**: Use the “Document Outline” feature in browser developer
   tools. Must show exactly one `<h1>`, followed by `<h2>`, `<h3>` without gaps.
3. **Readability**: Copy the main content into [Hemingway Editor](https://hemingwayapp.com).
   Target Grade 8 or below. Break sentences highlighted as “hard to read”.
4. **Images**: Inspect each `<img>` – every must have a non‑empty `alt` attribute
   describing the image content contextually.
5. **Videos**: Check that a transcript or detailed description exists nearby.

---

## 3. SEMANTIC COMPREHENSION (Structured Data)

### 3.1 Validation
1. Open the [Schema Markup Validator](https://validator.schema.org).
2. Fetch one URL at a time (or paste the HTML/JSON‑LD).
3. Verify zero **errors**. Warnings are acceptable but should be minimised.
4. Run the same URL through Google’s [Rich Results Test](https://search.google.com/test/rich-results)
   to see which rich result types are eligible.

### 3.2 Schema Type Inventory
Use the table below to tick off presence on the relevant pages.

| Schema Type       | Expected on…                      | Present | Validated |
|-------------------|-----------------------------------|---------|-----------|
| Organization / LocalBusiness | Homepage or /contact          | ☐ | ☐ |
| Product           | Each product page                 | ☐ | ☐ |
| Service           | Each service page                 | ☐ | ☐ |
| FAQPage           | Any FAQ section or page           | ☐ | ☐ |
| HowTo             | Step‑by‑step guide articles       | ☐ | ☐ |
| Article / BlogPosting | Each blog post                | ☐ | ☐ |

### 3.3 SameAs Consistency
- Open the `Organization` JSON‑LD block.
- Locate the `sameAs` array.
- Verify every linked profile (Google Business, Facebook, LinkedIn, etc.) exactly
  matches the **name**, **address**, and **phone** on the website.

---

## 4. AI VISIBILITY (LLM Presence)

### 4.1 Manual Prompt Library Testing
1. See `llm-prompt-templates.md` for the full list of test prompts.
2. For each prompt, execute it in a fresh conversation on:
   - ChatGPT (GPT‑4 or 4o)
   - Gemini (Advanced)
   - Perplexity (Pro, with web search enabled)
3. Fill in the tracking table:

| Prompt # | Model    | Brand Mentioned? | Information Correct? | Source Cited | Notes |
|----------|----------|------------------|----------------------|--------------|-------|
| 1        | ChatGPT  | Yes / No         | Yes / No / Partial   | URL / None   |       |
| 1        | Gemini   | Yes / No         | Yes / No / Partial   | URL / None   |       |
| 1        | Perplexity| Yes / No         | Yes / No / Partial   | URL / None   |       |

### 4.2 Automated Monitoring
1. If using **Ahrefs Brand Radar**, configure the project for your brand.
2. Check the **AI Share of Voice** metric weekly. A drop >10% warrants investigation.
3. Review the **Sources** tab – if authoritative external sites are being cited more
   than your own domain, improve content depth and structured data on those topics.

### 4.3 Content Reinforcement Actions
For any prompt where the answer was missing or incorrect:
1. Identify the exact information gap.
2. Create or update a dedicated page on your site that directly addresses that query.
3. Ensure the new content is wrapped in appropriate structured data (e.g., FAQ,
   Article).
4. Resubmit the updated URL in Search Console and re‑test in LLMs after 1‑2 weeks.

---

*Use this checklist as a living document. Tick items after every audit cycle and
keep notes on recurring issues.*