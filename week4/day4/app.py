import gradio as gr
from dotenv import load_dotenv
from system_info import get_system_info
from benchmark import PYTHON_PI_CODE
from translator import port_code
from runner import compile_and_benchmark

load_dotenv()
sys_info = get_system_info()

MODEL_MAP = {
    "Gemini 2.5 Flash (Google)": ("gemini", "gemini-2.5-flash"),
    "Gemini 1.5 Pro (Google)": ("gemini", "gemini-1.5-pro"),
    "Qwen 2.5 Coder 7B (Local Ollama)": ("ollama", "qwen2.5-coder:7b"),
    "DeepSeek Coder v2 (Local Ollama)": ("ollama", "deepseek-coder-v2"),
    "Llama 3.2 (Local Ollama)": ("ollama", "llama3.2"),
    "Llama 3.3 70B (Groq)": ("groq", "llama-3.3-70b-versatile"),
    "Qwen 2.5 Coder 32B (OpenRouter)": ("openrouter", "qwen/qwen-2.5-coder-32b-instruct")
}

def translate_and_run(python_code: str, model_selection: str):
    provider, model_id = MODEL_MAP[model_selection]
    try:
        cpp_code = port_code(provider, model_id, python_code, sys_info)
    except Exception as e:
        return f"Error during generation: {e}", "Generation failed."

    bench_res = compile_and_benchmark(cpp_code)
    if bench_res["success"]:
        report = (
            f"Execution Success!\n"
            f"Median Time: {bench_res['median_time']:.6f} s\n"
            f"Output:\n{bench_res['output']}"
        )
    else:
        report = f"Compilation/Run Note:\n{bench_res['error']}"

    return cpp_code, report

with gr.Blocks(title="Python to High-Performance C++ Pipeline") as demo:
    gr.Markdown("# Python to Optimized C++ Code Translator & Benchmark")
    gr.Markdown("Compare open-source and frontier models for code migration and performance optimization.")

    with gr.Row():
        py_input = gr.Code(label="Python Source Code", value=PYTHON_PI_CODE.strip(), language="python", lines=15)
        cpp_output = gr.Code(label="Generated C++ Code", language="cpp", lines=15)

    with gr.Row():
        model_dropdown = gr.Dropdown(
            label="Select Model",
            choices=list(MODEL_MAP.keys()),
            value="Gemini 2.5 Flash (Google)"
        )
        convert_btn = gr.Button("Convert & Benchmark", variant="primary")

    results_output = gr.Textbox(label="Benchmark / Compilation Status", lines=4)

    convert_btn.click(
        fn=translate_and_run,
        inputs=[py_input, model_dropdown],
        outputs=[cpp_output, results_output]
    )

if __name__ == "__main__":
    demo.launch()