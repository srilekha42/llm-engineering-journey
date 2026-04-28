from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import json
import re

# ✅ Connect to local Ollama model
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything"
)

# ✅ Take user input
url = input("Enter URL: ")

# ✅ Fetch webpage
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

# ✅ Debug
print("\n📊 Extracted text length:", len(text))

# ✅ Limit input size
if len(text) > 5000:
    text = text[:5000]

# 🧠 Extract JSON from messy output
def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group(0) if match else text

# 🧠 Safe JSON parse
def parse_json(text):
    try:
        return json.loads(text)
    except:
        return None

# ✅ First LLM call
completion = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {
            "role": "system",
            "content": """
You are a strict JSON generator.

Summarize the given article accurately and completely.

Requirements:
- Title must exactly match the article topic
- Summary must be at least 2-3 sentences
- key_points must be a list of simple strings (NOT objects, NOT dictionaries)
- Must contain at least 5 key points

Return ONLY valid JSON in this format:
{
  "title": "string",
  "summary": "string",
  "key_points": ["point1", "point2"]
}

Do not add extra text.
Do not explain anything.
"""
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

output = completion.choices[0].message.content

print("\n===== RAW OUTPUT =====\n")
print(output)

# ✅ Extract + Parse
clean_output = extract_json(output)
data = parse_json(clean_output)

# 🔁 Retry if JSON broken
if data is None:
    print("\n⚠️ Parsing failed. Retrying...")

    fix_prompt = f"""
Fix the following JSON. Return ONLY valid JSON.

{output}
"""

    retry = client.chat.completions.create(
        model="llama3.2:1b",
        messages=[
            {"role": "system", "content": "You fix broken JSON."},
            {"role": "user", "content": fix_prompt}
        ]
    )

    fixed_output = retry.choices[0].message.content

    print("\n===== FIXED OUTPUT =====\n")
    print(fixed_output)

    clean_fixed = extract_json(fixed_output)
    data = parse_json(clean_fixed)

# ✅ Final processing
if data:
    print("\n✅ Parsed JSON:\n", data)

    # 🔍 Schema validation
    if data.get("key_points"):
        if isinstance(data["key_points"][0], dict):
            print("\n⚠️ Fixing schema (objects → strings)...")
            data["key_points"] = [
                kp.get("name", "") for kp in data["key_points"]
            ]

    # 🔍 Content validation
    if not data.get("title") or not data.get("summary") or not data.get("key_points"):
        print("\n⚠️ Invalid content (missing fields)")

    if len(data.get("key_points", [])) < 5:
        print("\n⚠️ Not enough key points. Improving...")

        improve_prompt = f"""
Improve this JSON.

Requirements:
- At least 5 key_points
- key_points must be simple strings
- Summary must be 2-3 sentences
- Keep JSON valid

{data}
"""

        retry2 = client.chat.completions.create(
            model="llama3.2:1b",
            messages=[
                {"role": "system", "content": "You improve structured JSON."},
                {"role": "user", "content": improve_prompt}
            ]
        )

        improved_output = retry2.choices[0].message.content

        print("\n===== IMPROVED OUTPUT =====\n")
        print(improved_output)

        clean_improved = extract_json(improved_output)
        improved_data = parse_json(clean_improved)

        if improved_data:
            data = improved_data
            print("\n✅ Final Improved JSON:\n", data)
        else:
            print("\n❌ Improvement failed")

    # 🔍 Extra fields check
    allowed_keys = {"title", "summary", "key_points"}
    extra_keys = set(data.keys()) - allowed_keys
    if extra_keys:
        print(f"\n⚠️ Unexpected fields: {extra_keys}")

else:
    print("\n❌ Still failed after retry")