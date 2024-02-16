# Library
import threading
import threading
import tkinter as tk
from functools import partial
# Import functions
from functions import disk_cleanup, prefetch, win_update, ms_store_update, \
    defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, \
    nvidia, drivers_link

# Define stop_event as a global variable
stop_event = threading.Event()

# Stop all functions
def stop_all_functions():
    stop_event.set()
    print("All functions execution stopped.")

# Start all functions
def run_selected_functions(functions_to_run):
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            func()

# Stop all functions when pressing "q"
def on_key(event):
    if event.char.lower() == "q":
        stop_all_functions()

# Run spec function
def run_function(func):
    try:
        func()
    except Exception as e:
        print(f"Error running function: {e}")

# Styles
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

root = tk.Tk()
root.title("KNX")
root.resizable(False, False)
root.option_add("*Font", "Calibri")
# TOP Text
label = tk.Label(root, text="KNX Cleaner & Updater", font=("Calibri", 13))
label.pack()

# Style: Create function buttons frame
function_buttons_frame = tk.Frame(root)
function_buttons_frame.pack(expand=False, pady=10)

# Function buttons
functions_mapping = {
    "Run Learix FPS Script": learix_fps.learix_fps,
    "Run Disk Cleanup": disk_cleanup.run_disk_cleanup,
    "Run Clean Temp Script": temp.clean_temp,
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

    button = tk.Button(button_frame, text=function_name, command=partial(run_function, func))
    button.pack(side=tk.LEFT)

    bg_color = "#292929"
    fg_color = "#A9A9A9"
    button.configure(bg=bg_color, fg=fg_color)

# Bottom buttons
all_functions_button = tk.Button(root, text="Run all", command=partial(run_selected_functions, functions_mapping.keys()))
all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

stop_all_functions_button = tk.Button(root, text="Stop all", command=stop_all_functions)
stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

update_colors()
root.bind("<Key>", on_key)
root.mainloop()