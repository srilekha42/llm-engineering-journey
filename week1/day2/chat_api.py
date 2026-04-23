from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Create client (Gemini via OpenAI-compatible endpoint)
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Chat request
response = client.chat.completions.create(
    model="models/gemini-2.0-flash",  # stable working model
    messages=[
        {"role": "system", "content": "Explain clearly like a teacher"},
        {"role": "user", "content": "What is Artificial Intelligence?"}
    ]
)

# Print response
print(response.choices[0].message.content)