import customtkinter as ctk
import getpass
import threading
import os
import ctypes
import sys

def _ensure_admin():
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
    except Exception:
        pass

_ensure_admin()

from src.interface.utils import *
from src.interface.todo import load_todos, save_todos
from src.scripts import functions_mapping
VERSION = "6.0"

# ************ COLORS ************
bg_color = "#242424"
text_color = "#A9A9A9"
button_color = "#161616"
button_color_hover = "#0d0d0d"
green_color = "#33691E"
red_color = "#441A19"
red_color_hover = "#291111"

last_run_datetime = get_last_run_datetime()
save_last_run_datetime()
time_difference_text = calculate_time_difference(last_run_datetime)
accent_color = get_accent_color()

username = getpass.getuser()

# ******** GUI ********
root = ctk.CTk()
root.geometry("550x500")
ctk.set_appearance_mode("dark")
root.title("KNX Cleaner & Updater V5")
root.resizable(False, False)

def set_icon():
    try:
        icon_path = os.path.abspath("icon.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Warning: Could not set icon: {e}")

root.after(500, set_icon)

font = ctk.CTkFont(family='Centaur', size=18)
label = ctk.CTkLabel(root, text=f"Hello, {username}! {time_difference_text}. Version {VERSION}", font=font)
label.pack()
stop_event = threading.Event()

# ************ SCRIPT RUNNER ************
def run_functions(functions_to_run):
    results = {}
    for func_name in functions_to_run:
        if stop_event.is_set():
            break
        func = functions_mapping.get(func_name)
        if func:
            try:
                print(f"Running {func_name}...")
                func_result = func()
                results[func_name] = func_result
            except Exception as e:
                results[func_name] = str(e)
    print("====================")
    root.after(0, result_message, results)

def threaded_function(func, *args):
    stop_event.clear()
    thread = threading.Thread(target=func, args=args)
    thread.start()

def run_all_functions():
    threaded_function(run_functions, functions_mapping.keys())

def run_selected_functions():
    selected_functions = [name for name, var in checkboxes.items() if var.get()]
    if not selected_functions:
        print("No functions selected.")
        return
    for var in checkboxes.values():
        if var.get():
            var.set(False)
    threaded_function(run_functions, selected_functions)

def stop_all_functions():
    stop_event.set()
    print("All functions stopped.")

# ******************** LAYOUT ********************
scrollbar = ctk.CTkScrollbar(root)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

canvas = ctk.CTkCanvas(root, width=250, height=400, highlightthickness=0, bg=bg_color)
canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

right_frame = ctk.CTkCanvas(canvas, highlightthickness=0, bg=bg_color)

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)
_window_id = canvas.create_window((0, 0), window=right_frame, anchor=ctk.NW)

def on_canvas_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")
canvas.bind_all("<MouseWheel>", on_canvas_mouse_wheel)

def _on_canvas_resize(event):
    canvas.itemconfigure(_window_id, width=event.width)
canvas.bind("<Configure>", _on_canvas_resize)

def _refresh_scroll():
    right_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

# ******************** TAB BAR ********************
tab_frame = ctk.CTkFrame(right_frame, fg_color=bg_color)
tab_frame.pack(side=ctk.TOP, fill=ctk.X, pady=(8, 4))

tab_inner = ctk.CTkFrame(tab_frame, fg_color=bg_color)
tab_inner.pack()

tab_font = ctk.CTkFont(family='Centaur', size=15)

btn_tab_main = ctk.CTkButton(
    tab_inner, text="Main", font=tab_font, height=28, width=85,
    fg_color=accent_color, hover_color=button_color_hover,
    corner_radius=6
)
btn_tab_main.pack(side=ctk.LEFT, padx=(0, 2))

btn_tab_todo = ctk.CTkButton(
    tab_inner, text="Todo", font=tab_font, height=28, width=85,
    fg_color=button_color, hover_color=button_color_hover,
    corner_radius=6
)
btn_tab_todo.pack(side=ctk.LEFT, padx=(2, 0))

# ******************** MAIN BODY ********************
main_body = ctk.CTkFrame(right_frame, fg_color=bg_color)
main_body.pack(side=ctk.TOP, fill=ctk.X)

checkboxes = {}
for function_name, func in functions_mapping.items():
    checkbox_var = ctk.BooleanVar(value=False)
    checkboxes[function_name] = checkbox_var

    row = ctk.CTkFrame(main_body, fg_color=bg_color)
    row.pack(side=ctk.TOP, fill=ctk.X, pady=5)

    ctk.CTkCheckBox(
        row, text=function_name, variable=checkbox_var,
        onvalue=True, offvalue=False, font=font,
        border_width=1, checkbox_width=18, checkbox_height=18,
        hover_color=accent_color, fg_color=accent_color
    ).pack(side=ctk.LEFT, padx=5)

# ******************** TODO BODY ********************
todo_body = ctk.CTkFrame(right_frame, fg_color=bg_color)
# not packed — shown only when Todo tab active

TODO_WRAP_ACTIVE = 190
TODO_WRAP_DONE = 145

def _rebuild_todo():
    for w in todo_body.winfo_children():
        w.destroy()

    add_frame = ctk.CTkFrame(todo_body, fg_color=bg_color)
    add_frame.pack(fill=ctk.X, pady=3, padx=2)

    entry_var = ctk.StringVar()
    entry = ctk.CTkEntry(
        add_frame, textvariable=entry_var, placeholder_text="Add task...",
        font=font, fg_color=button_color, border_width=1, border_color=accent_color
    )
    entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=(4, 2))

    def add_task(event=None):
        text = entry_var.get().strip()
        if not text:
            return
        todos = load_todos()
        todos.append({"text": text, "done": False})
        save_todos(todos)
        _rebuild_todo()
        _refresh_scroll()

    entry.bind("<Return>", add_task)
    ctk.CTkButton(
        add_frame, text="+", width=36, command=add_task,
        fg_color=accent_color, hover_color=button_color_hover, font=font
    ).pack(side=ctk.LEFT, padx=(0, 4))

    todos = load_todos()
    active = [(i, t) for i, t in enumerate(todos) if not t["done"]]
    done_items = [(i, t) for i, t in enumerate(todos) if t["done"]]

    for i, todo in active:
        row = ctk.CTkFrame(todo_body, fg_color=bg_color)
        row.pack(fill=ctk.X, pady=5)

        var = ctk.BooleanVar(value=False)

        def make_check(idx):
            def on_check():
                t = load_todos(); t[idx]["done"] = True; save_todos(t)
                _rebuild_todo(); _refresh_scroll()
            return on_check

        cb = ctk.CTkCheckBox(
            row, text=todo["text"], variable=var, command=make_check(i),
            font=font, checkbox_width=18, checkbox_height=18,
            hover_color=accent_color, fg_color=accent_color, border_width=1
        )
        cb.pack(side=ctk.LEFT, padx=5)
        cb._text_label.configure(wraplength=TODO_WRAP_ACTIVE)

    if done_items:
        ctk.CTkLabel(
            todo_body, text="── Done ──", font=font, text_color=text_color
        ).pack(fill=ctk.X, pady=(6, 0))

        for i, todo in done_items:
            row = ctk.CTkFrame(todo_body, fg_color=bg_color)
            row.pack(fill=ctk.X, pady=5)

            var = ctk.BooleanVar(value=True)

            def make_uncheck(idx):
                def on_uncheck():
                    t = load_todos(); t[idx]["done"] = False; save_todos(t)
                    _rebuild_todo(); _refresh_scroll()
                return on_uncheck

            def make_delete(idx):
                def on_delete():
                    t = load_todos(); t.pop(idx); save_todos(t)
                    _rebuild_todo(); _refresh_scroll()
                return on_delete

            ctk.CTkButton(
                row, text="✕", width=30, command=make_delete(i),
                fg_color=red_color, hover_color=red_color_hover, font=font
            ).pack(side=ctk.RIGHT, padx=5)

            cb = ctk.CTkCheckBox(
                row, text=todo["text"], variable=var, command=make_uncheck(i),
                font=font, checkbox_width=18, checkbox_height=18,
                hover_color=accent_color, fg_color=accent_color, border_width=1,
                text_color=text_color
            )
            cb.pack(side=ctk.LEFT, padx=5)
            cb._text_label.configure(wraplength=TODO_WRAP_DONE)

# ******************** TAB SWITCHING ********************
def show_main():
    todo_body.pack_forget()
    main_body.pack(side=ctk.TOP, fill=ctk.X, after=tab_frame)
    btn_tab_main.configure(fg_color=accent_color)
    btn_tab_todo.configure(fg_color=button_color)
    _refresh_scroll()

def show_todo():
    main_body.pack_forget()
    _rebuild_todo()
    todo_body.pack(side=ctk.TOP, fill=ctk.X, after=tab_frame)
    btn_tab_todo.configure(fg_color=accent_color)
    btn_tab_main.configure(fg_color=button_color)
    _refresh_scroll()

btn_tab_main.configure(command=show_main)
btn_tab_todo.configure(command=show_todo)

_refresh_scroll()
root.after(200, _refresh_scroll)

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
