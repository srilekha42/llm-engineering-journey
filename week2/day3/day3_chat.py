import os
from pathlib import Path
from dotenv import load_dotenv
import gradio as gr
from google import genai
from google.genai import types

# 1. Secure Absolute Path Setup for the .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

# 2. Initialize the Google GenAI Client
client = genai.Client()

# 3. Define the Global Store Persona (System Instruction)
STORE_PERSONA = """You are a helpful assistant in a clothes store. 
You should try to gently encourage the customer to try items that are on sale.
Hats are 60% off and most other items are 50% off. 
If the customer asks for shoes, tell them shoes are not on sale today, but remind them to look at hats."""

# 4. The Gradio Chat Callback Function
def chat_callback(message: str, history: list):
    """
    Gradio automatically passes:
    - message: A string representing the current user input
    - history: A list of dictionaries representing past messages
    """
    model_name = "gemini-2.5-flash"
    formatted_contents = []
    
    # 5. Format conversation history into standard Google Content objects safely
    for turn in history:
        role = "user" if turn["role"] == "user" else "model"
        raw_content = turn["content"]
        
        # Extract the pure string text out of Gradio's multimodal structure
        if isinstance(raw_content, list):
            # Loop through elements to find text components
            text_parts = [item["text"] for item in raw_content if "text" in item]
            clean_text = " ".join(text_parts)
        else:
            clean_text = str(raw_content)
            
        formatted_contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=clean_text)]
            )
        )
    
    # 6. Append the current user prompt (Gradio passes the input message as a string)
    formatted_contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=str(message))]
        )
    )
    
    # 7. Apply dynamic context injection (Basic RAG simulation)
    current_persona = STORE_PERSONA
    if "belt" in message.lower():
        current_persona += "\nCRITICAL CONTEXT: The store does not sell belts. If asked for belts, point out other items on sale like hats."

    # 8. Request the real-time token stream from Google Cloud
    config = types.GenerateContentConfig(
        system_instruction=current_persona,
        temperature=0.7
    )
    
    response_stream = client.models.generate_content_stream(
        model=model_name,
        contents=formatted_contents,
        config=config
    )
    
    # 9. Clear and accumulate text chunks into Gradio using yield
    response_text = ""
    for chunk in response_stream:
        if chunk.text:
            response_text += chunk.text
            yield response_text

# 10. Launch the simple ChatInterface UI wrapper
demo = gr.ChatInterface(
    fn=chat_callback,
    title="🛍️ Week 2 Day 3: AI Store Assistant with Memory",
    description="Ask about shirts, shoes, or belts to see how system rules and history work!"
)

if __name__ == "__main__":
    demo.launch()