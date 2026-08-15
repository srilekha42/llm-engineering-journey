import time

PYTHON_PI_CODE = '''
import time

def calculate_pi(iterations: int = 200_000_000) -> float:
    start_time = time.perf_counter()
    val = 0.0
    for i in range(iterations):
        val += (-1.0 if i % 2 == 1 else 1.0) / (2.0 * i + 1.0)
    pi_approx = val * 4.0
    elapsed = time.perf_counter() - start_time
    print(f"Python Result : {pi_approx:.10f}")
    print(f"Python Time   : {elapsed:.6f} seconds")
    return elapsed

calculate_pi()
'''

def run_python_benchmark() -> float:
    start = time.perf_counter()
    val = 0.0
    iterations = 200_000_000
    for i in range(iterations):
        val += (-1.0 if i % 2 == 1 else 1.0) / (2.0 * i + 1.0)
    pi_val = val * 4.0
    elapsed = time.perf_counter() - start
    print(f"Python Baseline Result : {pi_val:.10f}")
    print(f"Python Baseline Time   : {elapsed:.6f} s")
    return elapsed

if __name__ == "__main__":
    run_python_benchmark()