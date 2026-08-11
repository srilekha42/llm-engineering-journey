# 📌 Week 3, Day 5 — Standalone Project: Multi-Modal Audio Minutes Generator

## 🔗 Standalone Repository

**GitHub Repository:** [audio-to-minutes-generator](https://github.com/srilekha42/audio-to-minutes-generator)

---

## 🎯 Project Overview

Built an end-to-end **multi-modal AI application** that converts meeting audio recordings into structured and professional executive meeting minutes.

The application combines **audio preprocessing, Automatic Speech Recognition (ASR), transcript chunking, LLM summarization, and structured information extraction** using open-source Hugging Face models.

### Pipeline

```text
Meeting Audio
      ↓
Librosa Audio Preprocessing
      ↓
16kHz Mono WAV
      ↓
Whisper-Small
      ↓
Raw Transcript
      ↓
Transcript Chunking
      ↓
Qwen2.5-0.5B-Instruct
      ↓
Final Consolidation
      ↓
Executive Meeting Minutes