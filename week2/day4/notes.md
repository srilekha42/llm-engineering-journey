# 📝 Week 2 Day 4: Function Calling & Relational Database Tools

## 🚀 Key Achievements
* **Built a Functional AI Agent:** Connected the `gemini-2.5-flash` model directly to custom local python operations using function signatures as executable tools.
* **Integrated SQLite Tables:** Developed a live database query system using parameter variables to safeguard against traditional SQL injection vulnerabilities.
* **Mastered the Handshake Workflow:** Understood the multi-step network loop where the cloud model acts as a coordinator—emitting JSON parameter specifications for local runtime execution rather than performing direct code calls.

## 💡 Engineering Insights
* **SDK Function Mapping:** Modern AI SDKs automate the janky, nested JSON schema definitions required by legacy frameworks; passing raw python functions directly handles structural parsing on the fly.
* **Deterministic Execution over Probabilistic Text:** Solved the natural LLM limitation with mathematics and raw data lookup by routing requests to strict code components instead of trusting raw token predictions.