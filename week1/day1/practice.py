import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model
model = genai.GenerativeModel("models/gemini-flash-latest")

# Prompt (you can change this later)
prompt = "Explain AI in simple words"

# Get response
response = model.generate_content(prompt)

# Print output
print(response.text)