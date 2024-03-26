import threading
import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import sys
import time
from functions import disk_cleanup, prefetch, win_update, ms_store_update, \
    defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, nvidia, drivers_link, bcdedit_optimizer, log_files, windows_optimize, ipconfig, sfc_scannow, winget

# Global Windows: Title, Window, Font, Icon
root = ctk.CTk()
root.title("KNX")
root.resizable(False, True)
root.option_add("*Font", "Calibri")
root.iconbitmap("icon.ico")
# Style: TOP Text
label = tk.Label(root, text="KNX Cleaner & Updater", font=("Calibri", 13))
bg_color = "#292929"
fg_color = "#A9A9A9"
label.pack()

# Define stop_event as a global variable
stop_event = threading.Event()

# Stop all functions
def stop_all_functions():
    stop_event.set()
    print("All functions execution stopped.")

# Function to display the output of the functions in the output text widget
def run_function(func):
    try:
        func()  # Call the function directly without extra output
        root.update()  # Update the GUI to keep it responsive
        print(f"Function {func.__name__} Completed!")
    except Exception as e:
        print(f"Error running function {func.__name__}: {e}")
    finally:
        if not stop_event.is_set():  # Add condition to check if the function was stopped
            print("Pause 0.5s...")
            time.sleep(0.5)  # 0.5 second pause
        output_text.see(tk.END)

# Start all functions sequentially with a pause between each
def run_all_functions(functions_to_run):
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            run_function(func)
            root.update()

# Button to run only selected functions
def run_selected_functions(selected_functions):
    for func_name in selected_functions:
        func = functions_mapping.get(func_name)
        if func:
            run_function(func)
            root.update()  # Update the GUI to keep it responsive

def update_colors():
    root.config(bg=bg_color)
    label.config(bg=bg_color, fg=fg_color)
    function_buttons_frame.config(bg=bg_color)

    for button_frame in function_buttons_frame.winfo_children():
        button_frame.configure(bg=bg_color)
        for button in button_frame.winfo_children():
            button.configure(bg=bg_color, fg=fg_color)

    all_functions_button.configure(bg=bg_color, fg=fg_color)
    stop_all_functions_button.configure(bg=bg_color, fg=fg_color)

# Create canvas with background color
canvas = tk.Canvas(root, bg=bg_color, width=250, height=400, highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create function buttons frame
function_buttons_frame = tk.Frame(canvas, bg=bg_color)

# Add a scrollbar to the canvas
scrollbar = ctk.CTkScrollbar(root, command=canvas.yview,)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas and scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=function_buttons_frame, anchor=tk.NW)

# Function to scroll the canvas with the mouse wheel
def on_canvas_mouse_wheel(event):
    canvas.yview_scroll(-1*(event.delta//120), "units")
canvas.bind_all("<MouseWheel>", on_canvas_mouse_wheel)

# Functions with Text properties
functions_mapping = {
    "Run Disk Cleanup": disk_cleanup.run_disk_cleanup,
    "Run Clean Temp Script": temp.clean_temp,
    "Run Bcdedit Optimizer Script": bcdedit_optimizer.run_bcdedit,
    "Run Log Files Cleaner Script": log_files.run_logfiles,
    "Run Windows Optimize Script": windows_optimize.run_win_optimize,
    "Flush DNS": ipconfig.flush_dns,
    "Open Prefetch Folder": prefetch.open_prefetch,
    "Disk Defrag": defrag.defrag,
    "Open Windows Update": win_update.win_update,
    "Open MS Store": ms_store_update.ms_store_update,
    "Open Adobe Creative Cloud": adobe.open_adobe,
    "Open Word": word.open_word,
    "Open TickTick": ticktick.open_ticktick,
    "Open SignalRGB": signalrgb.open_signalrgb,
    "Open Nvidia App": nvidia.open_nvidia,
    "Open Web Browser with Links": drivers_link.open_drivers_link,
    "Close Apps (Spotify)": close_apps.close_apps,
    "Open CCleaner": ccleaner.open_ccleaner,
}

# Style:
checkboxes = {}
for function_name, func in functions_mapping.items():
    checkbox_var = tk.BooleanVar(value=False)
    checkboxes[function_name] = checkbox_var

    button_frame = tk.Frame(function_buttons_frame)
    button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    checkbox = tk.Checkbutton(button_frame, text=function_name, variable=checkbox_var, onvalue=True, offvalue=False)
    checkbox.pack(side=tk.LEFT)

    checkbox.configure(bg=bg_color, fg=fg_color)

# Update the canvas scroll region after adding widgets
function_buttons_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Bottom buttons
all_functions_button = tk.Button(root, text="Run all", command=lambda: run_all_functions(functions_mapping.keys()))
all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

stop_all_functions_button = tk.Button(root, text="Stop all", command=stop_all_functions)
stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

run_selected_functions_button = tk.Button(root, text="Run Selected Functions", command=lambda: run_selected_functions([func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]))
run_selected_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Bottom, Style: Output Text Widget
output_text = scrolledtext.ScrolledText(root, width=30, height=7, wrap=tk.WORD, bg=bg_color, fg=fg_color)
output_text.pack(pady=10)

# Class Bottom Output Text - Redirect stdout to the output text widget
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Scroll to the bottom
sys.stdout = StdoutRedirector(output_text)

try:
  update_colors()
  root.mainloop()
except KeyboardInterrupt:
    print("Quitting... by keyboard interrupt")
    sys.exit()