import threading
import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import sys
import time
# ******************** IMPORT FUNCTIONS ********************
from functions import disk_cleanup, prefetch, win_update, ms_store_update, \
    defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, nvidia, drivers_link, bcdedit_optimizer, log_files, windows_optimize, ipconfig, sfc_scannow, winget

# GUI: Title, Window, Font, Icon
root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.title("KNX Cleaner & Updater")
root.resizable(False,False)
root.option_add("*Font", "Roboto 10",)  # Change font size globally
root.iconbitmap("icon.ico")
label = ctk.CTkLabel(root, text="KNX Cleaner & Updater", font=("Roboto",13, "bold"))
label.pack()
# Define color constants
bg_color = "#292929"
fg_color = "#A9A9A9"
set_color = "#161616"
set_color_hover = "#2F2F2F"
green_color = "#33691E"
red_color = "#441A19"
red_color_hover = "#692827"
# ******************** FUNCTIONS ********************

# Define stop_event as a global variable
stop_event = threading.Event()

# Stop all functions
def stop_all_functions():
    stop_event.set()
    print("All functions execution stopped.")

# Run single function
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

# Run all functions
def run_all_functions(functions_to_run):
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            run_function(func)
            root.update()

# Run selected functions
def run_selected_functions(selected_functions):
    for func_name in selected_functions:
        func = functions_mapping.get(func_name)
        if func:
            run_function(func)
            root.update()
            checkbox_var = checkboxes.get(func_name)
            if checkbox_var:
                checkbox_var.set(False)

# Functions with Text
functions_mapping = {
    "Open Disk Cleanup": disk_cleanup.run_disk_cleanup,
    "Clean Temp": temp.clean_temp,
    "Bcdedit Optimizer": bcdedit_optimizer.run_bcdedit,
    "Clean Log Files": log_files.run_logfiles,
    "Windows Optimize": windows_optimize.run_win_optimize,
    "Flush DNS Cache": ipconfig.flush_dns,
    "Open Prefetch Folder": prefetch.open_prefetch,
    "Open Disk Defragmentation": defrag.defrag,
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

# ******************** GUI ********************
canvas = ctk.CTkCanvas(root, width=220, height=400, highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Functions buttons
function_buttons_frame = ctk.CTkFrame(canvas, bg_color=bg_color)


# Scrollbar functionality
scrollbar = ctk.CTkScrollbar(root, command=canvas.yview,)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Configure canvas and scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=function_buttons_frame, anchor=tk.NW)
# Function to scroll the canvas with the mouse wheel
def on_canvas_mouse_wheel(event):
    canvas.yview_scroll(-1*(event.delta//120), "units")
canvas.bind_all("<MouseWheel>", on_canvas_mouse_wheel)

# Checkboxes for functions buttons
checkboxes = {}
for function_name, func in functions_mapping.items():
    checkbox_var = tk.BooleanVar(value=False)
    checkboxes[function_name] = checkbox_var

    button_frame = ctk.CTkFrame(function_buttons_frame)
    button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=3)

    checkbox = ctk.CTkCheckBox(button_frame, text=function_name, variable=checkbox_var, onvalue=True, offvalue=False, border_width=2, checkbox_width=20, checkbox_height=20, hover_color=fg_color, fg_color=(fg_color, set_color), font=("Roboto", 14,))
    checkbox.pack(side=tk.LEFT)

# Update the canvas scroll region after adding widgets
function_buttons_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Run all, stop all, run selected buttons
run_selected_functions_button = ctk.CTkButton(root, text="Run Selected", command=lambda: run_selected_functions([func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]), fg_color=set_color, hover_color=set_color_hover)
run_selected_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

all_functions_button = ctk.CTkButton(root, text="Run All", command=lambda: run_all_functions(functions_mapping.keys()), fg_color=set_color, hover_color=set_color_hover)
all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

stop_all_functions_button = ctk.CTkButton(root, text="Stop All", command=stop_all_functions, fg_color=red_color, hover_color=red_color_hover)
stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Bottom, Style: Output Text Widget
output_text = ctk.CTkTextbox(root, width=250, height=200, wrap=tk.WORD)
output_text.pack(pady=10)

# ******************** RUN ********************
# Output Text - Redirect stdout to the output text widget
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Scroll to the bottom
sys.stdout = StdoutRedirector(output_text)
print("Console:")

try:
  root.mainloop()
except KeyboardInterrupt:
    print("Quitting... by keyboard interrupt")
    sys.exit()