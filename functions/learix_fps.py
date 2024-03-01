import pyautogui
import os
import time
import pygetwindow as gw

learix_path = r'AssetsScripts\Learix FPS.bat'

def learix_fps():
        try:
            os.startfile(learix_path)
            time.sleep(3)
            active_window = gw.getWindowsWithTitle("Administrator:  Learix FPS 2.0")[0]
            pyautogui.press('1')
            pyautogui.press('enter')
            if active_window is not None:
                for i in range(1, 7):
                    active_window.activate()
                    pyautogui.press(str(i))
                    pyautogui.press('enter')
                    time.sleep(8)
                    print(str(i) + " - Done")
                active_window.activate()
                pyautogui.press('x')
                pyautogui.press('enter')
                pyautogui.press('x')
                pyautogui.press('enter')
                print("Learix FPS Script Done")
            else:
                print("Window not found.")
        except Exception as e:
            print("Error running Learix FPS Script:", str(e))
