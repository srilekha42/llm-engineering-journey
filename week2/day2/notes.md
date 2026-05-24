# 📝 Week 2 Day 2 Notes: Making a Live Gemini Chat App

## 🚀 What I Did Today
1. **Tested the Connection:** Built a small test file (`day2_verify.py`) to make sure my computer could talk to Google's AI servers without any errors.
2. **Fixed the Env File Bug:** Wrote smart Python code that automatically finds the `.env` file at the root folder, no matter which subfolder I am working in. This means I never have to copy-paste my API key again!
3. **Built a Web Page:** Used `Gradio` to build a clean web interface with an input box, a model selection dropdown, a run button, and an output box.
4. **Added Live Streaming:** Instead of making the user wait for the whole answer to load, I used `yield` to stream words onto the screen one by one in real-time.

---

## 🏗️ How the App Works (The Callback Layout)

When you use the app, data moves in a simple loop:

1. **User Input:** You type a prompt in the browser box and click the orange "Run Inference" button.
2. **The Python Server:** Gradio catches your text and hands it to our backend Python function.
3. **The Cloud Call:** Python sends your prompt out to Google's Gemini servers.
4. **The Live Stream:** As Google generates the answer, it sends back tiny pieces of text. Our code uses a loop and the `yield` keyword to display each word on your screen instantly.

---

## 🧠 Easy Deep Dive: Self-Attention vs. Multi-Head Attention

These are the core engine parts inside modern AI brains (Transformers) that help them understand human language:

* **Self-Attention (The Core Engine):** This mechanism helps the AI understand words based on the context around them. For example, in the sentence *"The animal didn't cross the street because **it** was too tired,"* Self-Attention connects the word **"it"** back to **"animal."** It creates vectors called Queries ($Q$), Keys ($K$), and Values ($V$) to calculate how much attention every word should pay to every other word.
* **Multi-Head Attention (Parallel Lenses):** Instead of using just one Self-Attention engine, modern AI uses multiple engines running side-by-side in parallel. One "head" might look at grammar, another might look at pronouns, and another might look at verbs. At the end, it combines all their findings into a final projection matrix ($W^O$) to get a complete, robust understanding of the sentence.

---

## 🚨 The Big Problem: Our App Has No Memory!
Right now, the Gemini API is **stateless** (it forgets everything the moment it finishes typing). 

Because our code only sends the *current* text inside the box (`contents=prompt`), the AI cannot remember what you asked it two seconds ago. If you ask a follow-up question, it will get confused. To fix this, we will need to build a system that saves the chat history and sends the whole conversation back to Google every time.