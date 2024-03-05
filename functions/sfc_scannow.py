import os
import pyautogui
import time
import pygetwindow as gw

cmd_path = r'AssetsScripts\cmd.lnk'

def run_sfc_scan():
    try:
        os.startfile(cmd_path)
        print("Otvorený CMD")
        time.sleep(2)
        while True:
            active_window = gw.getWindowsWithTitle("Administrator: cmd")
            if active_window:  # Ak sme našli okno
                active_window = active_window[0]
                break
            if not active_window:
                print("Okno príkazového riadku nebolo nájdené.")
                return
        active_window.activate()
        pyautogui.write('sfc /scannow')
        pyautogui.press('enter')
        print("SFC skenovanie bolo úspešne spustené.")
    except Exception as e:
        print("Chyba pri otváraní CMD alebo spúšťaní sfc /scannow:", str(e))