# 🧠 Week 2 - Day 1 Notes (LLM Engineering)

## 📌 What I Did

* Set up local LLM using Ollama (`phi3`)
* Built `experiments.py` to test model behavior
* Ran multiple experiments:

  * explanation
  * reasoning
  * prompt control
  * verbosity

---

## 🔑 Core Concepts

### 1. Same API → Different Models

* Code stays the same
* Only model changes

👉 Important for building flexible systems

---

### 2. Prompt Controls Output

Same model → different behavior

* Weak prompt → guessing / loose answers
* Strong prompt → structured reasoning

Example:

* “Answer only” → may fail
* “Solve step-by-step” → correct reasoning

👉 Prompt quality directly affects accuracy

---

### 3. Reasoning vs Pattern Matching

* Models can memorize common problems
* Fail when question is slightly changed

👉 Correct answer ≠ real reasoning

---

### 4. Cost Awareness (Token Thinking)

* More tokens = more cost
* GPT → verbose (wasteful)
* Claude → balanced
* Perplexity → concise

👉 Optimize: **information per token**

---

### 5. Model Behavior Differences

| Model        | Behavior                                    |
| ------------ | ------------------------------------------- |
| GPT          | expressive, sometimes ignores strict format |
| Claude       | structured, follows instructions well       |
| Perplexity   | concise, adds citations                     |
| phi3 (local) | works but unstable                          |

---

## 🧪 Experiments & Observations

### 🔹 Basic Explanation

* Correct output
* Slightly verbose
* Not beginner-optimized

---

### 🔹 Reasoning Test

* Solved correctly (0.60)
* Even without guidance → showed reasoning

👉 Small models can reason, but inconsistently

---

### 🔹 Step-by-step Prompt

* Improved clarity
* But output had formatting issues

---

### 🔹 Format Control

* Followed instructions partially
* Bullet points correct but formatting inconsistent

---

### 🔹 Verbosity Test

* Explained correctly
* But added unnecessary detail
* Grammar issues observed

---

## ⚠️ Limitations of Small Models (phi3)

* Grammar errors
* Formatting inconsistencies
* Noisy outputs
* Less stable than GPT/Claude

👉 Even correct answers may not be reliable

---

## 💡 Key Takeaways

### 1. LLM Performance Formula

LLM performance = model capability × prompt quality

---

### 2. Model Selection Thinking

Do NOT ask:
❌ Which model is best?

Instead ask:
✅ Which model fits constraints?

* cost
* speed
* accuracy

---

### 3. Local Models vs API Models

| Type             | Pros          | Cons             |
| ---------------- | ------------- | ---------------- |
| Local (phi3)     | free, private | unstable, weaker |
| API (GPT/Claude) | powerful      | cost             |

---

## 🧠 Final Insight

Even if a small model gives the correct answer:

* it may not be reliable
* it may fail on slightly different inputs
* it may produce unstable output

👉 Reliability matters more than correctness

---

## 🚀 What I Improved

* Understanding of prompt engineering
* Ability to evaluate model outputs critically
* Awareness of cost vs performance tradeoffs
* Hands-on experience with local LLMs

---
