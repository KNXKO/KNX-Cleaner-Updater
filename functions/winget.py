import subprocess
import sys

def run_winget():
    try:
        cmd = 'winget upgrade && winget update --all'
        subprocess.run(["cmd", "/c", cmd], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to run the command.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")