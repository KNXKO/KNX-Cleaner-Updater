import subprocess
import time
import pyautogui

def run_disk_cleanup():
        try:
            subprocess.Popen('cleanmgr.exe')
            time.sleep(1) # Wait for the window to open
            pyautogui.press('enter')
            print("Running Disk Cleanup Tool")
            print("Completed Clean Disk Tool")
        except Exception as e:
            print("Error running Disk Cleanup Tool:", str(e))