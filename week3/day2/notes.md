---

## 📝 Week 3, Day 2: Hugging Face Pipelines

---

### Two Ways to Use Hugging Face Code

**1. High-Level (Pipelines) - Easy Way**
- Pre-built functions for common tasks
- Just create once, call many times
- Great for quick experiments

**2. Low-Level (Tokenizers & Models) - Hard Way**
- Direct access to the AI's brain
- More control but more complex
- We'll do this tomorrow

---

### Training vs Inference

**Training:** Teaching the AI (costs millions, done once)
**Inference:** Using the AI (what we do every day, cheap)

Pipelines = only for inference

---

### Big Idea: Small Models = Cheap & Fast

- Big models (GPT-4) = expensive, do everything
- Small specialized models = cheap, do one thing well
- Use small models for specific tasks (translation, classification)
- Saves money and runs faster

---

### Hardware Settings

- **cuda** = for Nvidia GPUs (PC)
- **mps** = for Apple Silicon (Mac)

---

### What I Built Today

| Task | What It Does |
|------|--------------|
| Sentiment Analysis | Is this text happy or sad? |
| Named Entity Recognition (NER) | Find people, places, companies in text |
| Question Answering | Answer questions with given context |
| Zero-Shot Classification | Put text into custom categories with no examples |
| Summarization | Make long text short |
| Translation | Convert English to French/Spanish |
| Text Generation | Predict next words (GPT-2 = random nonsense) |
| Text-to-Speech | Convert text to audio |
| Image Generation | Create images from text prompts |

---

### Key Insight

> Pipelines make trying different models super easy. Experiment freely because open-source models are FREE.

---

### Pro Tip

If you see "CUDA required" error → Google bumped you to a CPU box.
Fix: Runtime → Disconnect & delete runtime → Edit → Clear all outputs → Run from top.

---