import os
import re
from openai import OpenAI
from google import genai

SYSTEM_PROMPT = """You are an expert systems programmer. 
Your task is to convert Python into high-performance, fully optimized C++.
Respond ONLY with raw C++ code. Do not include markdown codeblocks (```), explanations, or notes.
The code must produce the identical numerical output in the fastest execution time possible.
Optimize for hardware concurrency, cache efficiency, and compiler-level vectorization where applicable.
"""

def build_user_prompt(python_code: str, sys_info: dict) -> str:
    return f"""Target Environment:
- OS: {sys_info.get('os')} ({sys_info.get('architecture')})
- Logical CPU Cores: {sys_info.get('cpu_count')}
- Compiler: {sys_info.get('compiler')} ({sys_info.get('compiler_version', 'latest')})

Port this Python code to native high-performance C++:
{python_code}
"""

def clean_code(raw_response: str) -> str:
    cleaned = re.sub(r"^```(?:cpp|c\+\+|c)?\n", "", raw_response.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"\n```$", "", cleaned.strip(), flags=re.MULTILINE)
    return cleaned.strip()

def get_client_for_model(provider: str):
    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        return genai.Client(api_key=api_key)
    elif provider == "ollama":
        return OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    elif provider == "groq":
        return OpenAI(base_url="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)", api_key=os.getenv("GROQ_API_KEY"))
    elif provider == "openrouter":
        return OpenAI(base_url="[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)", api_key=os.getenv("OPENROUTER_API_KEY"))
    else:
        raise ValueError(f"Unknown provider: {provider}")

def port_code(provider: str, model_id: str, python_code: str, sys_info: dict) -> str:
    client = get_client_for_model(provider)
    user_prompt = build_user_prompt(python_code, sys_info)

    if provider == "gemini":
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        response = client.models.generate_content(
            model=model_id,
            contents=full_prompt
        )
        return clean_code(response.text)
    else:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
        response = client.chat.completions.create(
            model=model_id,
            messages=messages
        )
        return clean_code(response.choices[0].message.content or "")