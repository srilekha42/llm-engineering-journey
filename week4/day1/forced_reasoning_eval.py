import os
from groq import Groq

# Initialize Groq client using the GROQ_API_KEY environment variable
client = Groq()

PUZZLE = """
Four people (Alice, Bob, Charlie, David) are standing in a line facing north.
1. Bob is directly behind Alice.
2. Charlie is standing somewhere behind Bob.
3. David is standing directly in front of Alice.
Questions: Who is at the very front of the line, and who is third from the front?
"""

PROMPT_DIRECT = f"""
Solve this logic puzzle:
{PUZZLE}

Output ONLY a JSON object formatted as:
{{"front": "Name", "third": "Name"}}
Do not show your work or write any text outside the JSON.
"""

PROMPT_REASONING = f"""
Solve this logic puzzle step-by-step:
{PUZZLE}

Follow these steps strictly:
1. Identify the relative order from front to back step-by-step.
2. Write down the full line order from 1st (front) to 4th (back).
3. Conclude with the final answer.

At the very end, output:
FINAL ANSWER: {{"front": "Name", "third": "Name"}}
"""

def run_eval(model_name="llama-3.3-70b-versatile"):
    print(f"=== TESTING GROQ MODEL: {model_name} ===\n")

    print("--- TEST 1: DIRECT OUTPUT (NO REASONING TOKENS) ---")
    res_direct = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": PROMPT_DIRECT}],
        temperature=0.0,
    )
    print(res_direct.choices[0].message.content)

    print("\n" + "="*50 + "\n")

    print("--- TEST 2: FORCED REASONING (STEP-BY-STEP) ---")
    res_reasoning = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": PROMPT_REASONING}],
        temperature=0.0,
    )
    print(res_reasoning.choices[0].message.content)

if __name__ == "__main__":
    run_eval()