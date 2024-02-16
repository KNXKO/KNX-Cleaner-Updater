import threading
import pygetwindow as gw
import ctypes
import tkinter as tk
from tkinter import messagebox
from functools import partial

# FUNCTIONS
from functions import open_prefetch
from functions import run_disk_cleanup
from functions import windows_update
from functions import ms_store_update
from functions import defrag
from functions import temp
from functions import learix_fps
from functions import adobe
from functions import word
from functions import ticktick
from functions import signalrgb
from functions import ccleaner
from functions import close_apps
from functions import nvidia
from functions import drivers_link

class DiskCleaner:
    def __init__(self):
        self.running = False
        self.stop_event = threading.Event()

    # Stop all functions
    def stop_all_functions(self):
        self.stop_event.set()
        print("All functions execution stopped.")

    # Prefetch folder
    def open_prefetch(self):
        open_prefetch.open_prefetch()

    # Čistenie disku
    def run_disk_cleanup_tool(self):
        run_disk_cleanup.run_disk_cleanup_tool()

    # Windows update
    def windows_update(self):
         windows_update.windows_update()

    # Microsoft store
    def ms_store_update(self):
        ms_store_update.ms_store_update()

    # Defrag
    def defrag(self):
        defrag.defrag()

    # Open Clean Temp Script
    def clean_temp(self):
        temp.clean_temp()

    # Open Learix FPS Script
    def learix_fps(self):
       learix_fps.learix_fps()

    # Open Adobe Creative Cloud
    def open_adobe(self):
        adobe.open_adobe()

    # Open Word
    def open_word(self):
        word.open_word()

    # Open TickTick
    def open_ticktick(self):
        ticktick.open_ticktick()

    # Open SignalRGB
    def open_signalrgb(self):
        signalrgb.open_signalrgb()

    # Open Nvidia Experience
    def open_nvidia(self):
        nvidia.open_nvidia()

    # Open CCleaner
    def open_ccleaner(self):
        ccleaner.open_ccleaner()

    # Open web browser with links
    def open_drivers_link(self):
        drivers_link.open_drivers_link()

    # Close spotify
    def close_apps(self):
        close_apps.close_spotify()
        close_apps.close_browser()

    def run_all_functions(self):
        functions = [
            self.learix_fps,
            self.clean_temp,
            self.run_disk_cleanup_tool,
            self.open_prefetch,
            self.defrag,
            self.windows_update,
            self.ms_store_update,
            self.open_adobe,
            self.open_word,
            self.open_ticktick,
            self.open_signalrgb,
            self.open_nvidia,
            self.open_drivers_link,
            self.close_apps,
            self.open_ccleaner
        ]
        for func in functions:
            func()
        print("All functions executed successfully.")
        # Create a messagebox
        ctypes.windll.user32.MessageBoxW(0, "All functions executed successfully.", "Success", 0)

def run_selected_functions(functions_to_run):
    disk_cleaner = DiskCleaner()
    for func_name in functions_to_run:
        func = getattr(disk_cleaner, func_name)
        func()


def main():
    root = tk.Tk()
    # Title
    root.title("KNX")
    dark_mode = True
    root.resizable(False, False)
    disk_cleaner = DiskCleaner()

    # Close the app with the "q" key
    def on_key(event):
        if event.char.lower() == "q":
            disk_cleaner.stop_all_functions()

    root.bind("<Key>", on_key)

    # Dark mode colors
    dark_mode_bg = "#292929"
    dark_mode_fg = "#e5e5e5"

    # Light mode colors
    light_mode_bg = "#e5e5e5"
    light_mode_fg = "#000000"

    def toggle_dark_mode():
        nonlocal dark_mode
        dark_mode = not dark_mode
        update_colors()

    def update_colors():
        bg_color = dark_mode_bg if dark_mode else light_mode_bg
        fg_color = dark_mode_fg if dark_mode else light_mode_fg
        root.config(bg=bg_color)
        #TEXT
        label.config(bg=bg_color, fg=fg_color)
        #POZADIE OKOLO BUTTONS
        function_buttons_frame.config(bg=bg_color)

        for button in function_buttons_frame.winfo_children():
            button.configure(bg=bg_color)  # Nastavíme background color tlačidiel


    toggle_dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
    toggle_dark_mode_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    label = tk.Label(root, text="Select the action you want to perform:")
    label.pack()

    def run_function(func):
        try:
            func()
        except Exception as e:
            print(f"Error running function: {e}")

    function_buttons_frame = tk.Frame(root)
    function_buttons_frame.pack(expand=False, pady=10)

    functions = [
        ("Run Learix FPS Script", disk_cleaner.learix_fps),
        ("Run Disk Cleanup", disk_cleaner.run_disk_cleanup_tool),
        ("Run Clean Temp Script", disk_cleaner.clean_temp),
        ("Open Prefetch Folder", disk_cleaner.open_prefetch),
        ("Disk Defrag", disk_cleaner.defrag),
        ("Open Windows Update", disk_cleaner.windows_update),
        ("Open MS Store", disk_cleaner.ms_store_update),
        ("Open Adobe Creative Cloud", disk_cleaner.open_adobe),
        ("Open Word", disk_cleaner.open_word),
        ("Open TickTick", disk_cleaner.open_ticktick),
        ("Open SignalRGB", disk_cleaner.open_signalrgb),
        ("Open Nvidia Experience", disk_cleaner.open_nvidia),
        ("Open Web Browser with Links", disk_cleaner.open_drivers_link),
        ("Close Apps (Spotify, Browser)", disk_cleaner.close_apps),
        ("Open CCleaner", disk_cleaner.open_ccleaner),
    ]

    for function_name, func in functions:
        button_frame = tk.Frame(function_buttons_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

        button = tk.Button(button_frame, text=function_name, command=partial(run_function, func))
        button.pack(side=tk.LEFT)


    all_functions_button = tk.Button(root, text="Run all", command=disk_cleaner.run_all_functions)
    all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    stop_all_functions_button = tk.Button(root, text="Stop all", command=disk_cleaner.stop_all_functions)
    stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    update_colors()
    root.mainloop()
    
if __name__ == "__main__":
    main()