import pyautogui
import os
import time
import pygetwindow as gw

learix_path = r'AssetsScripts\Learix FPS.bat'

def learix_fps():
    try:
        os.startfile(learix_path)
        # Čakanie na zobrazenie okna s názvom "Administrator:  Learix FPS 2.0" do 5 sekúnd
        timeout = time.time() + 5  # Nastavenie maximálneho času čakania na 5 sekúnd
        time.sleep(3)
        while True:
            active_window = gw.getWindowsWithTitle("Administrator:  Learix FPS 2.0")
            if active_window:  # Ak sme našli okno
                active_window = active_window[0]
                break
            if time.time() > timeout:  # Ak prekročíme maximálny čas čakania
                raise TimeoutError("Timeout: Window not found.")
            time.sleep(1)  # Počkáme sekundu a skúsim to znova

        # Aktivácia okna
        active_window.activate()
        pyautogui.press('1')
        pyautogui.press('enter')

        # Cyklus pre stlačenie ďalších klávesov a Enter
        for i in range(1, 7):
            active_window.activate()
            pyautogui.press(str(i))
            pyautogui.press('enter')
            time.sleep(8)
            print(str(i) + " - Done")

        active_window.activate()
        for _ in range(2):
            pyautogui.press('x')
            pyautogui.press('enter')

        print("Learix FPS Script successfully executed.")
        return True
    except Exception as e:
        print(f"Error running Learix FPS Script: {e}")
        return False
