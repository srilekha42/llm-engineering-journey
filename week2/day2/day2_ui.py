import os
import gradio as gr
from google import genai
from dotenv import load_dotenv

# --- BULLETPROOF ENV PATH LOOKUP ---
# This looks up 2 levels from this file to find the root directory .env file
current_file_dir = os.path.dirname(os.path.abspath(__file__))
root_env_path = os.path.abspath(os.path.join(current_file_dir, "../../.env"))
load_dotenv(dotenv_path=root_env_path)

# Fetch the variable safely from memory
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(f"❌ Error: Could not read GEMINI_API_KEY from path: {root_env_path}")

# Initialize client using the automatically injected environment variable
client = genai.Client(api_key=API_KEY)

def stream_gemini_response(prompt, model_choice):
    if model_choice == "Gemini Flash (Ultra Fast)":
        target_model = "gemini-2.5-flash"
    else:
        target_model = "gemini-2.5-pro"

    try:
        response_stream = client.models.generate_content_stream(
            model=target_model,
            contents=prompt,
        )
        text_accumulator = ""
        for chunk in response_stream:
            if chunk.text:
                text_accumulator += chunk.text
                yield text_accumulator
    except Exception as e:
        yield f"⚠️ Error: {str(e)}"

# --- GRADIO INTERFACE LAYOUT ---
with gr.Blocks(title="Live Gemini Router") as demo:
    gr.Markdown("# 🤖 Week 2 Day 2: Live Gemini UI Dashboard")
    gr.Markdown("No hardcoded keys. Reading clean configuration values via absolute path injection.")
    
    with gr.Row():
        with gr.Column():
            user_prompt = gr.Textbox(label="Your Prompt", placeholder="Type here...", lines=4)
            model_select = gr.Dropdown(
                choices=["Gemini Flash (Ultra Fast)", "Gemini Pro (Deep Reasoning)"], 
                value="Gemini Flash (Ultra Fast)", 
                label="Choose Engine"
            )
            submit_button = gr.Button("⚡ Run Inference", variant="primary")
        with gr.Column():
            output_markdown = gr.Markdown(label="Live Stream Output")

    submit_button.click(
        fn=stream_gemini_response,
        inputs=[user_prompt, model_select],
        outputs=output_markdown
    )

if __name__ == "__main__":
    print("⏳ Starting your local Gradio application server...")
    demo.launch()