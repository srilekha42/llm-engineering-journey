import subprocess
import time
import os
import platform

def compile_and_benchmark(cpp_source: str, source_path: str = "main.cpp", exec_name: str = "main_exec", runs: int = 3) -> dict:
    with open(source_path, "w", encoding="utf-8") as f:
        f.write(cpp_source)

    is_windows = platform.system() == "Windows"
    exec_path = f".\\{exec_name}.exe" if is_windows else f"./{exec_name}"

    compiler = "clang++" if platform.system() == "Darwin" else "g++"
    compile_cmd = [compiler, "-O3", "-std=c++20", "-pthread", source_path, "-o", exec_path]

    try:
        subprocess.run(compile_cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        return {"success": False, "error": "No C++ compiler found on PATH."}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": f"Compilation failed:\n{e.stderr}"}

    times = []
    output = ""
    for _ in range(runs):
        start = time.perf_counter()
        res = subprocess.run([exec_path], capture_output=True, text=True, check=True)
        end = time.perf_counter()
        times.append(end - start)
        output = res.stdout.strip()

    if os.path.exists(exec_path):
        os.remove(exec_path)

    times.sort()
    median_time = times[len(times) // 2]

    return {
        "success": True,
        "median_time": median_time,
        "all_times": times,
        "output": output
    }