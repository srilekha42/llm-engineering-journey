# Week 2 Day 5: Multi-Modal Database Agent & Vocal Terminal

## 🔗 Project Architecture Showcase
The comprehensive production-ready codebase, assets, and documentation for this milestone are maintained in a dedicated engineering portfolio repository:
👉 **[Flighty Airlines Premium Concierge Terminal](https://github.com/srilekha42/flighty-airline-agent)**

---

## 🛠️ Core Engineering Implementations

### 1. Relational Tool Orchestration Layer
* Implemented deterministic tool calling bindings connecting the model layer straight to an isolated relational SQLite instance (`prices.db`).
* Built functional parsing wrappers that process natural language prompts down into exact parameterized database lookups, lowering text token prompt usage while eliminating model hallucination vectors entirely.

### 2. Native Multi-Modal Text-to-Speech Streaming
* Integrated `gemini-3.1-flash-tts-preview` utilising the `Fenrir` voice profile configuration to stream spoken agent updates natively alongside text blocks.
* Isolated file-writing race conditions by mapping unique local timestamp strings onto temporary audio files to bypass browser asset-locking bugs during real-time multi-turn feedback cycles.

### 3. Production State Defensiveness & Error Catch-Nets
* Formulated backend `try/except` safety buffers to maintain 100% user interface uptime during cloud API rate limiting transitions (`429 Resource Exhausted`) or network disruptions.
* Standardized state parsing code paths within the interface block to smoothly translate complex internal list/dictionary structures passed back and forth by Gradio chat components.

---

## 🧠 Mastered Engineering Concepts
* **Tool Separation Patterns:** Keeping core application data layers decoupled from basic prompt contexts to avoid large text token costs and preserve system security boundaries.
* **Multi-Modal State Handling:** Synchronizing ongoing chat history chains with live visual dashboard parameters and sequential audio streams dynamically.