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

def reset_network():
    try:
        subprocess.run(['netsh', 'winsock', 'reset'], capture_output=True)
        print("Winsock reset done.")
        subprocess.run(
            ['netsh', 'int', 'ip', 'reset', r'C:\Windows\Temp\ip_reset.log'],
            capture_output=True
        )
        print("IP stack reset done.")
        subprocess.run(['ipconfig', '/release'], capture_output=True)
        subprocess.run(['ipconfig', '/renew'], capture_output=True)
        subprocess.run(['ipconfig', '/flushdns'], capture_output=True)
        print("Network stack reset successfully. Restart recommended to fully apply changes.")
        return True
    except Exception as e:
        print(f"Error resetting network: {e}")
        return False

def optimize_drives():
    try:
        print("Running SSD Trim on all drives... (this may take a moment)")
        process = subprocess.Popen(
            ['defrag', '/C', '/U', '/L'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',
            errors='replace'
        )
        for line in process.stdout:
            stripped = line.strip()
            if stripped:
                print(stripped)
        process.wait()
        if process.returncode == 0:
            print("Drive optimization completed.")
        else:
            print(f"Drive optimization finished with code {process.returncode}.")
        return process.returncode == 0
    except Exception as e:
        print(f"Error optimizing drives: {e}")
        return False

def set_high_performance():
    HIGH_PERF_GUID = '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'
    try:
        subprocess.run(['powercfg', '/setactive', HIGH_PERF_GUID], check=True)
        print("Power plan set to High Performance.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set power plan: {e}")
        return False

def run_dism():
    try:
        print("Running DISM RestoreHealth... (this may take 10-20 minutes)")
        process = subprocess.Popen(
            ['dism', '/Online', '/Cleanup-Image', '/RestoreHealth'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',
            errors='replace'
        )
        for line in process.stdout:
            stripped = line.strip()
            if stripped:
                print(stripped)
        process.wait()
        if process.returncode == 0:
            print("DISM RestoreHealth completed successfully.")
        else:
            print(f"DISM finished with code {process.returncode}. Check CBS.log for details.")
        return process.returncode == 0
    except Exception as e:
        print(f"Error running DISM: {e}")
        return False