import customtkinter as ctk
import getpass
import threading
import os
from src.interface.utils import *
from src.scripts import functions_mapping
VERSION = "5.0"

# ************ COLORS ************
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

# ******** GUI  ********
root = ctk.CTk()
root.geometry("550x500")
ctk.set_appearance_mode("dark")
root.title("KNX Cleaner & Updater V5")
root.resizable(False, False)

# Nastavenie ikony s oneskorením a ošetrením chyby
def set_icon():
    try:
        icon_path = os.path.abspath("icon.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Varovanie: Nepodarilo sa nastaviť ikonu: {e}")
        # Aplikácia bude pokračovať s predvolenou ikonou

# Nastavenie ikony po spustení hlavného okna
root.after(500, set_icon)

font = ctk.CTkFont(family='Centaur', size=18)
label = ctk.CTkLabel(root, text=f"Hello, {username}! {time_difference_text}. Version {VERSION}", font=font)
label.pack()
stop_event = threading.Event()

# ************ FUNCTIONS TO RUN SCRIPTS  ************
def run_functions(functions_to_run):
    results = {}
    for func_name in functions_to_run:
        if stop_event.is_set():
            break
        func = functions_mapping.get(func_name)
        if func:
            try:
                output_text.insert(ctk.END, f"Running {func_name}...\n")
                func_result = func()
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)
    output_text.insert(ctk.END, "====================\n")
    output_text.see(ctk.END)
    result_message(results)

def threaded_function(func, *args):
    stop_event.clear()
    thread = threading.Thread(target=func, args=args)
    thread.start()

def run_all_functions():
    threaded_function(run_functions, functions_mapping.keys())

def run_selected_functions():
    selected_functions = [func_name for func_name, checkbox_var in checkboxes.items() if checkbox_var.get()]
    if not selected_functions:
        print("⚠️ No functions selected.")
        return
    # Clear checkboxes after execution
    for checkbox_var in checkboxes.values():
        if checkbox_var.get():
            checkbox_var.set(False)
    threaded_function(run_functions, selected_functions)

def stop_all_functions():
    stop_event.set()
    print("⚠️ All functions stopped.")

# ******************** GUI ********************
canvas = ctk.CTkCanvas(root, width=250, height=400, highlightthickness=0, bg=bg_color)
canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

right_frame = ctk.CTkCanvas(canvas, highlightthickness=0, bg=bg_color)

# ******************** SCROLLBAR ********************
scrollbar = ctk.CTkScrollbar(root, command=canvas.yview)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
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
btn_runAll = ctk.CTkButton(root, text="Run All", command=run_all_functions, fg_color=accent_color, hover_color=button_color_hover, font=font)
btn_runAll.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

btn_stopAll = ctk.CTkButton(root, text="Stop All", command=stop_all_functions, fg_color=red_color, hover_color=red_color_hover, font=font)
btn_stopAll.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

btn_runSelected = ctk.CTkButton(root, text="Run Selected", command=run_selected_functions, fg_color=button_color, hover_color=button_color_hover, font=font)
btn_runSelected.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=3)

# ******************** CONSOLE ********************
output_text = create_console_output(root)

# ******************** MAIN ********************
root.mainloop()