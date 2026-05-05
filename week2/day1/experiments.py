# experiments.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"   


def ask(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        # ✅ Expected case
        if "response" in data:
            return data["response"].strip()

        # ❌ Unexpected format
        else:
            return f"⚠️ Unexpected response:\n{data}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# -------------------------
# Experiment 1: Basic Output
# -------------------------
print("\n=== Experiment 1: Basic Explanation ===")
prompt = "Explain recursion in 2 simple sentences."
print(ask(prompt))


# -------------------------
# Experiment 2: Reasoning Test
# -------------------------
print("\n=== Experiment 2: Reasoning (No Guidance) ===")
prompt = """A bat and a ball together cost $2.20.
The bat costs $1 more than the ball.
How much does the ball cost?
Answer only with the number."""
print(ask(prompt))


print("\n=== Experiment 2: Reasoning (Step-by-step) ===")
prompt = """Solve step by step:
A bat and a ball together cost $2.20.
The bat costs $1 more than the ball."""
print(ask(prompt))


# -------------------------
# Experiment 3: Prompt Control
# -------------------------
print("\n=== Experiment 3: Format Control ===")
prompt = """You are a strict teacher.
Explain Python in exactly 5 bullet points.
Each bullet must be 1 line only.
No extra text."""
print(ask(prompt))


# -------------------------
# Experiment 4: Efficiency Test
# -------------------------
print("\n=== Experiment 4: Verbosity Check ===")
prompt = "Explain how a search engine works."
print(ask(prompt))