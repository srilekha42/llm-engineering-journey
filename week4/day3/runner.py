import os
import shutil
import subprocess
import time
import statistics


def find_compiler():

    # Check common Windows C++ compilers
    compilers = [
        "g++",
        "clang++",
        "cl"
    ]


    for compiler in compilers:

        path = shutil.which(compiler)

        if path:

            return compiler


    return None


def compile_and_benchmark(
    cpp_code: str,
    source_path: str = "main.cpp",
    runs: int = 3
):

    compiler = find_compiler()


    # No compiler available
    if compiler is None:

        return {
            "success": False,
            "error": (
                "No C++ compiler found.\n"
                "Install MinGW-w64/GCC or "
                "Visual Studio Build Tools."
            )
        }


    try:

        # --------------------------------
        # Save C++ source
        # --------------------------------

        with open(
            source_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(cpp_code)


        executable = (
            os.path.splitext(source_path)[0]
            + ".exe"
        )


        # --------------------------------
        # Compile
        # --------------------------------

        if compiler == "cl":

            compile_command = [
                "cl",
                "/O2",
                "/EHsc",
                source_path,
                f"/Fe:{executable}"
            ]

            use_shell = True

        else:

            compile_command = [
                compiler,
                "-O3",
                "-march=native",
                "-std=c++17",
                source_path,
                "-o",
                executable
            ]

            use_shell = False


        print(
            f"  Compiling using {compiler}..."
        )


        compile_result = subprocess.run(
            compile_command,
            capture_output=True,
            text=True,
            shell=use_shell
        )


        if compile_result.returncode != 0:

            return {
                "success": False,
                "error": (
                    "C++ compilation failed:\n"
                    + compile_result.stdout
                    + compile_result.stderr
                )
            }


        # --------------------------------
        # Run benchmark
        # --------------------------------

        times = []

        output = ""


        print(
            f"  Running C++ benchmark "
            f"({runs} runs)..."
        )


        for _ in range(runs):

            start = time.perf_counter()


            run_result = subprocess.run(
                [executable],
                capture_output=True,
                text=True
            )


            end = time.perf_counter()


            if run_result.returncode != 0:

                return {
                    "success": False,
                    "error": (
                        "C++ execution failed:\n"
                        + run_result.stderr
                    )
                }


            execution_time = end - start

            times.append(
                execution_time
            )


            output = (
                run_result.stdout.strip()
            )


        median_time = statistics.median(
            times
        )


        return {
            "success": True,
            "median_time": median_time,
            "times": times,
            "output": output
        }


    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }