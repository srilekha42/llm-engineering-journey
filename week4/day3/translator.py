import os
import re

from google import genai


SYSTEM_PROMPT = """
You are an expert systems programmer.

Your task is to convert Python into high-performance,
fully optimized C++.

Respond ONLY with raw C++ code.

Do not include:
- Markdown code blocks
- Explanations
- Notes

The C++ code must:
1. Produce the same numerical result as the Python code.
2. Execute as fast as reasonably possible.
3. Use efficient algorithms.
4. Reduce unnecessary calculations.
5. Use hardware concurrency only when it provides a real benefit.
6. Be compatible with C++17.
"""


def build_user_prompt(
    python_code: str,
    sys_info: dict
) -> str:

    return f"""
Target Environment:

- OS: {sys_info.get('os')}
- Architecture: {sys_info.get('architecture')}
- Logical CPU Cores: {sys_info.get('cpu_count')}
- Compiler: {sys_info.get('compiler')}
- Compiler Version: {sys_info.get('compiler_version', 'latest')}

Convert the following Python code into optimized C++17:

{python_code}

Important:
- Preserve the numerical result.
- Optimize execution speed.
- Return ONLY valid C++17 source code.
"""


def clean_code(raw_response: str) -> str:

    cleaned = raw_response.strip()

    # Remove markdown code blocks if Gemini returns them
    cleaned = re.sub(
        r"^```(?:cpp|c\+\+|c)?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE
    )

    cleaned = re.sub(
        r"\s*```$",
        "",
        cleaned
    )

    return cleaned.strip()


def port_to_cpp(
    model_name: str,
    python_code: str,
    sys_info: dict
) -> str:

    # Prefer GEMINI_API_KEY
    api_key = os.getenv("GEMINI_API_KEY")

    # Fall back to GOOGLE_API_KEY
    if not api_key:
        api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:

        raise ValueError(
            "No Gemini API key found. "
            "Set GEMINI_API_KEY in your .env file."
        )


    print("Using Gemini API key...")


    client = genai.Client(
        api_key=api_key
    )


    user_prompt = build_user_prompt(
        python_code,
        sys_info
    )


    full_prompt = (
        SYSTEM_PROMPT
        + "\n\n"
        + user_prompt
    )


    response = client.models.generate_content(
        model=model_name,
        contents=full_prompt
    )


    if not response.text:

        raise ValueError(
            "Gemini returned an empty response."
        )


    return clean_code(
        response.text
    )