import threading
import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import sys
import time
from functions import disk_cleanup, prefetch, win_update, ms_store_update, \
    defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, nvidia, drivers_link, bcdedit_optimizer, log_files, windows_optimize

# Define stop_event as a global variable
stop_event = threading.Event()

# Stop all functions
def stop_all_functions():
    stop_event.set()
    print("All functions execution stopped.")

# Start all functions
def run_selected_functions(functions_to_run):
    threads = []
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            thread = threading.Thread(target=func)
            thread.start()
            threads.append(thread)
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Stop all functions when pressing "q"
def on_key(event):
    if event.char.lower() == "q":
        stop_all_functions()

# Styles: Dark Color
def update_colors():
    root.config(bg="#292929")
    label.config(bg=bg_color, fg=fg_color)
    function_buttons_frame.config(bg=bg_color)

    for button_frame in function_buttons_frame.winfo_children():
        button_frame.configure(bg=bg_color)
        for button in button_frame.winfo_children():
            button.configure(bg=bg_color, fg=fg_color)

    all_functions_button.configure(bg=bg_color, fg=fg_color)
    stop_all_functions_button.configure(bg=bg_color, fg=fg_color)

# Global Windows: Title, Window, Font, Icon
root = ctk.CTk()
root.title("KNX")
root.resizable(False, False)
root.option_add("*Font", "Calibri")
root.iconbitmap("Style/logo.ico")

# Style: TOP Text
label = tk.Label(root, text="KNX Cleaner & Updater", font=("Calibri", 13))
label.pack()

# Style: Create function buttons frame
function_buttons_frame = tk.Frame(root)
function_buttons_frame.pack(expand=False, pady=10)

# Functions with Text properties
functions_mapping = {
    "Run Learix FPS Script": learix_fps.learix_fps,
    "Run Disk Cleanup": disk_cleanup.run_disk_cleanup,
    "Run Clean Temp Script": temp.clean_temp,
    "Run Bcdedit Optimizer Script": bcdedit_optimizer.run_bcdedit,
    "Run Log Files Cleaner Script": log_files.run_logfiles,
     "Run Windows Optimize Script": windows_optimize.run_win_optimize,
    "Open Prefetch Folder": prefetch.open_prefetch,
    "Disk Defrag": defrag.defrag,
    "Open Windows Update": win_update.win_update,
    "Open MS Store": ms_store_update.ms_store_update,
    "Open Adobe Creative Cloud": adobe.open_adobe,
    "Open Word": word.open_word,
    "Open TickTick": ticktick.open_ticktick,
    "Open SignalRGB": signalrgb.open_signalrgb,
    "Open Nvidia Experience": nvidia.open_nvidia,
    "Open Web Browser with Links": drivers_link.open_drivers_link,
    "Close Apps (Spotify, Browser)":lambda: (close_apps.close_spotify(), close_apps.close_browser()),
    "Open CCleaner": ccleaner.open_ccleaner,
}

# Style:
for function_name, func in functions_mapping.items():
    button_frame = tk.Frame(function_buttons_frame)
    button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    button = tk.Button(button_frame, text=function_name, command=lambda f=func: run_function(f))
    button.pack(side=tk.LEFT)

    bg_color = "#292929"
    fg_color = "#A9A9A9"
    button.configure(bg=bg_color, fg=fg_color)

# Style: Custom Script Icon
icon_path = "Style/logo.ico"
root.iconbitmap(default=icon_path)

# Bottom buttons
all_functions_button = tk.Button(root, text="Run all", command=lambda: run_selected_functions(functions_mapping.keys()))
all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

stop_all_functions_button = tk.Button(root, text="Stop all", command=stop_all_functions)
stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Bottom, Style: Output Text Widget
output_text = scrolledtext.ScrolledText(root, width=30, height=7, wrap=tk.WORD, bg="#292929", fg="#A9A9A9")
output_text.pack(pady=10)

# Bottom: Function to Output Text
def run_function(func):
    try:
        output_text.insert(tk.END, f"Running function: {func.__name__}\n")
        output_text.insert(tk.END, f"Opened {func.__name__}\n")  # Print message for function opening
        func()
        output_text.insert(tk.END, f"Function {func.__name__} executed successfully.\n\n")
        print("2s Pauza")
        time.sleep(2)
    except Exception as e:
        output_text.insert(tk.END, f"Error running function {func.__name__}: {e}\n\n")
        print(f"Error running function {func.__name__}: {e}")
    finally:
        # AutoScroll to the bottom
        output_text.see(tk.END)

# Class Bottom Output Text - Redirect stdout to the output text widget
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Scroll to the bottom
sys.stdout = StdoutRedirector(output_text)

update_colors()
root.bind("<Key>", on_key)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Quitting... by keyboard interrupt")
    sys.exit()