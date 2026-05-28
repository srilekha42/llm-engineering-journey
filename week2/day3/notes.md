# 📝 Week 2 Day 3: Conversational AI & System Personas

## 🚀 Key Achievements
* **Built a Stateful Chat Application:** Moved away from single-turn stateless responses by maintaining and processing full conversational history states.
* **Implemented Custom Personas:** Leveraged `system_instruction` boundaries to enforce business logic, rules, and an on-brand corporate tone.
* **Multi-Shot Example Training:** Biased model prediction accuracy by embedding rigid contextual examples inside the core system rules.
* **Dynamic Prompt Context Injection:** Programmed a conditional keyword trigger that appends rules on the fly based on runtime user inputs (the fundamental basis of RAG).

## 💡 Engineering Insights
* **The Illusion of Memory:** LLM cloud endpoints do not "remember" anything. Memory is engineered on the backend by packing the entire array of past dialogue and sending it alongside every new user prompt.
* **Handling Multimodal Payloads:** Discovered that modern UI frameworks (like Gradio 6+) pass chat history logs as granular multimodal structures (`list` of dictionaries) rather than raw text strings, requiring clean backend parsing.