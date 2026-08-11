```
# 🚀 LLM Engineering Journey

This repository documents my hands-on learning and practical implementation of Large Language Models (LLMs), focusing on building reliable, real-world systems.

---

## 📌 Week 1 - Foundations

### ✅ Day 1: Basic LLM Interaction
- Connected Python with LLM APIs
- Built a prompt → response pipeline
- Learned basic prompt engineering

---

### ✅ Day 2: Basic LLM Applications
- Used Chat Completions API
- Built a webpage summarizer
- Extracted and cleaned HTML using BeautifulSoup
- Understood token limits and model constraints
- Compared cloud vs local models (Ollama)

---

### ✅ Day 3: LLM Output Control & Reliability
- Learned that LLM outputs are **not reliable by default**
- Implemented structured JSON output
- Added JSON parsing, output validation, retry mechanisms, and schema handling
- Built a multi-step pipeline for reliability

---

### ✅ Day 5: Pipeline-Based Project (AI Brochure Generator)
🔗 Project: https://github.com/srilekha42/ai-brochure-generator

- Scraped website content with retry handling
- Extracted and filtered internal links
- Identified key pages (About, Docs, Careers)
- Generated structured brochure output

---

## 📌 Week 2 - Advanced Interfaces & Conversation Systems

### ✅ Day 2: Dynamic Model Routing & Streaming UIs
- Built multi-model UI with Gradio Blocks
- Added real-time token streaming using Python generators (`yield`)
- Connected to Google GenAI SDK
- Learned streaming shows answers as they generate (not all at once)

---

### ✅ Day 3: Conversation History & System Personas
- Fixed stateless API limitation with conversation memory
- Added system instructions for brand voice control
- Built foundation for RAG pipelines

---

### ✅ Day 4: Function Calling & Relational Database Tools
- Built AI Agent that calls external tools
- Connected Gemini to SQLite database
- Enabled multi-tool data aggregation

---

## 📌 Week 3 - Open-Source Foundations

### ✅ Day 1: Hugging Face & Google Colab
- Moved from paid APIs to free open-source models
- Used **Hugging Face** for models (2M+ free)
- Used **Google Colab** for cloud GPUs (free T4 with 15GB VRAM)
- Learned GPU = parallel math, VRAM = model must fit entirely
- Built Text-to-Speech and Image Generator
- **Key Takeaway:** Can run free models on rented GPUs—no longer API-dependent

---

### ✅ Day 2: Hugging Face Pipelines
- Learned two API levels: **Pipelines** (easy) and **Tokenizers/Models** (advanced)
- Used pipelines for common AI tasks
- Built Sentiment Analysis, NER, Question Answering, Summarization, Translation, Zero-Shot Classification, Text Generation, Image Generation, and Text-to-Speech
- **Key Takeaway:** Small specialized models are faster, cheaper, and good enough for many tasks

---

### ✅ Day 3: Tokenizers, Special Tokens & Chat Templates
- Learned that LLMs understand **numbers (Token IDs), not text**
- Explored how **tokenizers** convert text into tokens and token IDs
- Learned that **every model has its own tokenizer and vocabulary**
- Understood **special tokens** used to mark the start and end of messages
- Learned how **`apply_chat_template()`** formats chat conversations before tokenization
- **Key Takeaway:** Every message must be converted into the exact token format expected by the model before inference.

---

### ✅ Day 4: Deep Model Architectures, Quantization & Streaming Inference
- Explored internal structure of Transformer models
- Learned three main parts: **Embedding Layer** (converts words to numbers), **Decoder Layers** (processes with Self-Attention + MLP), and **LM Head** (predicts next word)
- Understood **Quantization** – converts 16-bit numbers to 4-bit, reducing GPU memory by 4x with almost no quality loss
- Learned **Streaming Inference** – `model.generate()` predicts tokens step-by-step, while `TextStreamer` shows output in real-time as each word is generated
- **Key Takeaway:** Quantization makes large models run on limited hardware; streaming creates better user experience

---

## 🛠️ Projects Built

### 🔹 Chat API
- System + user message structure
- OpenAI-compatible API format

### 🔹 Local LLM (Ollama)
- Ran LLM locally without API cost

### 🔹 Webpage Summarizer
- Extract, clean, summarize webpage content

### 🔹 Structured Summarizer
- Convert webpage → structured JSON with validation

### 🔹 AI Brochure Generator
- URL → Scraper → Link Filter → Content Selector → Generator

### 🔹 Live Gemini Router UI
- Side-by-side Gradio UI with real-time streaming

### 🔹 AI Store Assistant with Memory
- Chatbot with conversation tracking

### 🔹 Open-Source Image & Audio Generator
- Hugging Face pipelines on Google Colab

---

## 🧠 Key Concepts

- LLMs are **probabilistic systems**
- Reliability requires pipelines, not single calls
- LLM APIs are **stateless**; memory must be managed explicitly
- **LLMs understand Token IDs (numbers), not plain text**
- **Every model has its own tokenizer and vocabulary**
- **Chat templates format conversations before tokenization**
- **GPUs** handle parallel matrix math
- **VRAM** is the workbench—models must fit completely
- **Hugging Face** = App Store for free AI models
- **Google Colab** = Rent powerful computers in the cloud
- **Training** = teaching the AI (done once, expensive)
- **Inference** = using the AI (what we do daily, cheap)
- **Quantization** = shrink models to fit in less memory
- **Streaming** = show output word-by-word for better user experience

---

## ⚙️ Tech Stack

- Python
- OpenAI-compatible APIs
- Google GenAI SDK
- Gradio (UI Framework)
- Ollama (Local LLM)
- BeautifulSoup
- Python-dotenv
- Hugging Face Hub
- Transformers
- Diffusers
- Google Colab

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

**Week 1 - Day 2 (Basic Summarizer)**

```bash
python week1/day2/basic_summarizer.py
```

**Week 1 - Day 3 (Structured Summarizer)**

```bash
python week1/day3/structured_summarizer.py
```

**Week 2 - Day 2 (Live Gemini Router UI)**

```bash
cd week2/day2
python day2_ui.py
```

**Week 2 - Day 3 (AI Store Assistant with Memory)**

```bash
cd week2/day3
python day3_chat.py
```

**Week 2 - Day 4 (Airline AI Agent with SQL Tools)**

```bash
cd week2/day4
python day4_tools.py
```

**Week 3 - Day 1 (Hugging Face + Colab)**

```bash
# Open the Colab link from course materials
cd week3/day1
python image_generator.py
python text_to_speech.py
```

**Week 3 - Day 2 (Hugging Face Pipelines)**

```bash
# Open the Colab link from course materials
cd week3/day2
python pipelines_demo.py
```

**Week 3 - Day 3 (Tokenizers & Chat Templates)**

```bash
cd week3/day3
python tokenizer_demo.py
```

**Week 3 - Day 4 (Quantization & Streaming)**

```bash
cd week3/day4
python quantization_demo.py
python streaming_demo.py
```

---

## 💡 Key Insight

> Calling an LLM is easy.
>
> Building reliable systems around LLMs is the real challenge.
>
> Understanding how text becomes tokens and running open-source models yourself is the next superpower.

---

## 👩‍💻 Author

**Sri Lekha**
---