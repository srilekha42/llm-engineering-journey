# 🚀 LLM Engineering Journey

This repository documents my hands-on learning and practical implementation of Large Language Models (LLMs), focusing on building reliable, real-world systems.

---

## 📌 Week 1 - Foundations

### ✅ Day 1: Basic LLM Interaction

* Connected Python with LLM APIs
* Built a prompt → response pipeline
* Learned basic prompt engineering

---

### ✅ Day 2: Basic LLM Applications

* Used Chat Completions API
* Built a webpage summarizer
* Extracted and cleaned HTML using BeautifulSoup
* Understood token limits and model constraints
* Compared cloud vs local models (Ollama)

---

### ✅ Day 3: LLM Output Control & Reliability

* Learned that LLM outputs are **not reliable by default**
* Implemented structured JSON output
* Added:

  * JSON parsing (`json.loads`)
  * Output validation
  * Retry mechanisms
  * Schema handling
* Built a multi-step pipeline for reliability

---

### ✅ Day 5: Pipeline-Based Project (AI Brochure Generator)

🔗 Project: https://github.com/srilekha42/ai-brochure-generator

* Scraped website content with retry handling
* Extracted and filtered internal links
* Identified key pages (About, Docs, Careers)
* Improved output by prioritizing the About page
* Generated structured brochure output

---

## 🛠️ Projects Built

### 🔹 Chat API

* Implemented system + user message structure
* Used OpenAI-compatible API format

---

### 🔹 Local LLM (Ollama)

* Ran LLM locally without API cost
* Compared local vs cloud models

---

### 🔹 Webpage Summarizer

* Extract webpage content
* Clean HTML
* Generate summary using LLM

---

### 🔹 Structured Summarizer

* Convert webpage → structured JSON
* Handle invalid outputs, schema mismatches, retries

---

### 🔹 AI Brochure Generator (Pipeline System)

* URL → Scraper → Link Filter → Content Selector → Generator
* Demonstrates real-world system design thinking

---

## 🧠 Key Concepts

* LLMs are **probabilistic systems**
* Prompt design impacts output quality
* Parsing converts text → structured data
* Validation ensures correctness
* Reliability requires pipelines, not single calls

---

## ⚙️ Tech Stack

* Python
* OpenAI-compatible APIs
* Ollama (Local LLM)
* BeautifulSoup
* Requests

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
```

### Day 2

```bash
python week1/day2/basic_summarizer.py
```

### Day 3

```bash
python week1/day3/structured_summarizer.py
```

---

## 📁 Project Structure

```
week1/
│── day1/
│── day2/
│── day3/
│── day5/
```

---

## 💡 Key Insight

> Calling an LLM is easy.
> Building reliable systems around LLMs is the real challenge.

---

## 👩‍💻 Author

Sri Lekha
