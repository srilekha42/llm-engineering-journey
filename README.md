# 🚀 LLM Engineering Journey

This repository documents my hands-on learning and practical implementation of Large Language Models (LLMs).

---

## 📌 Week 1 - Foundations

### ✅ Day 1: Basic LLM Interaction

* Connected Python with Gemini API
* Built a simple prompt → response pipeline
* Learned basic prompt engineering

---

### ✅ Day 2: Basic LLM Applications

* Used Chat Completions API
* Built a webpage summarizer
* Extracted and cleaned webpage data using BeautifulSoup
* Understood token limits and model constraints
* Switched between cloud and local models (Ollama)

---

### ✅ Day 3: LLM Output Control & Reliability

* Learned that LLM outputs are **not reliable by default**
* Implemented **structured JSON output**
* Added:

  * JSON parsing (`json.loads`)
  * Output validation
  * Retry mechanism
  * Schema handling
* Built a multi-step pipeline to handle real-world LLM issues

---

## 🛠️ Projects Built

### 🔹 1. Chat API

* Implemented system + user message structure
* Used OpenAI-compatible API format

---

### 🔹 2. Local LLM (Ollama)

* Ran LLM locally without API cost
* Compared local vs cloud models

---

### 🔹 3. Basic Webpage Summarizer (Day 2)

* Extract webpage content
* Clean HTML
* Generate summary using LLM

---

### 🔹 4. Structured Summarizer (Day 3)

* Convert webpage → structured JSON
* Handle:

  * invalid JSON
  * extra text
  * schema mismatches
  * incomplete outputs

---

## 🧠 Key Concepts

* LLMs work using **next-token prediction**
* Prompt design affects output quality
* LLM outputs are **probabilistic**
* Parsing converts text → usable data
* Validation ensures correctness
* Reliability requires multi-step pipelines

---

## ⚙️ Tech Stack

* Python
* OpenAI-compatible API
* Ollama (Local LLM)
* BeautifulSoup
* Requests

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
```

### Day 2 (Basic Summarizer)

```bash
python week1/day2/basic_summarizer.py
```

### Day 3 (Structured Summarizer)

```bash
python week1/day3/structured_summarizer.py
```

---

## 📁 Project Structure

```
week1/
│── day1/
│── day2/
│   ├── basic_summarizer.py
│
│── day3/
│   ├── structured_summarizer.py
```

---

## 💡 Key Insight

> Calling an LLM is easy.
> Building reliable systems with LLMs is the real challenge.

---

## 👩‍💻 Author

Sri Lekha
