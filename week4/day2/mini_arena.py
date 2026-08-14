import os
import random
import time
from groq import Groq

# Uses GROQ_API_KEY from environment or directly initialized
client = Groq()

# Production supported models on Groq
CANDIDATE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant"
]

def run_blind_arena(prompt: str):
    # Select the two models and shuffle their display order
    models = CANDIDATE_MODELS.copy()
    random.shuffle(models)
    model_a, model_b = models[0], models[1]
    
    print(f"\nPrompt: \"{prompt}\"")
    
    print("\n" + "="*50)
    print("🤖 Model A generating...")
    t0 = time.time()
    res_a = client.chat.completions.create(
        model=model_a,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    time_a = time.time() - t0
    ans_a = res_a.choices[0].message.content
    print(ans_a)

    print("\n" + "="*50)
    print("🤖 Model B generating...")
    t0 = time.time()
    res_b = client.chat.completions.create(
        model=model_b,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    time_b = time.time() - t0
    ans_b = res_b.choices[0].message.content
    print(ans_b)
    print("\n" + "="*50)

    # Blind Voting
    vote = input("\nWhich response was better? Enter (A/B/Tie): ").strip().upper()
    
    # Reveal identity & latency metrics
    print("\n🎉 REVEALING MODELS:")
    print(f"Model A: {model_a} (Time: {time_a:.2f}s)")
    print(f"Model B: {model_b} (Time: {time_b:.2f}s)")
    print(f"Your Vote: {vote}")

if __name__ == "__main__":
    test_prompt = input("Enter a test prompt for the Arena (or press Enter for default): ").strip()
    if not test_prompt:
        test_prompt = "Explain what an API is to a beginner."
    run_blind_arena(test_prompt)