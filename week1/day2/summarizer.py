from openai import OpenAI
import requests
from bs4 import BeautifulSoup

# Connect to local Ollama model
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything"
)

# Get URL from user
url = input("Enter URL: ")

# Fetch webpage
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Handle error
if response.status_code != 200:
    print("Failed to fetch webpage")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Remove unwanted tags
for tag in soup(["script", "style"]):
    tag.decompose()

# Extract text
text = soup.get_text(separator=" ", strip=True)

# Limit size (basic token handling)
if len(text) > 5000:
    text = text[:5000]

# Send to LLM
completion = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {
            "role": "system",
            "content": "Summarize the webpage clearly using bullet points."
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

# Print result
print("\n===== SUMMARY =====\n")
print(completion.choices[0].message.content)