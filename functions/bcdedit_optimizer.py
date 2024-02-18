import os
import time
import pyautogui
import pygetwindow as gw

bcdedit_path = r'AssetsScripts\Bcdedit Optimizer.cmd'

def run_bcdedit():
    try:
        os.startfile(bcdedit_path)
        time.sleep(6)

        # Získanie zoznamu všetkých okien
        all_windows = gw.getAllWindows()

        # Hľadanie okna s názvom "C:\WINDOWS\system32\cmd.exe"
        active_window = None
        for window in all_windows:
            if "C:\WINDOWS\system32\cmd.exe" in window.title:
                active_window = window
                break

        if active_window is not None:
            active_window.activate()
            pyautogui.press('enter')
            print("Cakame")
        else:
            print("Window not found.")
    except Exception as e:
        print("Error running Bcdedit Optimizer Script:", str(e))