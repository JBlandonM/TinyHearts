---
name: seo-llm-optimization
description: >
  Use this skill when building, auditing, or optimizing a business website to rank well
  in search engines (Google) AND to be accurately understood and cited by Large Language
  Models (ChatGPT, Gemini, Perplexity, etc.). Covers technical foundations, on-page SEO,
  semantic content for LLMs, Schema.org structured data, external authority building,
  and continuous monitoring. Trigger when the user mentions SEO, search engine ranking,
  Google visibility, LLM discoverability, AI search optimization, website audit,
  Schema.org markup, or GEO (Generative Engine Optimization).
license: MIT
metadata:
  author: dev-team
  version: "1.0"
  category: web-development
---

# SEO & LLM Optimization — Implementation & Audit Skill

## Overview

This skill provides a complete, phase-by-phase workflow to build and verify a business
website that performs well in two complementary discovery channels:

1. **Traditional search engines** (Google, Bing) — via ranking signals and rich results.
2. **Large Language Models** (ChatGPT, Gemini, Perplexity) — via semantic clarity and
   structured data that LLMs ingest during training and retrieval-augmented generation.

The skill is divided into **six implementation phases** followed by a **four-area audit
framework** for ongoing verification. Follow the phases in order when building from
scratch. Jump directly to the audit framework when evaluating an existing site.

---

## PHASE 1 — Technical Foundations

### 1.1 Ensure crawlability and indexability
1. Verify the entire site is served over **HTTPS** with a valid certificate.
2. Create or review the `robots.txt` file: ensure it does NOT block CSS, JavaScript,
   images, or any critical path the site needs to render properly.
3. Generate an **XML sitemap** that includes all indexable pages. Submit it via
   Google Search Console and reference it in `robots.txt`.
4. Design every URL to be **descriptive, short, and human-readable**
   (e.g., `/services/digital-marketing` instead of `/index.php?page=123`).

### 1.2 Optimize performance and mobile experience
1. Compress and convert all images to modern formats (WebP/AVIF) with appropriate
   dimensions. Eliminate unused CSS and JavaScript (tree-shaking, code-splitting).
2. Implement a **responsive design** that works flawlessly on all device widths.
   Test on real mobile devices, not just viewport resizers.
3. Ensure navigation is intuitive: the user should reach any important page within
   three clicks from the homepage.
4. Minimize render-blocking resources. Defer non-critical JavaScript.

### 1.3 Establish clear information architecture
1. Define a logical hierarchy: Homepage → Main sections → Sub-pages.
2. Use **internal links** with descriptive anchor text that reflects the thematic
   relationship between source and target pages.
3. Ensure every important page is linked from at least one other page on the site.

---

## PHASE 2 — On-Page Optimization

### 2.1 Metadata and tags
1. Craft a **unique, descriptive title tag** per page (max 60 characters). Include
   the primary keyword near the beginning and the brand name where relevant.
2. Write a **compelling meta description** (max 160 characters) that summarizes the
   page's value proposition and includes a soft call to action.
3. Use exactly **one H1 heading** per page, aligned with the title tag's topic.
4. Structure subsequent headings (H2, H3, H4) in a strict hierarchical order
   without skipping levels. The heading outline should make sense if read in isolation.

### 2.2 Semantic content and multi-format presentation
1. Write in **natural, conversational language** that directly answers the questions
   your ideal customer would ask.
2. Organize content into short paragraphs, bulleted lists, tables, and
   **FAQ blocks** — structured formats are easier for both humans and LLMs to parse.
3. For every image, provide a descriptive `alt` attribute that explains what the
   image depicts in context. For videos and audio, include transcripts or detailed
   textual descriptions.

### 2.3 Demonstrate authority and trust (E-E-A-T)
1. Create a dedicated **"About Us" page** covering the business's history, mission,
   team members, and any certifications, awards, or professional affiliations.
2. Showcase **real testimonials, case studies, and client logos** with verifiable
   attribution.
3. Cite and link to reputable external sources when presenting factual claims.
4. Display complete **contact information**: physical address, phone number, email,
   and links to verified social media profiles.

---

## PHASE 3 — LLM-Specific Content Strategy

### 3.1 Define and cover business entities comprehensively
1. Describe the business as a **complete entity**: what it does, where it operates,
   what products or services it offers, and what problems it solves.
2. Create dedicated, detailed pages for each **service**, **product**, and
   **geographic location**, covering attributes such as pricing, features,
   availability, and service area.
3. Build a thorough **FAQ section** using real customer questions. Answer each one
   concisely and directly — LLMs extract knowledge most reliably from well-defined
   question-answer pairs.

### 3.2 Use formats that AI models parse best
1. Open each important page with a **2–3 sentence summary** that distills the core
   answer. This favors both featured snippets in Google and accurate extraction by LLMs.
2. Use **numbered steps or bulleted lists** for procedures, feature comparisons,
   and specifications.
3. Include a **"Key Concepts" section or glossary** when operating in a specialized
   domain with technical terminology.
4. Close articles with a **"Key Takeaways" or conclusion paragraph** that reinforces
   the main points.

---

## PHASE 4 — Structured Data (Schema.org)

### 4.1 Implement JSON-LD markup
Add structured data in **JSON-LD format** (Google's recommended syntax) for each
of the following entity types, as applicable:

- **Organization / LocalBusiness**: `name`, `logo`, `address`, `telephone`,
  `openingHours`, `geo` coordinates, `sameAs` links to social profiles.
- **Product**: `name`, `description`, `offers` (with `price` and `availability`),
  `aggregateRating`.
- **Service**: `name`, `description`, `areaServed`, `provider`.
- **FAQPage**: each question with its accepted answer.
- **HowTo**: step-by-step guides with `name`, `description`, and `step` entries.
- **Article / BlogPosting**: `headline`, `author`, `datePublished`, `dateModified`,
  `image`.

### 4.2 Validate and connect
1. Validate all markup using the **Schema Markup Validator** (schema.org) and the
   **Rich Results Test** (Google). Fix every error.
2. In the `Organization` schema, use the `sameAs` property to link to the official
   Google Business Profile, Wikidata entry, Wikipedia page, and major directory
   listings. These must have **identical NAP data** (name, address, phone).

---

## PHASE 5 — External Authority and Reputation

### 5.1 Quality link building
1. Pursue backlinks from **relevant, authoritative sites** in your industry:
   professional associations, chambers of commerce, trade publications, and
   reputable niche directories.
2. Prioritize link quality over quantity. A single link from an industry-leading
   publication outweighs dozens from low-quality directories.
3. Earn mentions as a cited source in articles, press releases, and research
   studies — LLMs learn from brand mentions in authoritative texts.

### 5.2 Knowledge platform presence
1. Optimize your **Google Business Profile**: upload real photos, maintain accurate
   hours, select precise categories, and actively respond to reviews.
2. Where appropriate, create or update the business's **Wikidata entry** with
   references to the official website and reliable third-party sources. This feeds
   directly into Google's Knowledge Graph and LLM training corpora.

---

## PHASE 6 — Monitoring and Continuous Improvement

### 6.1 Search engine signals
1. Review **Google Search Console** regularly for crawl errors, mobile usability
   issues, and the search queries generating impressions.
2. Identify pages ranking near the top positions and reinforce them with better
   content, additional internal links, or more detailed structured data.

### 6.2 Content freshness and accuracy
1. Update dates, prices, hours, and any time-sensitive information promptly.
   Stale data propagates through both search indexes and LLM snapshots.
2. Add new FAQ entries as customer questions emerge.
3. Publish fresh content regularly (blog posts, industry news, guides) to signal
   vitality and broaden the site's topical coverage.

### 6.3 LLM visibility testing
1. Periodically query ChatGPT, Gemini, and Perplexity about the business, its
   products, and its services. Assess whether responses are accurate and complete.
2. If gaps are found, reinforce those areas on the website: add dedicated pages,
   enhance structured data, or publish an article directly addressing that query.
3. Ensure all critical information lives in **plain HTML text**, not solely in
   images, JavaScript-rendered elements, or iframes — LLMs and crawlers must be
   able to read it directly.

---

## AUDIT FRAMEWORK — Four-Area Measurement System

For verifying that the above characteristics are correctly implemented, use this
four-area diagnostic framework. Perform these checks at regular intervals (e.g.,
per sprint or monthly). Detailed procedures and tool configurations are available in
`references/audit-checklist.md`.

### Area 1: Technical Diagnostics (Performance & Health)
**Objective**: Evaluate speed, user experience, and indexing health.

**Core Web Vitals targets**:
| Metric | Full Name | Target |
|--------|-----------|--------|
| LCP | Largest Contentful Paint | ≤ 2.5 seconds |
| INP | Interaction to Next Paint | ≤ 200 milliseconds |
| CLS | Cumulative Layout Shift | ≤ 0.1 |

**Manual verifications**:
- Site loads under HTTPS with no mixed-content warnings.
- `robots.txt` does not block CSS, JS, or key images.
- XML sitemap is accessible and submitted to Search Console.
- URLs are descriptive and free of unnecessary parameters.

### Area 2: On-Page Analysis (Content & Metadata)
**Objective**: Verify each page is semantically optimized and readable.

**Key checks per page**:
- Title and meta description are unique, correctly sized, and include the target keyword.
- Exactly one H1 exists; heading hierarchy (H2→H3) has no gaps.
- Content is scannable: short paragraphs, lists, bold key phrases.
- All images have descriptive `alt` text; videos include transcripts.

### Area 3: Semantic Comprehension (Structured Data)
**Objective**: Ensure Schema.org markup is valid and complete.

**Verification checklist**:
- `Organization`/`LocalBusiness` present on homepage or contact page.
- `Product` markup on product pages; `Service` markup on service pages.
- `FAQPage` markup wherever FAQ content appears.
- `Article`/`BlogPosting` markup on all blog content.
- Zero critical errors in the Schema Markup Validator.

### Area 4: AI Visibility (LLM Presence)
**Objective**: Measure whether LLMs understand and recommend the business correctly.

**Testing protocol**:
1. Define 10–15 questions a potential customer would ask about the business.
2. Pose each question to ChatGPT, Gemini, and Perplexity.
3. Record: Does the brand appear? Is the information correct? What source is cited?
4. Track AI Share of Voice using tools like Ahrefs Brand Radar or Sistrix AI
   Visibility Index.
5. If citations come from sources other than your website, reinforce your own
   content on those topics.

---

## References

When detailed procedures are required beyond what is covered here, direct the agent to
load the appropriate reference file:

- **`references/audit-checklist.md`** — Step-by-step audit procedures with tool
  configurations, specific validation commands, and troubleshooting guides for each
  of the four audit areas.
- **`references/schema-examples.md`** — Complete JSON-LD examples for each Schema.org
  type relevant to a local business website.
- **`references/llm-prompt-templates.md`** — Standardized prompt templates for
  testing brand visibility across different LLM platforms.

Load these files **on demand** when the agent needs granular, procedural detail
beyond the core instructions in this SKILL.md.