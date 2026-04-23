# 🚀 LLM Engineering Journey

This repository documents my hands-on learning and practical implementation of Large Language Models (LLMs).

---

## 📌 Week 1 - Foundations

### ✅ Day 1: Basic LLM Interaction

* Connected Python with Gemini API
* Built a simple prompt → response pipeline
* Explored prompt engineering basics

---

### ✅ Day 2: LLM Engineering Fundamentals

#### 🔹 What I Learned

* Chat Completions API (standard way to interact with LLMs)
* Difference between SDK vs API-based interaction
* Switching between cloud models and local models
* Understanding token limits and model constraints
* Handling real-world API errors (429, 503, 404)

---

## 🛠️ Projects Built

### 🔹 1. Chat API (Structured LLM Interaction)

* Used OpenAI-compatible API format
* Implemented system + user role-based messaging
* Parsed structured responses (`choices → message → content`)

---

### 🔹 2. Local LLM with Ollama

* Ran LLM locally using Ollama (no API cost)
* Switched from cloud model → local model with minimal code changes
* Understood trade-offs between performance and cost

---

### 🔹 3. Webpage Summarizer (Core Project)

#### 📥 Input:

* Any webpage URL

#### ⚙️ Pipeline:

1. Fetch webpage using `requests`
2. Clean HTML using `BeautifulSoup`
3. Remove noise (`script`, `style`, `noscript`)
4. Extract readable text
5. Handle token limits (truncate large input)
6. Send structured prompt to LLM
7. Generate summarized output

#### 📤 Output:

* Structured bullet-point summary with headings

---

## 🧠 Key Concepts Understood

* LLMs work on **next-token prediction**
* Prompt design directly affects output quality
* Token limits restrict input size
* Local models vs cloud models trade-offs:

  * Local → free, private, less powerful
  * Cloud → powerful, paid, scalable
* Small models may produce **hallucinations**

---

## ⚠️ Challenges Faced

* ❌ API quota errors (429)
* ❌ Model availability issues (404)
* ❌ Server overload (503)
* ✅ Solution: Switched to local LLM (Ollama)

---

## ⚙️ Tech Stack

* Python
* OpenAI-compatible API
* Ollama (Local LLM)
* BeautifulSoup
* Requests
* dotenv

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run summarizer

```bash
python week1/day2/summarizer.py
```

### 3. Enter URL when prompted

---

## 📁 Project Structure

```
week1/
│── day1/
│── day2/
│   ├── check_models.py
│   ├── chat_api.py
│   ├── ollama_chat.py
│   ├── summarizer.py
```

---

## 🚀 Next Steps

* Model comparison and evaluation
* Multi-model workflows
* Handling long documents (chunking, RAG)
* Building production-ready LLM applications

---

## 💡 Key Insight

> Building with LLMs is not just about calling APIs — it involves data preprocessing, prompt design, model selection, and handling real-world constraints.

---

## 👩‍💻 Author

Sri Lekha

