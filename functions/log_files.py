import os
import time
import pygetwindow as gw

logfiles_path = r'AssetsScripts\Log Files Cleaner.bat'

def run_logfiles():
    try:
        os.startfile(logfiles_path)
        start_time = time.time()
        while True:
            active_window = gw.getWindowsWithTitle(r"C:\WINDOWS\system32\cmd.exe")
            if active_window:
                active_window[0].activate()
                print("Cakame")
                break
            if time.time() - start_time > 30:
                print("Timeout: Window not found.")
                break
            time.sleep(1)
    except Exception as e:
        print("Error running Log Files Cleaner Script:", str(e))
