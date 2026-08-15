import os
from dotenv import load_dotenv

from system_info import get_system_info
from benchmark import PYTHON_PI_CODE, run_python_benchmark
from translator import port_to_cpp
from runner import compile_and_benchmark


load_dotenv()


# Current Gemini model
MODELS = [
    "gemini-2.5-flash"
]


def main():

    print("=== Step 1: System Identification ===")

    sys_info = get_system_info()

    print(
        f"OS: {sys_info.get('os')} | "
        f"Arch: {sys_info.get('architecture')} | "
        f"Compiler: {sys_info.get('compiler')}"
    )


    print("\n=== Step 2: Running Python Baseline ===")

    py_baseline_time = run_python_benchmark()


    results = {}


    print("\n=== Step 3: LLM Port & C++ Execution ===")


    for model_name in MODELS:

        print(f"\nRequesting C++ code from {model_name}...")

        try:

            # Ask Gemini to convert Python → C++
            cpp_code = port_to_cpp(
                model_name,
                PYTHON_PI_CODE,
                sys_info
            )

            print(
                f"C++ code generated successfully by "
                f"{model_name}."
            )


            # Compile and benchmark C++
            source_path = (
                f"main_{model_name.replace('-', '_')}.cpp"
            )

            bench_res = compile_and_benchmark(
                cpp_code,
                source_path=source_path
            )


            if bench_res["success"]:

                median_t = bench_res["median_time"]

                speedup = py_baseline_time / median_t


                results[model_name] = {
                    "time": median_t,
                    "speedup": speedup,
                    "output": bench_res["output"]
                }


                print(
                    f"  Result      : {bench_res['output']}"
                )

                print(
                    f"  Median Time : {median_t:.6f} s"
                )

                print(
                    f"  Speedup     : {speedup:.2f}x"
                )


            else:

                print(
                    f"  Execution/Compilation Error: "
                    f"{bench_res['error']}"
                )


        except Exception as e:

            print(
                f"  Execution Error: {e}"
            )


    print("\n=== Final Benchmark Summary ===")


    if not results:

        print("No successful C++ benchmark results.")


    for model, data in results.items():

        print(
            f"{model}: "
            f"{data['time']:.6f}s "
            f"({data['speedup']:.2f}x speedup)"
        )


if __name__ == "__main__":
    main()