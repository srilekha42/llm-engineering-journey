# Day 1 Notes: Model Selection & Reasoning

## 🧠 What I Learned

### 1. There is No "Best" AI Model

There is no single best model for everything.

We should choose a model based on our project.

We should check:

- Cost 💰
- Speed ⚡
- Context window 📖
- License 📜
- Model capability 🧠
- Accuracy 🎯

For example, a model that is very good at coding may not be the best model for summarizing audio.

---

### 2. Chinchilla Scaling Law

A bigger model is not always better.

When we increase the number of parameters, we also need enough training data.

Simple idea:

**Bigger model + enough training data = Better training**

---

### 3. Important Benchmarks

Benchmarks are like exams for AI models.

Different benchmarks test different skills:

- **GPQA** → Difficult science questions
- **MMLU-Pro** → General knowledge and reasoning
- **AIME** → Mathematics
- **LiveCodeBench** → Coding
- **MuSR** → Logical reasoning
- **HLE** → Very difficult questions

---

### 4. Benchmark Problems

We cannot choose a model only by looking at benchmark scores.

Why?

- Some test questions may already be present in the model's training data.
- One benchmark tests only certain skills.
- A model can be good at one task and bad at another.
- Some old benchmarks have become too easy for modern models.

So we should also test the model on **our own data**.

---

# 🧪 Practical Experiment

## Direct Prompt vs Forced Reasoning

**Model:** Groq `llama-3.3-70b-versatile`

I tested the same logic puzzle in two ways.

### Test 1: Direct Prompt

I asked the model to give only the answer.

Result:

```text
{"front": "David", "third": "Bob"}