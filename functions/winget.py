import os
import pyautogui
import time
import pygetwindow as gw

cmd_path = r'AssetsScripts\cmd.lnk'

def run_winget():
    try:
        os.startfile(cmd_path)
        print("CMD otvorené")
        time.sleep(2)
        active_window = gw.getWindowsWithTitle("Administrator: cmd")
        if not active_window:  # Ak sme nenájdu okno
            print("Okno príkazového riadku nebolo nájdené.")
            return False

        active_window = active_window[0]
        active_window.activate()

        pyautogui.write('winget upgrade')
        pyautogui.press('enter')
        time.sleep(8)  # Počkaj na vykonanie príkazu

        pyautogui.write('winget update --all')
        pyautogui.press('enter')
        print("Prikazy winget boli úspešne spustené.")
        return True
    except Exception as e:
        print(f"Chyba pri otváraní CMD alebo spúšťaní príkazov winget: {e}")
        return False
