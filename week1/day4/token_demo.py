import tiktoken

# Load tokenizer for GPT-style models
enc = tiktoken.encoding_for_model("gpt-4")

texts = [
    "Hi",
    "This is a simple sentence",
    "exquisitely handcrafted response",
    "def add(a, b): return a + b",
    "Machine learning is powerful"
]

print("===== TOKENIZATION DEMO =====")

for text in texts:
    tokens = enc.encode(text)

    print("\n--------------------------")
    print(f"Text: {text}")
    print(f"Token count: {len(tokens)}")
    print(f"Tokens: {tokens}")

    # Decode back (sanity check)
    decoded = enc.decode(tokens)
    print(f"Decoded: {decoded}")