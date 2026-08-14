# Day 2 Notes: AI Leaderboards & Blind A/B Testing

## 🎯 What I Learned

Today I learned how to **compare different AI models** before choosing one for a project.

An **AI leaderboard** is like a ranking table for AI models. It helps us compare models based on things like:
- Intelligence
- Speed
- Cost
- Context window
- Human preference

The important lesson is:

> **The best AI model is not always the biggest or most expensive model. It depends on the task.**

---

## 🏆 Key AI Leaderboards

### 1. Artificial Analysis
Helps compare AI models based on **intelligence, speed, latency, and cost**.

### 2. Vellum
Useful for checking **context window, pricing, and model performance**.

### 3. Scale AI SEAL & HLE
Provides difficult and specialized tests to evaluate AI model capabilities.

### 4. LiveBench
Uses regularly updated questions to provide a fresh evaluation of AI models.

### 5. LM Arena (Chatbot Arena)
Allows real users to compare two AI model responses **without knowing which model produced each response**. Users vote for the better answer.

---

## 🧪 Practical Project: Local Model Arena

I built a simple **Blind A/B Testing program** using the **Groq API**.

### What is Blind A/B Testing?

Two AI models receive the **same question**.

```text
              Same Prompt
                   ↓
          ┌────────┴────────┐
          ↓                 ↓
       Model A           Model B
          ↓                 ↓
      Answer A           Answer B
          ↓                 ↓
          Compare Both Answers
                   ↓
              Vote A / B
                   ↓
          Reveal Model Names