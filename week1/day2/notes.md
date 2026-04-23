# 📌 Week 1 - Day 2 Notes (LLM Engineering Fundamentals)

---

## 🧠 1. What is Chat Completions API?

* Standard way to interact with LLMs
* Takes structured input as **messages**
* Returns structured output (JSON)

### 👉 Input format:

```json
messages = [
  {"role": "system", "content": "..."},
  {"role": "user", "content": "..."}
]
```

### 👉 Output format:

```json
response.choices[0].message.content
```

---

## 🧠 2. How LLM APIs Work

### Flow:

1. Send request (HTTP)
2. Include:

   * model name
   * messages
   * API key (if cloud)
3. Model processes input
4. Returns response (JSON)
5. Extract output

👉 SDKs are just wrappers over HTTP requests

---

## 🧠 3. System vs User Role

| Role   | Purpose                          |
| ------ | -------------------------------- |
| system | Controls behavior (tone, format) |
| user   | Actual input                     |

### Example:

* system → “Summarize clearly in bullet points”
* user → webpage content

👉 System prompt strongly affects output quality

---

## 🧠 4. Model Types

### 🔹 Cloud Models

* Gemini, GPT, Claude
* High performance
* Require API key & cost

### 🔹 Local Models

* Llama (via Ollama)
* Run on local machine
* Free but less powerful

---

## 🧠 5. Model Switching (Important Concept)

Same code works for different models by changing:

* `base_url`
* `model`

### Example:

| Provider | base_url               |
| -------- | ---------------------- |
| Gemini   | Google endpoint        |
| Ollama   | http://localhost:11434 |

👉 This is called **model abstraction**

---

## 🧠 6. Token Limit Problem

* LLMs cannot process unlimited text
* Input must be limited

### Solution:

```python
text = text[:5000]
```

### Why:

* Avoid crashes
* Reduce latency
* Stay within model limits

---

## 🧠 7. Web Scraping for LLM

### Steps:

1. Fetch webpage → `requests`
2. Parse HTML → `BeautifulSoup`
3. Remove noise:

   * script
   * style
   * noscript
4. Extract clean text

---

## 🧠 8. Why Cleaning is Important

* HTML contains noise (JS, CSS)
* LLM needs only readable text
* Cleaner input → better output

---

## 🧠 9. Prompt Engineering

Output depends heavily on prompt

### Weak:

* “summarize this”

### Strong:

* “Summarize in structured bullet points with headings”

---

## 🧠 10. Model Limitations

### ❌ Hallucination

* Model may generate incorrect facts

### ❌ Partial context

* Truncated input → incomplete summary

### ❌ Smaller models

* Less accurate than larger ones

---

## 🧠 11. Errors Faced (Real-world Learning)

| Error | Reason              |
| ----- | ------------------- |
| 503   | Server overload     |
| 404   | Model not available |
| 429   | Quota exceeded      |

### Solution:

👉 Use local model (Ollama)

---

## 🧠 12. Key Takeaways

* LLM = next-token prediction (not real understanding)
* Prompt controls output quality
* API = structured communication
* Local models are useful for development
* Handling input size is critical

---

## 🚀 What I Built

### Webpage Summarizer Pipeline:

```text
URL → Fetch → Clean → Limit → LLM → Summary
```

---

## 💡 Insight

> Building LLM apps is not just calling APIs — it involves preprocessing, prompt design, model selection, and handling real-world constraints.
