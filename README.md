# 🚀 LLM Engineering Journey

This repository documents my hands-on learning journey in LLM Engineering, covering everything from basic LLM API interactions to open-source models, structured outputs, function calling, conversation memory, Hugging Face, quantization, streaming inference, model selection strategies, and LLM benchmarking.

The goal is to move beyond simply using LLMs and understand how to build reliable, practical, and real-world LLM applications.

---

## 📌 Week 1 — Foundations

### ✅ Day 1: Basic LLM Interaction

- Connected Python with LLM APIs
- Built a basic prompt → response pipeline
- Learned the fundamentals of prompt engineering

### ✅ Day 2: Basic LLM Applications

- Used Chat Completions API
- Built a webpage summarizer
- Extracted and cleaned HTML using BeautifulSoup
- Understood token limits and model constraints
- Compared cloud-based models with local models using Ollama

### ✅ Day 3: LLM Output Control & Reliability

Learned that LLM outputs are probabilistic and not reliable by default.

Implemented:

- Structured JSON output
- JSON parsing
- Output validation
- Retry mechanisms
- Schema handling
- Multi-step LLM pipelines

### ✅ Day 5: Pipeline-Based Project — AI Brochure Generator

🔗 Project: https://github.com/srilekha42/ai-brochure-generator

- Scraped website content with retry handling
- Extracted and filtered internal links
- Identified important pages such as About, Documentation, and Careers
- Generated structured brochure output

---

# 📌 Week 2 — Advanced Interfaces & Conversation Systems

### ✅ Day 2: Dynamic Model Routing & Streaming UIs

- Built a multi-model UI using Gradio Blocks
- Added real-time token streaming using Python generators (`yield`)
- Connected applications with the Google GenAI SDK
- Learned how streaming displays responses as they are generated instead of waiting for the complete response

### ✅ Day 3: Conversation History & System Personas

- Understood the stateless nature of LLM APIs
- Implemented conversation memory
- Added system instructions for controlling brand/persona behavior
- Built the foundation for future RAG pipelines

### ✅ Day 4: Function Calling & Relational Database Tools

- Built an AI Agent capable of calling external tools
- Connected Gemini with a SQLite database
- Implemented multi-tool data aggregation
- Learned how LLMs can interact with external systems through function calling

---

# 📌 Week 3 — Open-Source LLM Foundations & Standalone Builds

### ✅ Day 1: Hugging Face & Google Colab

Moved from paid APIs toward free and open-source AI models.

Learned:

- Hugging Face model ecosystem
- Google Colab for cloud GPU computing
- NVIDIA T4 GPU with approximately 15 GB VRAM
- GPU = parallel mathematical computation
- VRAM = memory required to load and run models

Built:

- Text-to-Speech application
- Image generation application

**Key Takeaway:**

> Open-source models can be run on rented cloud GPUs, reducing dependency on paid LLM APIs.

---

### ✅ Day 2: Hugging Face Pipelines

Learned the two major API levels in Hugging Face Transformers:

- **Pipelines** → high-level and easy to use
- **Tokenizers + Models** → lower-level and more customizable

Built implementations for:

- Sentiment Analysis
- Named Entity Recognition (NER)
- Question Answering
- Summarization
- Translation
- Zero-Shot Classification
- Text Generation
- Image Generation
- Text-to-Speech

**Key Takeaway:**

> Small, specialized models can often be faster, cheaper, and sufficient for many real-world AI tasks.

---

### ✅ Day 3: Tokenizers, Special Tokens & Chat Templates

Learned how LLMs process text internally.

Explored:

- Tokenization
- Token IDs
- Model vocabularies
- Special tokens
- Chat templates
- `apply_chat_template()`
- Converting conversations into model-specific formats

**Key Takeaway:**

> LLMs don't directly understand raw text. Text is converted into token IDs and formatted according to the model's expected input structure.

---

### ✅ Day 4: Transformer Architecture, Quantization & Streaming Inference

Explored the internal architecture of Transformer-based language models.

Studied three major components:

1. **Embedding Layer** — converts token IDs into numerical representations
2. **Decoder Layers** — process information using Self-Attention and MLP layers
3. **LM Head** — predicts probabilities for the next token

### Quantization

Learned how quantization:

- Converts higher-precision weights into lower-precision representations
- Can convert FP16 models to 4-bit representations
- Significantly reduces memory requirements
- Makes larger models easier to run on limited hardware

### Streaming Inference

- `model.generate()` produces tokens progressively
- `TextStreamer` displays generated tokens in real time
- Improves the user experience by avoiding long waits for complete responses

**Key Takeaway:**

> Quantization helps large models fit into limited GPU memory, while streaming makes LLM applications feel faster and more interactive.

---

### ✅ Day 5: End-to-End Multimodal Pipeline — Audio-to-Minutes Generator

🔗 Standalone Project Repository: `audio-to-minutes-generator`

Combined Whisper audio transcription, structured LLM extraction, and automated document generation.

Implemented:

- **Whisper Integration:** Transcribed audio files into structured text
- **Automated Summarization:** Extracted key topics, decisions, action items, and owners
- **Document Output:** Exported meeting minutes directly into clean Markdown/Docx formats

**Key Takeaway:**

> Combining specialized multimodal models (e.g., Whisper for speech) with LLMs creates powerful automated workflow pipelines.

---

# 📌 Week 4 — Model Selection & Evaluation Strategy

### ✅ Day 1: Model Selection Strategy, Chinchilla Scaling & Benchmarks

Explored how to systematically select the right model for a specific production task rather than defaulting to the largest model.

Covered:

- **Model Specifications:** Learned to choose the right model based on task, cost, speed, context window, and accuracy.
- **Chinchilla Scaling Laws:** Learned how model size and training data affect model performance.
- **Hard Benchmarks:** Explored GPQA, MMLU-Pro, AIME, LiveCodeBench, MuSR, and HLE.
- **Benchmark Limitations:** Learned about contamination, saturation, and narrow benchmark testing.
- **Forced Reasoning (Chain of Thought):** Compared direct prompting with step-by-step reasoning using a Groq model.

**Key Takeaway:**

> There is no single "best" model—only the right model for a given task, speed, cost, and accuracy requirement.

---

# 🛠️ Projects Built

### 🔹 Chat API

- System + user message structure
- OpenAI-compatible API format
- Basic LLM interaction

### 🔹 Local LLM with Ollama

- Ran an LLM locally
- Reduced dependency on cloud APIs
- Explored local inference

### 🔹 Webpage Summarizer

**URL → HTML → Clean Content → Summary**

- Extracted webpage content
- Cleaned HTML
- Generated summaries using an LLM

### 🔹 Structured Summarizer

**Webpage → LLM → Structured JSON → Validation**

- Generated structured outputs
- Added JSON parsing
- Added validation and retry handling

### 🔹 AI Brochure Generator

**URL → Scraper → Link Filter → Content Selector → Generator**

- Scraped company websites
- Identified relevant pages
- Generated structured company brochures

### 🔹 Live Gemini Router UI

- Built with Gradio
- Multi-model comparison
- Real-time streaming
- Google GenAI SDK integration

### 🔹 AI Store Assistant with Memory

- Conversation tracking
- Persistent chat context
- System persona
- AI-assisted store interactions

### 🔹 Open-Source Image & Audio Generator

- Hugging Face pipelines
- Google Colab GPU
- Image generation
- Text-to-Speech

### 🔹 Audio-to-Minutes Generator 

**Audio → Whisper Transcription → LLM Extraction → Meeting Minutes**

- Transcribed raw audio to text
- Processed transcripts via LLM to extract key decisions and action items
- Formatted structured outputs into meeting minutes documents

### 🔹 Forced Reasoning Benchmark Evaluator  

**Logic Puzzle → Direct Prompting vs. Forced Reasoning (Groq API)**

- Evaluated standard output against step-by-step Chain-of-Thought prompting
- Demonstrated how scratchpad token allocation prevents logical hallucinations

---

# 🧠 Key Concepts Learned

### LLM Fundamentals & Model Selection

- LLMs are probabilistic systems requiring validation pipelines
- Model selection is guided by context windows, latency, costs, parameters, and benchmark fits
- Forced reasoning (intermediate token generation) drastically improves task performance

### APIs & Applications

- LLM APIs are generally stateless; conversation memory must be managed explicitly
- Function calling allows models to interact with external tools and databases
- Structured JSON outputs improve production reliability

### Tokenization & Transformers

- LLMs operate on token IDs rather than raw text
- Every model relies on specific tokenizers, vocabularies, and chat templates
- Transformers use Embedding Layers, Decoder Attention Layers, and LM Heads to predict next tokens

### Hardware, Inference & Scaling

- GPUs accelerate parallel matrix operations; VRAM limits downloadable model sizes
- Quantization reduces memory requirements, fitting models into smaller hardware limits
- Chinchilla Scaling defines the ratio between parameters and training tokens
- Streaming inference enhances UI/UX responsiveness

### Benchmarking & Open Source

- Standard benchmarks (GPQA, AIME, MuSR, LiveCodeBench) gauge multi-domain capabilities
- Beware of training data contamination and benchmark saturation when evaluating candidate models
- Hugging Face, Groq, and Google AI Studio provide powerful open-source & fast inference options

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **OpenAI / Groq API** | LLM API integration & ultra-fast open inference |
| **Google GenAI SDK** | Gemini integration |
| **Gradio** | Interactive AI interfaces |
| **Ollama** | Local LLM inference |
| **BeautifulSoup** | Web scraping & HTML parsing |
| **python-dotenv** | Environment variable management |
| **Hugging Face Hub** | Open-source model ecosystem |
| **Transformers & Diffusers** | LLMs, NLP pipelines, & image generation |
| **Whisper** | Audio transcription pipeline |
| **Google Colab** | Cloud GPU environment |
| **SQLite** | Database integration |

---

# 📂 Repository Structure

```text
llm-engineering-journey/
│
├── week1/
│   ├── chat-api/
│   ├── webpage-summarizer/
│   ├── structured-summarizer/
│   └── ai-brochure-generator/
│
├── week2/
│   ├── gemini-router/
│   ├── conversation-memory/
│   └── function-calling/
│
├── week3/
│   ├── day1/  <-- Hugging Face & Colab Setup
│   ├── day2/  <-- Transformers Pipelines
│   ├── day3/  <-- Tokenizers & Chat Templates
│   ├── day4/  <-- Transformer Architecture & Quantization
│   └── day5/  <-- README link to audio-to-minutes-generator & week3 notes
│
├── week4/
│   └── day1/  <-- Model Selection Matrix & Forced Reasoning Evaluator
│
├── requirements.txt
└── README.md

--- 
# ▶️ How to Run

### 1. Clone the repository

git clone <your-repository-url>

cd LLM-Engineering

### 2. Install dependencies

pip install -r requirements.txt

### 3. Configure environment variables

Create a `.env` file and add the required API keys:

OPENAI_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
GROQ_API_KEY=your_groq_api_key

> Only add the keys required by the specific project you want to run.

### 4. Run a project

Navigate to the required project directory and run its Python/Gradio application.

python app.py

---

# 🎯 Learning Goal

This repository is a continuous record of my progress toward becoming an LLM / AI Engineer.

The focus is not just on calling an LLM API, but on understanding the complete process:

LLM APIs
   ↓
Prompt Engineering
   ↓
Structured Outputs
   ↓
Reliable Pipelines
   ↓
Conversation Memory
   ↓
Function Calling
   ↓
Open-Source Models
   ↓
Tokenization
   ↓
Transformers
   ↓
Quantization
   ↓
Streaming Inference
   ↓
Real-World LLM Applications

---

## 🚀 Learning Philosophy

**Learn → Build → Break → Debug → Improve → Repeat**