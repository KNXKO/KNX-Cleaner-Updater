import os
import subprocess
import time
import pyautogui
import pygetwindow as gw
import webbrowser
import ctypes
import psutil
import tkinter as tk
from tkinter import messagebox
from functools import partial


class DiskCleaner:
    def __init__(self):
        self.Prefetch_path = r'C:\Windows\Prefetch'
        self.Temp_path = r'AssetsScripts\SPEEDUP.BAT'
        self.Learix_path = r'AssetsScripts\Learix FPS.bat'
        self.Adobe_path = r'AssetsScripts\Adobe Creative Cloud.lnk'
        self.Word_path = r'AssetsScripts\Word.lnk'
        self.TickTick_path = r'AssetsScripts\TickTick.lnk'
        self.Signalrgb_path = r'AssetsScripts\SignalRgb.lnk'
        self.Nvidia_path = r'AssetsScripts\GeForce Experience.lnk'
        self.Ccleaner_path = r'AssetsScripts\GeForce Experience.lnk'

    # Prefetch folder
    def open_prefetch_folder(self):
        try:
            os.startfile(self.Prefetch_path)
            print("Opened Prefetch Folder")
        except Exception as e:
            print("Error opening Prefetch Folder:", str(e))

    # Čistenie disku
    def run_disk_cleanup_tool(self):
        try:
            subprocess.Popen('cleanmgr.exe')
            print("Running Disk Cleanup Tool")
            time.sleep(5)  # Čakanie na zobrazenie okna nástroja na čistenie disku
            pyautogui.press('enter')
            print("Opened Clean Disk Tool")
        except Exception as e:
            print("Error running Disk Cleanup Tool:", str(e))

    # Windows update
    def open_windows_settings_update_section(self):
        try:
            os.system("start ms-settings:windowsupdate")
            print("Opened Windows Update")
        except Exception as e:
            print("Error opening Windows Update:", str(e))

    # Microsoft store
    def open_microsoft_store_update_section(self):
        try:
            os.system("start ms-windows-store:home")
            print("Opened Microsoft Store")
        except Exception as e:
            print("Error opening Microsoft Store:", str(e))

    # Defragmentácia
    def open_disk_defragmenter(self):
        try:
            subprocess.Popen('dfrgui.exe')
            print("Opened Disk Defragmenter")
        except Exception as e:
            print("Error opening Disk Defragmenter:", str(e))

    # Open Clean Temp Skript
    def run_clean_temp(self):
        try:
            os.startfile(self.Temp_path)
            print("Cleaned Temp Folder")
        except Exception as e:
            print("Error running Clean Temp Script:", str(e))

    # Open Learix FPS Script
    def run_learix_fps(self):
        try:
            os.startfile(self.Learix_path)
            time.sleep(5)
            active_window = gw.getWindowsWithTitle("Administrator:  Learix FPS 2.0")[0]
            pyautogui.press('1')
            pyautogui.press('enter')
            if active_window is not None:
                for i in range(1, 7):
                    active_window.activate()
                    pyautogui.press(str(i))
                    pyautogui.press('enter')
                    time.sleep(5)
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

    # Open Adobe Creative Cloud
    def open_adobe(self):
        try:
            os.startfile(self.Adobe_path)
            print("Opened Adobe Creative Cloud")
        except Exception as e:
            print("Error opening Adobe Creative Cloud:", str(e))

    # Open Word
    def open_word(self):
        try:
            os.startfile(self.Word_path)
            print("Opened Word")
        except Exception as e:
            print("Error opening Word:", str(e))

    # Open TickTick
    def open_ticktick(self):
        try:
            os.startfile(self.TickTick_path)
            print("Opened TickTick")
        except Exception as e:
            print("Error opening TickTick:", str(e))

    # Open SignalRGB
    def open_signalrgb(self):
        try:
            os.startfile(self.Signalrgb_path)
            print("Opened SignalRGB")
        except Exception as e:
            print("Error opening SignalRGB:", str(e))

    # Open Nvidia Experience
    def open_nvidia(self):
        try:
            os.startfile(self.Nvidia_path)
            print("Opened Nvidia Experience")
        except Exception as e:
            print("Error opening Nvidia Experience:", str(e))

    # Open CCleaner
    def open_ccleaner(self):
        try:
            os.startfile(self.Ccleaner_path)
            print("Opened CCleaner")
        except Exception as e:
            print("Error opening CCleaner:", str(e))

    # Open web browser with links
    def open_drivers_link(self):
        try:
            webbrowser.open('https://rog.asus.com/motherboards/rog-strix/rog-strix-b550-f-gaming-model/helpdesk_download/')
            webbrowser.open_new_tab('https://www.amd.com/en/support/chipsets/amd-socket-am4/b550')
            print("Opened web browser with links")
        except Exception as e:
            print("Error opening web browser with links:", str(e))

    # Close spotify
    def close_spotify(self):
        try:
            for proc in psutil.process_iter():
                if "spotify" in proc.name().lower():
                    proc.kill()
                    print("Spotify closed successfully.")
                    break
            else:
                print("Spotify is not running.")
        except Exception as e:
            print("An error occurred while closing Spotify:", str(e))

    # Close browser
    def close_browser(self):
        try:
            subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
            print("Browser closed successfully.")
        except Exception as e:
            print("An error occurred while closing the browser:", str(e))

    def run_all_functions(self):
        functions = [
            self.run_learix_fps,
            self.run_clean_temp,
            self.run_disk_cleanup_tool,
            self.open_disk_defragmenter,
            self.open_prefetch_folder,
            self.open_windows_settings_update_section,
            self.open_microsoft_store_update_section,
            self.open_adobe,
            self.open_word,
            self.open_ticktick,
            self.open_signalrgb,
            self.open_nvidia,
            self.open_drivers_link,
            self.close_spotify,
            self.close_browser,
            self.open_ccleaner
        ]

        for func in functions:
            func()

        print("All functions executed successfully.")

        # Create a messagebox
        ctypes.windll.user32.MessageBoxW(0, "All functions executed successfully.", "Success", 0)

        # Alternatively, for error handling:
        # ctypes.windll.user32.MessageBoxW(0, "An error occurred during function execution.", "Error", 0)

def run_selected_functions(functions_to_run):
    disk_cleaner = DiskCleaner()
    for func_name in functions_to_run:
        func = getattr(disk_cleaner, func_name)
        func()

def run_all_functions():
    disk_cleaner = DiskCleaner()
    disk_cleaner.run_all_functions()


def main():
    root = tk.Tk()
    root.title("Disk Cleaner")

    # Dark mode colors
    dark_mode_bg = "#292929"
    dark_mode_bc = "#1e1e1e"
    dark_mode_fg = "#e5e5e5"

    # Light mode colors
    light_mode_bg = "#FFFFFF"
    light_mode_bc = "#e5e5e5"
    light_mode_fg = "#000000"

    dark_mode = True

    def toggle_dark_mode():
        nonlocal dark_mode
        dark_mode = not dark_mode
        update_colors()

    def update_colors():
        bg_color = dark_mode_bg if dark_mode else light_mode_bg
        fg_color = dark_mode_fg if dark_mode else light_mode_fg
        root.config(bg=bg_color)
        label.config(bg=bg_color, fg=fg_color)
        function_buttons_frame.config(bg=bg_color)
        for button in function_buttons_frame.winfo_children():
            button.config(bg=bg_color)  # Zmeníme farbu pozadia tlačidiel



    toggle_dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
    toggle_dark_mode_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    label = tk.Label(root, text="Select the action you want to perform:")
    label.pack()

    disk_cleaner = DiskCleaner()

    def run_function(func):
        try:
            func()
        except Exception as e:
            print(f"Error running function: {e}")

    function_buttons_frame = tk.Frame(root)
    function_buttons_frame.pack(expand=True, pady=10)

    functions = [
        ("Open Prefetch Folder", disk_cleaner.open_prefetch_folder),
        ("Run Disk Cleanup Tool", disk_cleaner.run_disk_cleanup_tool),
        ("Open Windows Update", disk_cleaner.open_windows_settings_update_section),
        ("Open Microsoft Store", disk_cleaner.open_microsoft_store_update_section),
        ("Open Disk Defragmenter", disk_cleaner.open_disk_defragmenter),
        ("Run Clean Temp Script", disk_cleaner.run_clean_temp),
        ("Run Learix FPS Script", disk_cleaner.run_learix_fps),
        ("Open Adobe Creative Cloud", disk_cleaner.open_adobe),
        ("Open Word", disk_cleaner.open_word),
        ("Open TickTick", disk_cleaner.open_ticktick),
        ("Open SignalRGB", disk_cleaner.open_signalrgb),
        ("Open Nvidia Experience", disk_cleaner.open_nvidia),
        ("Open CCleaner", disk_cleaner.open_ccleaner),
        ("Open Web Browser with Links", disk_cleaner.open_drivers_link),
        ("Close Spotify", disk_cleaner.close_spotify),
        ("Close Browser", disk_cleaner.close_browser)
    ]

    for function_name, func in functions:
        button_frame = tk.Frame(function_buttons_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

        button = tk.Button(button_frame, text=function_name, command=partial(run_function, func))
        button.pack(side=tk.LEFT)


    all_functions_button = tk.Button(root, text="Run all", command=disk_cleaner.run_all_functions)
    all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    update_colors()  # Initialize with dark mode colors

    root.mainloop()

if __name__ == "__main__":
    main()