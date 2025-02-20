import os
import subprocess
import time
import pyautogui
import pygetwindow as gw

learix_path = r'src\shortcuts\Learix FPS.bat'
logfiles_path = r'src\shortcuts\Log Files Cleaner.bat'
temp_path = r'src\shortcuts\SPEEDUP.BAT'

def run_logfiles():
    try:
        os.startfile(logfiles_path)
        print("Log folder successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Log Files Cleaner Script: {e}")
        return False

def clean_prefetch():
    try:
        os.startfile(r'C:\Windows\Prefetch')
        print("Opening Prefetch folder...")

        timeout = time.time() + 5
        prefetch_window = None
        while time.time() < timeout:
            windows = gw.getWindowsWithTitle('Prefetch')
            if windows:
                prefetch_window = windows[0]
                break
            time.sleep(0.5)

        if not prefetch_window:
            raise TimeoutError("Prefetch window did not open in time")

        prefetch_window.activate()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.press('delete')
        time.sleep(0.5)

        try:
            pyautogui.press('enter')
        except:
            pass

        prefetch_window.close()

        print("Prefetch files successfully deleted.")
        return True

    except Exception as e:
        print(f"Error cleaning Prefetch folder: {e}")
        return False

def clean_temp():
    try:
        os.startfile(temp_path)
        print("Temp folder successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Clean Temp Script: {e}")
        return False

def defrag_disk():
    try:
        subprocess.Popen('dfrgui.exe')
        print("Disk Defragmenter successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Disk Defragmenter: {e}")
        return False

def disk_cleanup():
    try:
        subprocess.Popen('cleanmgr.exe')
        time.sleep(1)
        pyautogui.press('enter')
        print("Disk Cleanup Tool successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Disk Cleanup Tool: {e}")
        return False

def learix_fps():
    try:
        os.startfile(learix_path)
        timeout = time.time() + 5
        time.sleep(3)
        while True:
            active_window = gw.getWindowsWithTitle("Administrator:  Learix FPS 2.0")
            if active_window:  # Ak sme našli okno
                active_window = active_window[0]
                break
            if time.time() > timeout:
                raise TimeoutError("Timeout: Window not found.")
            time.sleep(1)
        print("Learix FPS Script successfully opened.")
        active_window.activate()
        pyautogui.press('1')
        pyautogui.press('enter')

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

def flush_dns():
    try:
        result = subprocess.run("cmd /c ipconfig /flushdns", shell=True, check=True)
        print("DNS cache successfully flushed.")
        return True
    except subprocess.CalledProcessError:
        print("Failed to flush the DNS cache.")
        return False