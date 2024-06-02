import threading
import tkinter as tk
import customtkinter as ctk
import time
# ******************** IMPORT FUNCTIONS ********************
from functions import disk_cleanup, prefetch, win_update, ms_store_update, \
    defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, nvidia, drivers_link, bcdedit_optimizer, log_files, windows_optimize, ipconfig

# GUI: Title, Window, Font, Icon
root = ctk.CTk()
root.geometry("550x500")
ctk.set_appearance_mode("dark")
root.title("KNX Cleaner & Updater")
root.resizable(False,False)
root.iconbitmap("icon.ico")
font=ctk.CTkFont(family='Centaur', size=17)
label = ctk.CTkLabel(root, text="KNX Cleaner & Updater", font=font)
label.pack()

# Define color constants
bg_color = "#242424"
text_color = "#A9A9A9"
button_color = "#161616"
button_color_hover = "#2F2F2F"
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
    success = False  # Initiate the success variable
    try:
        result = func()  # Call the function directly without extra output
        root.update()  # Update the GUI to keep it responsive
        if result is False:
            print(f"Function {func.__name__} Failed!")  # Print the failure message
        else:
            print(f"Function {func.__name__} Completed!")  # Print the completion message
        success = True  # Mark the function as successful
    except Exception as e:
        print(f"Error running function {func.__name__}: {e}")
    finally:
        if not stop_event.is_set():  # Add condition to check if the function was stopped
            print("Pause 0.5s...")
            time.sleep(0.5)  # 0.5 second pause
        output_text.see(tk.END)

# Run all functions
def run_all_functions(functions_to_run):
    results = {}
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            try:
                func_result = func()  # Call the function directly without extra output
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)
    show_result_message(results)

# Run selected functions
def run_selected_functions(selected_functions):
    checked_functions = [func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]
    if not checked_functions:
        # Spoja emoji s hláškou
        message = f"⚠️ No Functions Selected.\nPlease select at least one function to run."
        show_alert_window("Warning", message)
        return

    results = {}
    for func_name in selected_functions:
        func = functions_mapping.get(func_name)
        if func:
            try:
                func_result = func()  # Call the function directly without extra output
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)
    show_result_message(results)

def show_result_message(results):
    success = all(result is True for result in results.values())
    if success:
        message = "✅ All functions executed successfully."
    else:
        message = "❌ Some functions encountered errors:\n"
        for func_name, result in results.items():
            if result is not True:
                message += f"❗{func_name}: {result}.\n"
    show_alert_window("Function Execution Results", message.strip())

def show_alert_window(title, message):
    alert_window = ctk.CTkToplevel(root)
    alert_window.title("Results")
    alert_window.resizable(False, False)
    alert_window.attributes('-topmost', True)  # Make window always on top
    alert_window.after(250, lambda: alert_window.iconbitmap("icon.ico"))
    alert_window.grab_set()  # Nastavenie modálneho okna

    # Get main window position
    main_x = root.winfo_x()
    main_y = root.winfo_y()
    main_width = root.winfo_width()
    main_height = root.winfo_height()
    # Calculate alert window position
    alert_x = main_x + main_width // 2 - 150
    alert_y = main_y + main_height // 2 - 75
    alert_window.geometry(f"+{alert_x}+{alert_y}")

    message_label = ctk.CTkLabel(alert_window, text=message, font=font, wraplength=300)
    message_label.pack(pady=10, padx=30)

    ok_button = ctk.CTkButton(alert_window, text="OK", command=alert_window.destroy, fg_color=button_color, hover_color=button_color_hover, font=font)
    ok_button.pack(pady=10)

# Functions with Text
functions_mapping = {
    "Run Learix FPS": learix_fps.learix_fps,
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
canvas = ctk.CTkCanvas(root, width=250, height=400, highlightthickness=0, bg=bg_color)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Functions buttons
function_buttons_frame = ctk.CTkCanvas(canvas,highlightthickness=0, bg=bg_color)

# Scrollbar functionality
scrollbar = ctk.CTkScrollbar(root, command=canvas.yview)
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
    button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

    checkbox = ctk.CTkCheckBox(button_frame, text=function_name, variable=checkbox_var, onvalue=True,font=font,offvalue=False, border_width=1, checkbox_width=18, checkbox_height=18, hover_color=text_color, fg_color=(text_color, button_color))
    checkbox.pack(side=tk.LEFT, padx=5)

# Update the canvas scroll region after adding widgets
function_buttons_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Run all, stop all, run selected buttons
run_selected_functions_button = ctk.CTkButton(root, text="Run Selected", command=lambda: run_selected_functions([func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]), fg_color=button_color, hover_color=button_color_hover, font=font)
run_selected_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

all_functions_button = ctk.CTkButton(root, text="Run All", command=lambda: run_all_functions(functions_mapping.keys()), fg_color=button_color, hover_color=button_color_hover, font=font)
all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

stop_all_functions_button = ctk.CTkButton(root, text="Stop All", command=stop_all_functions, fg_color=red_color, hover_color=red_color_hover, font=font)
stop_all_functions_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Output Text Widget
output_text = ctk.CTkTextbox(root, width=250, height=200, wrap=tk.WORD, font=font, fg_color=button_color)
output_text.pack(pady=5, padx=5)

# ******************** RUN ********************
# Output Text - Redirect stdout to the output text widget
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Scroll to the bottom
        print("Console: ")

    def flush(self):
        pass  # No need to flush anything in this case
root.mainloop()
