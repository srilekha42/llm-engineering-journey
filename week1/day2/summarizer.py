from openai import OpenAI
import requests
from bs4 import BeautifulSoup

# ✅ Connect to local Ollama model
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything"  # not needed for local
)

# ✅ Take user input
url = input("Enter URL: ")

# ✅ Fetch webpage with headers (avoid blocking)
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# ✅ Error handling
if response.status_code != 200:
    print("❌ Failed to fetch webpage")
    print("Status code:", response.status_code)
    exit()

# ✅ Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Remove unwanted tags
for tag in soup(["script", "style"]):
    tag.decompose()

# Extract clean text
text = soup.get_text(separator=" ", strip=True)

# ✅ Debug: check text size
print("\n📊 Extracted text length:", len(text))

# ✅ Limit input size (token constraint handling)
if len(text) > 5000:
    text = text[:5000]

# ✅ Send to LLM
completion = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {
            "role": "system",
            "content": "Summarize the content into structured bullet points with headings. Avoid repetition and ensure factual correctness."
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

# ✅ Print output
print("\n===== SUMMARY =====\n")
print(completion.choices[0].message.content)