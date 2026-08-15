import platform
import subprocess
import json
import os

def get_system_info() -> dict:
    info = {
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
    }
    
    for compiler in ["g++", "clang++", "cl"]:
        try:
            res = subprocess.run([compiler, "--version"], capture_output=True, text=True, check=True)
            info["compiler"] = compiler
            info["compiler_version"] = res.stdout.splitlines()[0]
            break
        except (subprocess.SubprocessError, FileNotFoundError):
            continue
            
    if "compiler" not in info:
        info["compiler"] = "None found"
        
    return info

if __name__ == "__main__":
    print(json.dumps(get_system_info(), indent=2))