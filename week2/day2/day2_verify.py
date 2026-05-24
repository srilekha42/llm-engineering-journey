import gradio as gr
from google import genai

# Use your new, regenerated key safely here
MY_API_KEY = "PASTE_YOUR_NEW_SAFE_AIZA_KEY_HERE"

client = genai.Client(api_key=MY_API_KEY)

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

# --- UI LAYOUT ---
with gr.Blocks(title="Live Gemini Router") as demo:
    gr.Markdown("# 🤖 Week 2 Day 2: Live Gemini UI Dashboard")
    
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

# Strict check: This MUST use double underscores!
if __name__ == "__main__":
    print("⏳ Starting your local Gradio application server...")
    demo.launch()