from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything"
)

response = client.chat.completions.create(
    model="llama3.2:1b",        
    messages=[
        {"role": "system", "content": "Explain clearly like a teacher"},
        {"role": "user", "content": "What is Artificial Intelligence?"}
    ]
)

print(response.choices[0].message.content)