import os
import pyautogui
import time
import pygetwindow as gw

cmd_path = r'AssetsScripts\cmd.lnk'

def run_sfc():
    try:
        os.startfile(cmd_path)
        print("CMD successfully opened.")
        time.sleep(2)

        active_window = gw.getWindowsWithTitle("Administrator: cmd")
        if not active_window:  # Ak sme nenájdu okno
            print("Command Prompt window not found.")
            return False

        active_window = active_window[0]
        active_window.activate()

        pyautogui.write('sfc /scannow')
        pyautogui.press('enter')
        print("SFC scan successfully initiated.")
        return True
    except Exception as e:
        print(f"Error opening CMD or running sfc /scannow: {e}")
        return False