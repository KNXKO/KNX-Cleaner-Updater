import os
import pygetwindow as gw
import subprocess
import pyautogui
import time

bcdedit_path = r'src\shortcuts\Bcdedit Optimizer.cmd'
win_optimize_path = r'src\shortcuts\Windows Optimization.bat'
cmd_path = r'src\shortcuts\cmd.lnk'

def run_win_optimize():
    try:
        os.startfile(win_optimize_path)
        print("Windows Optimize successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Windows Optimize: {e}")
        return False

def run_sfc():
    try:
        print("Running SFC scan... (this may take several minutes)")
        process = subprocess.Popen(
            ['sfc', '/scannow'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',
            errors='replace'
        )
        for line in process.stdout:
            print(line, end='')
        process.wait()
        codes = {
            0: "No integrity violations found.",
            2: "Corrupted files found and repaired.",
            3: "Corrupted files found, some could not be repaired.",
            4: "Scan could not be performed or was interrupted."
        }
        print(f"SFC: {codes.get(process.returncode, f'Finished with code {process.returncode}')}")
        print("Full log: C:\\Windows\\Logs\\CBS\\CBS.log")
        return process.returncode in (0, 2)
    except Exception as e:
        print(f"Error running SFC scan: {e}")
        return False

def run_bcdedit():
    try:
        os.startfile(bcdedit_path)
        print("Successfully opened Bcdedit Optimizer script.")
        return True
    except Exception as e:
        print(f"Error opening Bcdedit Optimizer script: {e}")
        return False

# Close Apps - Spotify, Browser
def close_apps():
    try:
        subprocess.Popen('taskkill /F /IM Spotify.exe', shell=True)
        print("Spotify successfully closed.")
        return True
    except Exception as e:
        print(f"An error occurred while closing Spotify: {e}")
        return False