import customtkinter as ctk
import getpass
from mirror import *
from functions import disk_cleanup, prefetch, win_update, ms_store_update, defrag, temp, learix_fps, adobe, word, ticktick, signalrgb, ccleaner, close_apps, nvidia, drivers_link, bcdedit_optimizer, log_files, windows_optimize, ipconfig

# Define color constants
bg_color = "#242424"
text_color = "#A9A9A9"
button_color = "#161616"
button_color_hover = "#0d0d0d"
green_color = "#33691E"
red_color = "#441A19"
red_color_hover = "#291111"

# Time
last_run_datetime = get_last_run_datetime()
save_last_run_datetime()
time_difference_text = calculate_time_difference(last_run_datetime)

accent_color = get_accent_color()

# Greet user with their name
username = getpass.getuser()

# ******** Title, Window, Font, Icon ********
root = ctk.CTk()
root.geometry("550x500")
ctk.set_appearance_mode("dark")
root.title("KNX Cleaner & Updater")
root.resizable(False, False)
root.iconbitmap("icon.ico")
font = ctk.CTkFont(family='Centaur', size=18)
label = ctk.CTkLabel(root, text=f"Hello, {username}! {time_difference_text}.", font=font)
label.pack()

# Stop all functions
def stop_all_functions():
    print("All functions execution stopped!")

# Run single function
def run_function(func):
    success = False
    try:
        result = func()
        root.update()
        if result is False:
            print(f"Function {func.__name__} Failed!")
    except Exception as e:
        print(f"Error running function {func.__name__}: {e}")

# Run all functions
def run_all_functions(functions_to_run):
    results = {}
    for func_name in functions_to_run:
        func = functions_mapping.get(func_name)
        if func:
            try:
                output_text.insert(ctk.END, f"Running function {func_name}...\n")
                func_result = func()
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)
    output_text.insert(ctk.END, "====================\n")
    output_text.see(ctk.END)
    result_message(results)

# Run selected functions
def run_selected_functions(selected_functions):
    checked_functions = [func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]
    if not checked_functions:
        message = f"⚠️ No Functions Selected.\nPlease select at least one function to run."
        alert_window("Warning", message)
        return

    results = {}
    for func_name in selected_functions:
        func = functions_mapping.get(func_name)
        if func:
            try:
                func_result = func()
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)

    # Clear checkboxes after execution
    for func_name, checkbox_var in checkboxes.items():
        if checkbox_var.get():
            checkbox_var.set(False)

    output_text.insert(ctk.END, "====================\n")
    output_text.see(ctk.END)
    result_message(results)

# ******************** FUNCTIONS ********************
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
canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

right_frame = ctk.CTkCanvas(canvas, highlightthickness=0, bg=bg_color)

# ******************** SCROLLBAR ********************
scrollbar = ctk.CTkScrollbar(root, command=canvas.yview)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
# Configure canvas and scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=right_frame, anchor=ctk.NW)
# Function to scroll the canvas with the mouse wheel
def on_canvas_mouse_wheel(event):
    canvas.yview_scroll(-1*(event.delta//120), "units")
canvas.bind_all("<MouseWheel>", on_canvas_mouse_wheel)

# ******************** CHECKBOXES ********************
checkboxes = {}
for function_name, func in functions_mapping.items():
    checkbox_var = ctk.BooleanVar(value=False)
    checkboxes[function_name] = checkbox_var

    button_frame = ctk.CTkFrame(right_frame)
    button_frame.pack(side=ctk.TOP, fill=ctk.X, pady=5)

    checkbox = ctk.CTkCheckBox(button_frame, text=function_name, variable=checkbox_var, onvalue=True, font=font, offvalue=False, border_width=1, checkbox_width=18, checkbox_height=18, hover_color=accent_color, fg_color=accent_color)
    checkbox.pack(side=ctk.LEFT, padx=5)

# Update the canvas scroll region after adding widgets
right_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# ******************** BUTTONS ********************
btn_runAll = ctk.CTkButton(root, text="Run All", command=lambda: run_all_functions(functions_mapping.keys()), fg_color=accent_color, hover_color=button_color_hover, font=font)
btn_runAll.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

btn_stopAll = ctk.CTkButton(root, text="Stop All", command=stop_all_functions, fg_color=red_color, hover_color=red_color_hover, font=font)
btn_stopAll.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

btn_runSelected = ctk.CTkButton(root, text="Run Selected", command=lambda: run_selected_functions([func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]), fg_color=button_color, hover_color=button_color_hover, font=font)
btn_runSelected.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

# ******************** CONSOLE ********************
output_text = create_console_output(root)

# ******************** MAIN ********************
root.mainloop()