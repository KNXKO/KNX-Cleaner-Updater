import subprocess
import sys

def run_winget():
    try:
        cmd = 'cmd /k winget upgrade && winget update --all'
        subprocess.run(cmd, shell=True, check=True)
        print("Windows applications have been successfully updated.")
    except subprocess.CalledProcessError:
        print("Error: Failed to run the command.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
