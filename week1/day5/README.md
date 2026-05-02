# Day 5 — Building a Mini LLM Pipeline Project

## Project Link

🔗 https://github.com/srilekha42/ai-brochure-generator

---

## What I Built

A complete pipeline-based system that:

* Scrapes website content
* Extracts and filters internal links
* Identifies important pages (About, Docs, Careers)
* Cleans noisy HTML content
* Generates structured brochure output

---

## Architecture

```
URL
 → Scraper
 → Link Extractor
 → Link Filter
 → Content Selector (About Page)
 → Brochure Generator
```

---

## Key Learnings

* Handling unreliable web scraping using retries and sessions
* Filtering useful data from noisy HTML
* Importance of selecting the right data source (About page)
* Designing modular pipelines similar to LLM systems

---

## Insight

Instead of summarizing the homepage directly, selecting the **About page** significantly improves output quality.

---

## Future Improvements

* Replace rule-based filtering with LLM
* Improve summarization using AI
* Build UI or API layer
