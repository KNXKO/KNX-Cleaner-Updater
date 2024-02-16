import subprocess
import time
import pyautogui

def run_disk_cleanup():
        try:
            subprocess.Popen('cleanmgr.exe')
            time.sleep(1)  # Čakanie na zobrazenie okna nástroja na čistenie disku
            pyautogui.press('enter')
            print("Running Disk Cleanup Tool")
            print("Completed Clean Disk Tool")
        except Exception as e:
            print("Error running Disk Cleanup Tool:", str(e))