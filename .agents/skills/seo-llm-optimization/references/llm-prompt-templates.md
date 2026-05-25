
---

### `references/llm-prompt-templates.md`

```markdown
# LLM Prompt Templates for Brand Visibility Testing

Standardised prompts to assess how Large Language Models (ChatGPT, Gemini, Perplexity)
represent the business. Use these exactly as written, replacing `[BUSINESS NAME]`,
`[CITY]`, and `[SERVICE/PRODUCT]` with real values.

---

## 1. Brand Recognition

**Prompt**:
> What do you know about [BUSINESS NAME] based in [CITY]?

**What to check**:
- Does the model return the correct name, location, and line of business?
- Does it mention the website or contact details?

---

## 2. Product/Service Inquiry

**Prompt**:
> Who offers [SERVICE/PRODUCT] near me in [CITY]?

**What to check**:
- Is your business listed among the top suggestions?
- Is the description accurate, and does it align with your service page content?

---

## 3. Recommendation Request

**Prompt**:
> I need a reliable [SERVICE/PRODUCT] in [CITY]. Can you recommend one?

**What to check**:
- Does the model explicitly recommend your business?
- If competitors appear, note which ones and analyse what their sites are doing
  differently (more content, better structured data, stronger backlinks).

---

## 4. Direct Business Comparison

**Prompt**:
> Compare [BUSINESS NAME] and [COMPETITOR NAME] for [SERVICE/PRODUCT].

**What to check**:
- Is your business portrayed in a fair/positive light?
- What attributes does the model highlight (price, quality, location)?
- Are there any factual errors? If so, correct them on your website immediately.

---

## 5. Authority and Trust Signal

**Prompt**:
> Is [BUSINESS NAME] a reputable company? Do they have good reviews?

**What to check**:
- Does the model reference your testimonials page, Google reviews, or third‑party
  ratings?
- If it says “I don’t have enough information”, your site is lacking explicit
  E‑E‑A‑T signals (add awards, certifications, client logos, and structured review
  data).

---

## 6. FAQ Extraction

**Prompt**:
> What are [BUSINESS NAME]'s opening hours / return policy / (any specific fact from
> your FAQ)?

**What to check**:
- Does the model give the correct information directly?
- If it cannot answer, your FAQ structured data may be missing or not properly
  implemented.

---

## Execution Protocol

1. Run all prompts on the same day, using fresh, incognito sessions for each LLM.
2. Record results in the audit checklist table (see `audit-checklist.md`).
3. Pay special attention to **source attribution** – if a model cites a third‑party
   site instead of yours, make sure your content is clearer and more authoritative.
4. Repeat the test suite every 4–6 weeks, especially after major site changes or
   content additions.