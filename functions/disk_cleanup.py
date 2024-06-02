import subprocess
import time
import pyautogui

def run_disk_cleanup():
    try:
        subprocess.Popen('cleanmgr.exe')
        time.sleep(1)  # Počkajte, kým sa okno otvorí
        pyautogui.press('enter')
        print("Disk Cleanup Tool successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Disk Cleanup Tool: {e}")
        return False
