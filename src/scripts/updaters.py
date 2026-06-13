import os
import pyautogui
import time
import pygetwindow as gw
import webbrowser

def run_winget():
    cmd_path = r'src\shortcuts\cmd.lnk'
    try:
        os.startfile(cmd_path)
        print("CMD opened.")
        time.sleep(2)
        active_window = gw.getWindowsWithTitle("Administrator: cmd")
        if not active_window:
            print("CMD window not found.")
            return False

        active_window = active_window[0]
        active_window.activate()

        pyautogui.write('winget upgrade')
        pyautogui.press('enter')
        time.sleep(8)

        pyautogui.write('winget upgrade --all')
        pyautogui.press('enter')
        print("Winget commands executed successfully.")
        return True
    except Exception as e:
        print(f"Error opening CMD or running winget commands: {e}")
        return False

def open_drivers_link():
    link1 = 'https://rog.asus.com/motherboards/rog-strix/rog-strix-b550-f-gaming-model/helpdesk_download/'
    link2 = 'https://www.amd.com/en/support/chipsets/amd-socket-am4/b550'
    try:
        webbrowser.open(link1)
        webbrowser.open_new_tab(link2)
        print("Web browser successfully opened with links.")
        return True
    except Exception as e:
        print(f"Error opening web browser with links: {e}")
        return False
