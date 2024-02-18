import os
import time
import pygetwindow as gw

win_optimize_path = r'AssetsScripts\Windows Optimization.bat'

def run_win_optimize():
        try:
            os.startfile(win_optimize_path)
            start_time = time.time()
            while True:
                active_window = gw.getWindowsWithTitle("Administrator:  [Windows Optimization by Saerro]")[0]
                if active_window:
                    active_window[0].activate()
                    print("Cakame")
                    break
                if time.time() - start_time > 30:
                    print("Timeout: Window not found.")
                    break
                time.sleep(1)
        except Exception as e:
            print("Error running Windows Optimize Script:", str(e))
