import requests

URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    response = requests.post(URL, json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"].strip()


print("===== MEMORY DEMO =====")

# ❌ Without history
print("\n--- Without History ---")

no_history_prompt = """
Answer the question exactly.

Question: What is my name?
Answer:
"""

print(ask_ollama(no_history_prompt))


# ✅ With history
print("\n--- With History ---")

with_history_prompt = """
My name is Sri.

Answer the question exactly.

Question: What is my name?
Answer:
"""

print(ask_ollama(with_history_prompt))


print("\n--- Conclusion ---")
print("LLM has no memory. It only uses provided context.")