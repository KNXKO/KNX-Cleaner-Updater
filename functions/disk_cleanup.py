import subprocess
import time
import pyautogui

def run_disk_cleanup():
        try:
            subprocess.Popen('cleanmgr.exe')
            time.sleep(1) # Wait for the window to open
            pyautogui.press('enter')
            print("Opened Disk Cleanup Tool")
        except Exception as e:
            print("Error opening Disk Cleanup Tool:", str(e))