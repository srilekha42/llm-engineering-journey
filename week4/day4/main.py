import os
from dotenv import load_dotenv
from system_info import get_system_info
from benchmark import PYTHON_PI_CODE, run_python_benchmark
from translator import port_code
from runner import compile_and_benchmark

load_dotenv()

EVAL_MODELS = [
    ("Gemini 2.5 Flash", "gemini", "gemini-2.5-flash"),
    # Add any active local Ollama or Groq models you want evaluated
]

def main():
    print("=== Week 4 Day 4: Open & Frontier Model Code Benchmark ===")
    sys_info = get_system_info()
    print(f"Host: {sys_info['os']} | CPU Cores: {sys_info['cpu_count']} | Compiler: {sys_info['compiler']}")

    print("\n--- Running Python Baseline ---")
    py_baseline_time = run_python_benchmark()

    results = {}

    for label, provider, model_id in EVAL_MODELS:
        print(f"\n--- Testing: {label} ({model_id}) ---")
        try:
            cpp_code = port_code(provider, model_id, PYTHON_PI_CODE, sys_info)
            bench = compile_and_benchmark(cpp_code, source_path=f"main_{provider}.cpp")
            
            if bench["success"]:
                median_t = bench["median_time"]
                speedup = py_baseline_time / median_t
                results[label] = {"time": median_t, "speedup": speedup}
                print(f"  Status   : Success")
                print(f"  Time     : {median_t:.6f} s")
                print(f"  Speedup  : {speedup:.2f}x")
            else:
                print(f"  Failure  : {bench['error']}")
        except Exception as e:
            print(f"  Error    : {e}")

    print("\n=== Final Performance Table ===")
    print(f"{'Model':<25} | {'Median Time (s)':<16} | {'Speedup':<10}")
    print("-" * 55)
    for model_name, data in results.items():
        print(f"{model_name:<25} | {data['time']:<16.6f} | {data['speedup']:.2f}x")

if __name__ == "__main__":
    main()