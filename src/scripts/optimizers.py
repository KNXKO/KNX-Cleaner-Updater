import os
import pygetwindow as gw
import subprocess

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
        subprocess.run(['runas', '/user:Administrator', 'sfc', '/scannow'],
                      capture_output=True,
                      text=True)
        print("SFC scan initiated. Please wait...")
        return True
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

    '''
    try:
        subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
        print("Browser successfully closed.")
        return True
    except Exception as e:
        print(f"An error occurred while closing the browser: {e}")
        return False
    '''