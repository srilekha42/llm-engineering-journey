# 🚀 LLM Engineering Journey

This repository documents my **hands-on journey of learning LLM Engineering**.

The goal of this journey is not just to use AI tools like ChatGPT, but to understand:

- How LLMs work
- How applications communicate with LLMs
- How to write better prompts
- How to control and validate LLM output
- How to give LLMs memory and tools
- How to use open-source models
- How tokens and Transformers work
- How to run models locally
- How to select the right model
- How to evaluate and compare AI models
- How to build practical LLM applications

The learning approach is:

> **Learn → Build → Test → Debug → Improve**

---

# 📚 Learning Roadmap

```text
LLM Basics
    ↓
LLM APIs
    ↓
Prompt Engineering
    ↓
Structured Outputs
    ↓
Reliable LLM Applications
    ↓
Conversation Memory
    ↓
Function Calling & Tools
    ↓
Agents
    ↓
Open-Source Models
    ↓
Tokenization
    ↓
Transformers
    ↓
Quantization
    ↓
Streaming
    ↓
Model Selection
    ↓
Benchmarks
    ↓
AI Leaderboards
    ↓
Blind A/B Testing
    ↓
Real-World LLM Applications
````

---

# 📌 Week 1 — LLM Foundations

Week 1 focused on understanding the basic concepts behind LLM applications and learning how to communicate with AI models through APIs.

---

## ✅ Day 1 — Basic LLM Interaction

Learned how to connect a Python application with an LLM API.

### What is an LLM API?

An API allows a Python application to send a request to an AI model and receive a response.

### Basic Flow

```text
Python Application
       ↓
     Prompt
       ↓
    LLM API
       ↓
   AI Response
```

### Learned

* Basic LLM interaction
* Sending prompts
* Receiving responses
* Basic prompt engineering
* Working with LLM APIs

### Key Takeaway

> An LLM API allows our application to communicate with an AI model.

---

## ✅ Day 2 — Basic LLM Applications

Learned how to combine LLMs with normal Python tools to build useful applications.

### Built

* Webpage Summarizer
* Local LLM application using Ollama

### Learned

* Chat Completions API
* Webpage content extraction
* HTML parsing using BeautifulSoup
* Token limits
* Model limitations
* Cloud-based vs local AI models

### Webpage Summarizer Flow

```text
Webpage URL
     ↓
Download HTML
     ↓
Extract Text
     ↓
Clean Text
     ↓
Send to LLM
     ↓
Generate Summary
```

### Key Takeaway

> LLMs become more useful when they are combined with normal programming tools.

---

## ✅ Day 3 — LLM Output Control & Reliability

Learned that LLMs do not always produce exactly the output an application expects.

Therefore, applications need to **check and validate** model responses.

### Implemented

* Structured JSON output
* JSON parsing
* Output validation
* Retry mechanisms
* Schema handling
* Multi-step LLM pipelines

### Basic Flow

```text
LLM
 ↓
Generate Response
 ↓
Validate Response
 ↓
Is it valid?
 ├── Yes → Continue
 └── No  → Retry / Fix
```

### Why is this important?

An application should not blindly trust every LLM response.

### Key Takeaway

> Reliable LLM applications need validation and error handling.

---

## ✅ Day 4 — Tokens, Context Window, Cost & Agents

Learned some important concepts that explain how LLM applications work behind the scenes.

### 🔹 Tokens

A **token is a small piece of text**.

A token is not always a complete word.

For example, a sentence can be broken into several tokens before the model processes it.

```text
Human Text
    ↓
Tokenization
    ↓
Tokens
    ↓
LLM
```

The model works with **tokens rather than raw text**.

### Important

More tokens generally mean:

* More input/output processing
* More API cost
* More context usage

---

### 🔹 Illusion of Memory

LLMs do not automatically remember every previous message.

LLM APIs are generally **stateless**.

This means the application usually needs to send previous conversation history again when continuing a conversation.

```text
Previous Conversation
        +
New User Message
        ↓
      LLM
        ↓
    Response
```

So the model appears to remember, but the application is usually providing the previous conversation again.

---

### 🔹 Context Window

The **context window** is the maximum amount of information, measured in tokens, that a model can handle at one time.

It can include:

* User input
* Previous conversation
* Instructions
* Model output

```text
Context Window
┌──────────────────────────┐
│ System Instructions      │
│ Conversation History     │
│ New User Message         │
│ Generated Output         │
└──────────────────────────┘
```

If the conversation becomes very large, it can use more tokens and increase cost.

---

### 🔹 API Cost

LLM APIs generally charge based on tokens.

Cost can come from:

* Input tokens
* Output tokens

Therefore:

> **More tokens = higher usage and potentially higher cost.**

Long conversations can become more expensive because more conversation history may need to be sent.

---

### 🔹 Scaling

Learned that improvement can happen at different stages.

**Training-time scaling:**

> Using larger models and more training resources.

**Inference-time scaling:**

> Improving how we use the model through better prompts and reasoning strategies.

---

### 🔹 Agents

A simple way to understand an AI agent is:

```text
LLM + Loop + Tools
```

An agent can:

1. Understand a task
2. Decide what to do
3. Use a tool
4. Observe the result
5. Continue until the task is completed

### Key Takeaway

> Tokens affect how LLMs process text and cost. Context windows limit how much information can be handled at once, and agents allow LLMs to work with tools.

---

## ✅ Day 5 — AI Brochure Generator

🔗 Project: [https://github.com/srilekha42/ai-brochure-generator](https://github.com/srilekha42/ai-brochure-generator)

Built an application that collects information from a company website and generates a structured company brochure.

### Implemented

* Website scraping
* Content extraction
* Internal link discovery
* Useful page selection
* Content cleaning
* LLM-based brochure generation
* Structured output
* Retry handling

### Pipeline

```text
Company Website
       ↓
Web Scraper
       ↓
Find Internal Links
       ↓
Select Useful Pages
       ↓
Extract Content
       ↓
LLM
       ↓
Company Brochure
```

### Key Takeaway

> A useful AI application can be built by connecting multiple small steps into one pipeline.

---

# 📌 Week 2 — Advanced LLM Interfaces & Agents

Week 2 focused on local LLMs, prompt experiments, conversation memory, function calling, databases, and multimodal AI applications.

---

## ✅ Day 1 — Local LLM & Prompt Experiments

### What I Did

* Set up a local LLM using Ollama
* Used the `phi3` model
* Built `experiments.py`
* Tested different types of prompts
* Compared model behavior

### Experiments

* Basic explanation
* Reasoning
* Prompt control
* Step-by-step prompting
* Format control
* Verbosity

---

### 🔹 Same API → Different Models

The application code can remain mostly the same while changing the model.

```text
Same Application
      ↓
Different Model
      ↓
Different Output
```

This is useful when building flexible systems.

---

### 🔹 Prompt Controls Output

The same model can behave differently depending on the prompt.

For example:

```text
Weak Prompt
    ↓
Less controlled answer
```

while:

```text
Detailed Prompt
    ↓
More controlled answer
```

### Key Takeaway

> Prompt quality can directly affect the quality and structure of an LLM response.

---

### 🔹 Reasoning vs Pattern Matching

A model may know the answer to a familiar problem because it has seen similar patterns before.

But when the question is changed slightly, it may fail.

Therefore:

> **A correct answer does not always mean the model truly handled the problem reliably.**

---

### 🔹 Cost Awareness

More generated tokens generally mean more cost.

The goal is not simply to generate a long answer.

Instead, we want:

> **More useful information per token.**

---

### 🔹 Model Behavior

During the experiments, different models showed different behaviors.

| Model      | Observed Behavior                               |
| ---------- | ----------------------------------------------- |
| GPT        | Expressive, sometimes ignored strict formatting |
| Claude     | Structured and followed instructions well       |
| Perplexity | Concise and added citations                     |
| phi3       | Worked but was less stable                      |

---

### 🔹 Small Model Limitations

The local `phi3` model showed:

* Grammar errors
* Formatting inconsistencies
* Noisy outputs
* Less stable responses

This showed an important lesson:

> **Correctness alone is not enough. Reliability also matters.**

---

### 🔹 Local Models vs API Models

| Type        | Advantages                  | Limitations                           |
| ----------- | --------------------------- | ------------------------------------- |
| Local Model | Free to run, more private   | Can be weaker or less stable          |
| API Model   | Powerful and easy to access | Requires API usage and can cost money |

---

### Final Insight

> **LLM performance depends on both model capability and prompt quality.**

A simple way to remember this is:

```text
LLM Performance
      =
Model Capability × Prompt Quality
```

---

## ✅ Day 2 — Dynamic Model Routing & Streaming UI

Built a multi-model AI interface using Gradio.

### Learned

* Gradio Blocks
* Multiple model selection
* Real-time token streaming
* Python generators
* `yield`
* Google GenAI SDK

### What is streaming?

Normally, an application waits for the entire answer.

With streaming, the answer appears as it is generated.

```text
Token 1 → displayed
Token 2 → displayed
Token 3 → displayed
Token 4 → displayed
```

### Key Takeaway

> Streaming makes an AI application feel faster because the user can see the answer while it is being generated.

---

## ✅ Day 3 — Conversation History & System Personas

Learned how AI applications maintain conversations and control the behavior of an AI assistant.

### Learned

* Conversation history
* Stateless LLM APIs
* System instructions
* AI personas
* Brand behavior
* Conversation memory

### Conversation Flow

```text
User Message
     ↓
Store Conversation
     ↓
Send History + New Message
     ↓
LLM
     ↓
Response
```

### System Persona

A system instruction can tell the model how it should behave.

For example:

```text
You are a helpful customer support assistant.
Answer clearly and politely.
```

### Key Takeaway

> Conversation memory and system instructions help create more useful and consistent AI assistants.

---

## ✅ Day 4 — Function Calling & Relational Database Tools

Built an AI Agent that can use external tools and a database.

### Implemented

* Gemini integration
* SQLite database
* Function calling
* Multiple tools
* Data aggregation

### What is Function Calling?

Function calling allows an LLM to decide that it needs a specific function or tool.

Example:

```text
User:
"What is the total sales?"

        ↓

LLM decides:
"I need database information."

        ↓

Database Function
        ↓
Database Result
        ↓
LLM
        ↓
Final Answer
```

### Key Takeaway

> Function calling allows an LLM to work with external systems instead of relying only on information inside the model.

---

## ✅ Day 5 — Multi-Modal Database Agent & Vocal Terminal

🔗 Project: [https://github.com/srilekha42/flighty-airline-agent](https://github.com/srilekha42/flighty-airline-agent)

Built a **Flighty Airlines Premium Concierge Terminal** combining database tools, an AI agent, text responses, and voice output.

---

### 🔹 1. Database Tool Layer

Connected the AI application to a SQLite database containing flight price information.

The system converts natural-language questions into database lookups.

For example:

```text
User:
"Find the cheapest flight."

        ↓

AI Agent
        ↓

Database Tool
        ↓

SQLite
        ↓

Flight Information
        ↓

AI Response
```

This is better than asking the LLM to guess database information.

---

### 🔹 2. Text-to-Speech

Integrated Gemini Text-to-Speech to allow the agent to provide spoken responses in addition to text.

### Implemented

* Text responses
* Voice responses
* Audio streaming
* Temporary audio files
* Unique timestamp-based file names

---

### 🔹 3. Error Handling

Added error handling to protect the application from problems such as:

* API rate limits
* `429 Resource Exhausted`
* Network failures
* Unexpected application states

```text
Application
    ↓
Try Operation
    ↓
Success → Continue
    ↓
Error → Handle Safely
```

### Key Takeaway

> Production applications need error handling so that one API or network problem does not completely break the application.

---

### 🔹 4. State Handling

Worked with Gradio chat state and application data.

The system manages:

* Conversation history
* Internal lists
* Dictionaries
* Dashboard values
* Audio streams

### Key Takeaway

> A multimodal AI application needs to keep different types of information synchronized while the user interacts with it.

---

# 📌 Week 3 — Open-Source LLMs & Standalone Projects

Week 3 focused on Hugging Face, open-source models, tokenization, Transformer architecture, quantization, streaming inference, and multimodal AI.

---

## ✅ Day 1 — Hugging Face & Google Colab

Learned how to work with open-source AI models.

### Tools

* Hugging Face
* Google Colab
* NVIDIA T4 GPU
* GPU memory / VRAM

### What is Hugging Face?

Hugging Face provides a large ecosystem of open-source AI models, datasets, and tools.

### What is a GPU?

A GPU can perform many calculations in parallel, which makes it useful for running AI models.

### What is VRAM?

VRAM is the memory available on the GPU.

AI models need enough VRAM to load and run.

### Built

* Text-to-Speech application
* Image generation application

### Key Takeaway

> Open-source models can be downloaded and run using available hardware such as cloud GPUs.

---

## ✅ Day 2 — Hugging Face Pipelines

Learned how Hugging Face pipelines make it easier to use AI models.

### Worked With

* Sentiment Analysis
* Named Entity Recognition
* Question Answering
* Summarization
* Translation
* Zero-Shot Classification
* Text Generation
* Image Generation
* Text-to-Speech

### Pipeline

A pipeline provides a simple way to perform a specific AI task without manually handling every model step.

### Key Takeaway

> Pipelines make it easier to quickly experiment with different AI tasks and models.

---

## ✅ Day 3 — Tokenizers, Special Tokens & Chat Templates

Learned how text is prepared before it reaches an LLM.

### What is Tokenization?

Tokenization breaks text into smaller pieces called tokens.

```text
"Hello, how are you?"
          ↓
       Tokens
          ↓
      Token IDs
          ↓
         LLM
```

The model processes these token IDs.

---

### Special Tokens

Models can use special tokens to represent things such as:

* Start of a conversation
* End of a response
* User message
* Assistant message

---

### Chat Templates

Different models may expect conversations in different formats.

A chat template converts messages into the format expected by the selected model.

### Key Takeaway

> Before an LLM processes a conversation, the text must be converted into the token and message format expected by that model.

---

## ✅ Day 4 — Transformer Architecture, Quantization & Streaming

Learned the basic internal flow of a Transformer-based language model.

### Basic Architecture

```text
Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer Layers
 ↓
LM Head
 ↓
Next Token
```

---

### 🔹 Embedding Layer

Converts token IDs into numerical representations that the model can process.

---

### 🔹 Transformer / Decoder Layers

Process the information using components such as:

* Self-Attention
* MLP layers

---

### 🔹 LM Head

Uses the processed information to predict the next token.

The model repeatedly predicts the next token to generate a complete response.

---

## 🔹 Quantization

Quantization reduces the amount of memory required to run a model.

For example:

```text
Higher Precision
      ↓
Lower Precision
      ↓
4-bit Model
```

### Benefits

* Lower memory usage
* Easier local model execution
* Allows larger models to run on smaller hardware

---

## 🔹 Streaming Inference

Used:

* `model.generate()`
* `TextStreamer`

Instead of waiting for the complete answer:

```text
Token → Token → Token → Token
```

the output can be displayed as it is generated.

### Key Takeaway

> Quantization helps reduce model memory usage, while streaming improves the user experience.

---
## ✅ Day 5 — Multi-Modal Audio-to-Minutes Generator

🔗 Project Repository: https://github.com/srilekha42/audio-to-minutes-generator

Built an end-to-end AI application that converts a meeting audio file into structured meeting minutes.

The project combines **Speech-to-Text** and a **Language Model** to automatically understand a meeting and create a useful summary.

---

### 🎯 What Does This Project Do?

Normally, after a meeting, someone has to:

- Listen to the meeting recording
- Write down important discussion points
- Note the decisions
- Identify action items
- Prepare meeting minutes

This project automates this process.

The user provides a meeting audio file, and the application produces:

- Executive Summary
- Key Discussion Points
- Decisions Made
- Action Items
- Next Steps

---

### 🔄 Complete Pipeline

```text
Meeting Audio
      ↓
Audio Preprocessing
      ↓
Whisper-Small
      ↓
Speech-to-Text
      ↓
Raw Transcript
      ↓
Transcript Chunking
      ↓
Qwen2.5-0.5B-Instruct
      ↓
AI Understanding & Summarization
      ↓
Structured Meeting Minutes
### Key Takeaway

> Different AI models can be combined to solve different parts of one real-world problem.
 
---


# 🧠 Week 4 — Model Selection & Evaluation

Week 4 focuses on answering an important question:

> **Which AI model should we use for a particular task?**

Instead of always selecting the largest model, I learned to consider:

- Intelligence
- Accuracy
- Cost
- Speed
- Latency
- Context window
- Task requirements
- Benchmark performance

---

## ✅ Day 1 — Model Selection Strategy & Benchmarks

Learned how to systematically select a model for a production task.

### Model Specifications

Compared models using:

* Parameter count
* Training data
* Context window
* Knowledge cutoff
* API cost
* Speed
* Latency
* Performance

---

## 🔹 Chinchilla Scaling Laws

Learned about the relationship between:

* Model parameters
* Training tokens
* Model performance

The important idea is:

> A larger model is not automatically better if it is not trained with enough data.

---

## 🔹 Benchmarks

Explored difficult AI benchmarks such as:

* GPQA
* MMLU-Pro
* AIME
* LiveCodeBench
* MuSR
* Humanity's Last Exam (HLE)

These benchmarks test areas such as:

* Knowledge
* Mathematics
* Coding
* Reasoning
* Expert-level questions

---

## 🔹 Benchmark Limitations

Learned that benchmarks are useful but not perfect.

### Contamination

A model may have seen benchmark questions during training.

### Saturation

A benchmark may become too easy for newer models and stop showing meaningful differences.

### Narrow Testing

One benchmark usually measures only certain abilities.

Therefore:

> **A high benchmark score does not automatically mean the model is the best choice for every real-world application.**

---

## 🔹 Forced Reasoning

Compared normal prompting with prompts that encourage step-by-step reasoning.

The purpose was to test whether additional reasoning guidance could improve performance on logical tasks.

### Basic Idea

```text
Question
   ↓
Normal Prompt
   ↓
Answer

Question
   ↓
Reasoning Prompt
   ↓
More Structured Reasoning
   ↓
Answer
```

### Key Takeaway

> Model selection should consider the actual task instead of relying only on benchmark scores or model size.

---

## ✅ Day 2 — AI Leaderboards & Blind A/B Testing

Learned how AI leaderboards can help compare different AI models.

---

## 🏆 What is an AI Leaderboard?

An AI leaderboard is like a **scoreboard for AI models**.

It can compare models based on:

* Intelligence
* Speed
* Cost
* Latency
* Context window
* Human preference

Leaderboards are useful for **shortlisting models**.

However:

> **The final model should be tested on the actual task.**

---

## 🔹 Artificial Analysis

Used to compare AI models across areas such as:

* Intelligence
* Speed
* Latency
* Cost

A useful goal is:

```text
High Intelligence
       +
Low Cost
       =
Good Value
```

---

## 🔹 Vellum

Useful for quickly checking:

* Context windows
* Token pricing
* Latency
* Model performance

---

## 🔹 Scale AI SEAL & HLE

Explored specialized model evaluations and difficult benchmarks, including **Humanity's Last Exam**.

---

## 🔹 LiveBench

Learned about fresh model evaluation using regularly updated questions.

The goal is to reduce the chance that models perform well simply because they have already seen the benchmark questions.

---

## 🔹 LM Arena / Chatbot Arena

Learned about **blind human A/B testing**.

Two anonymous AI models answer the same question.

```text
            Same Prompt
                ↓
       ┌────────┴────────┐
       ↓                 ↓
    Model A           Model B
       ↓                 ↓
    Answer A           Answer B
       └────────┬────────┘
                ↓
          Human Vote
                ↓
        A / B / Tie
                ↓
        Reveal Models
```

The model identities are hidden while the user compares the answers.

This helps reduce bias.

---

# 🧪 Practical Project — Local Model Arena

Built a simple **Blind A/B Model Evaluator** using the Groq API.

### Models Tested

* `llama-3.3-70b-versatile`
* `llama-3.1-8b-instant`

The program randomly assigns the models as Model A and Model B.

---

## Experiment

### Prompt

> "Explain what an API is to a beginner."

### Model A

The response:

* Used a restaurant analogy
* Explained API endpoints
* Explained API requests
* Explained API responses
* Covered REST
* Covered GraphQL
* Covered SOAP
* Gave a Gmail API example

It was detailed and thorough.

### Model B

The response:

* Used a restaurant analogy
* Explained Client = Customer
* Explained API = Waiter
* Explained Server = Kitchen
* Gave a simple software example

It was shorter and easier for a beginner to understand.

### Result

**Winner: Model B — `llama-3.1-8b-instant`**

### Observation

The larger model did not automatically produce the preferred answer.

For this particular beginner-level task, the smaller model was preferred because its answer was:

* Clear
* Simple
* Focused
* Beginner-friendly

### Key Insight

> **Model size does not always determine which model is best.**

A smaller model can sometimes be a better choice when the task is simple and speed or cost is important.

---

### Lesson Learned

> AI models and APIs change over time, so developers need to check the currently supported models before using them.

---

# 💼 Commercial AI Use Cases

Learned three common ways companies can use AI.

---

## 1. Automation

AI performs repetitive work.

Example:

> Automatically translating emails.

```text
Many Emails
    ↓
   AI
    ↓
Translated Emails
```

---

## 2. Augmentation

AI works together with humans.

Example:

> An AI coding assistant helps a programmer write and debug code.

The human remains involved in the decision-making process.

---

## 3. Differentiation

AI enables a company to create a new capability.

Example:

> An AI agent that independently researches information and creates a report.

### Key Insight

> A company's unique data can become an important advantage when building AI products.

---

# 🛠️ Projects Built During the Journey

## 🔹 Chat API

Learned basic LLM API interaction.

---

## 🔹 Local LLM with Ollama

Learned how to run an LLM locally using Ollama.

---

## 🔹 Webpage Summarizer

Built a pipeline that extracts webpage content and generates a summary.

---

## 🔹 Structured Summarizer

Built an LLM pipeline with JSON output and validation.

---

## 🔹 AI Brochure Generator

🔗 [https://github.com/srilekha42/ai-brochure-generator](https://github.com/srilekha42/ai-brochure-generator)

Built a system that converts company website information into a structured brochure.

---

## 🔹 Multi-Model Streaming UI

Built an interactive Gradio application that allows model selection and streams responses in real time.

---

## 🔹 Conversation Memory Assistant

Built an AI assistant that maintains conversation context and follows a defined system persona.

---

## 🔹 Function Calling Database Agent

Built an AI application that uses functions and SQLite to retrieve information.

---

## 🔹 Flighty Airlines Premium Concierge Terminal

🔗 [https://github.com/srilekha42/flighty-airline-agent](https://github.com/srilekha42/flighty-airline-agent)

Built a multimodal airline assistant that combines:

* AI agent
* SQLite database
* Function calling
* Text responses
* Text-to-Speech
* Audio streaming
* Error handling
* Gradio state management

---

## 🔹 Hugging Face NLP Applications

Built applications for:

* Sentiment Analysis
* Named Entity Recognition
* Question Answering
* Summarization
* Translation
* Zero-Shot Classification
* Text Generation
* Image Generation
* Text-to-Speech

---

## 🔹 Audio-to-Minutes Generator

Built an end-to-end application that converts meeting audio into structured meeting minutes. 
https://github.com/srilekha42/audio-to-minutes-generator

---

## 🔹 Forced Reasoning Evaluator

Built an experiment to compare normal prompting with reasoning-focused prompting.

---

## 🔹 Local Model Arena

Built a blind A/B testing system to compare two AI models using the same prompt.

---

# 🧠 Key Concepts Learned

## LLM Basics

* LLMs generate text probabilistically.
* The same prompt can sometimes produce different responses.
* Model output should be validated in reliable applications.
* Prompt quality affects model behavior.

---

## Tokens

* LLMs process tokens instead of raw text.
* More tokens generally mean more usage and cost.
* Conversation history can increase token usage.

---

## Context Window

* The context window is the amount of information a model can handle at one time.
* It can include instructions, conversation history, user input, and output.

---

## Memory

* LLM APIs are generally stateless.
* Applications can provide conversation history to create the experience of memory.

---

## Prompt Engineering

* Better prompts can produce more controlled outputs.
* Clear instructions reduce ambiguity.
* Output format can be specified.
* Reasoning prompts can sometimes improve performance.

---

## Function Calling

* Allows an LLM to use external functions and tools.
* Useful for databases, APIs, calculations, and other external systems.

---

## Agents

A simple model of an agent is:

```text
LLM + Loop + Tools
```

The agent can decide what action to take, use a tool, observe the result, and continue working.

---

## Open-Source Models

* Hugging Face provides access to many open-source models.
* Ollama can be used to run models locally.
* Local models can provide privacy and avoid some API costs.

---

## Tokenization

* Text is converted into tokens.
* Tokens are converted into token IDs.
* Models process these IDs.

---

## Transformers

Basic Transformer flow:

```text
Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer Layers
 ↓
LM Head
 ↓
Next Token
```

---

## Quantization

* Reduces model memory requirements.
* Makes it easier to run models on limited hardware.
* Lower precision can allow larger models to fit into available memory.

---

## Streaming

* Shows generated output progressively.
* Improves the user experience.
* Reduces the feeling of waiting for the complete response.

---

## Model Selection

A model should be selected based on:

* Task
* Accuracy
* Cost
* Speed
* Latency
* Context requirements
* Model capability

---

## Benchmarks

Benchmarks help compare models, but they have limitations.

Important limitations include:

* Contamination
* Saturation
* Narrow task coverage

---

## Leaderboards

Leaderboards help shortlist models.

But:

> **A leaderboard should not be the only reason for choosing a model.**

The model should also be tested on the actual task.

---

## Blind A/B Testing

Blind A/B testing means:

```text
Same Prompt
   ↓
Model A + Model B
   ↓
Hide Model Names
   ↓
Compare Answers
   ↓
Vote
   ↓
Reveal Models
```

This helps reduce bias when comparing models.

---

# ⚙️ Tech Stack

| Technology                 | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| **Python**                 | Main programming language                |
| **OpenAI-compatible APIs** | LLM interaction                          |
| **Groq API**               | Fast LLM inference and model experiments |
| **Google GenAI SDK**       | Gemini integration                       |
| **Gradio**                 | Interactive AI interfaces                |
| **Ollama**                 | Running LLMs locally                     |
| **Hugging Face**           | Open-source models and tools             |
| **Transformers**           | Working with Transformer models          |
| **Diffusers**              | Image generation                         |
| **BeautifulSoup**          | Webpage parsing                          |
| **Whisper**                | Audio transcription                      |
| **SQLite**                 | Database storage                         |
| **Google Colab**           | Cloud GPU experiments                    |
| **Python-dotenv**          | Environment variable management          |

---

# 📂 Repository Structure

```text
llm-engineering-journey/
│
├── week1/
│   ├── day1/
│   ├── day2/
│   ├── day3/
│   ├── day4/
│   └── day5/
│
├── week2/
│   ├── day1/
│   ├── day2/
│   ├── day3/
│   ├── day4/
│   └── day5/
│
├── week3/
│   ├── day1/
│   ├── day2/
│   ├── day3/
│   ├── day4/
│   └── day5/
│
├── week4/
│   ├── day1/
│   └── day2/
│
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Projects

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd llm-engineering-journey
```

---

## 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Keys

Create a `.env` file for projects that require API access.

Example:

```text
OPENAI_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

> Never upload real API keys to GitHub.

---

## 5. Run a Project

Move into the required project folder and run its Python file.

Example:

```bash
python app.py
```

For the Week 4 Day 2 Local Model Arena:

```powershell
cd week4/day2
python mini_arena.py
```

---

# 🎯 Final Learning Goal

This repository represents my progress from **basic LLM usage to practical LLM engineering**.

The journey started with:

```text
What is an LLM?
       ↓
How do I call an LLM API?
       ↓
How do I control its output?
       ↓
How do I make it reliable?
       ↓
How do I give it memory?
       ↓
How do I give it tools?
       ↓
How do I build agents?
       ↓
How do I use open-source models?
       ↓
How do LLMs process tokens?
       ↓
How do Transformers work?
       ↓
How can I run models efficiently?
       ↓
How do I choose the right model?
       ↓
How do I evaluate models?
       ↓
How do I compare models in real tasks?
       ↓
How do I build useful AI applications?
```

---

# ⭐ Overall Takeaways

Throughout this journey, I learned that building LLM applications is not just about sending a prompt and getting an answer.

A good LLM application requires:

```text
Good Model
    +
Good Prompt
    +
Good Data
    +
Tools
    +
Validation
    +
Error Handling
    +
Evaluation
    +
Cost Awareness
    ↓
Reliable AI Application
```

The most important lesson so far is:

> **Do not simply ask which AI model is the best. Ask which model, prompt, tools, and architecture are best for the specific problem.**

---

# 🚀 Learning Philosophy

> **Learn → Build → Break → Debug → Improve → Repeat**

```
```
