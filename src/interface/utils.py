import customtkinter as ctk
import sys
import winreg
from datetime import datetime, timedelta

# Define color constants
bg_color = "#242424"
text_color = "#A9A9A9"
button_color = "#161616"
button_color_hover = "#0d0d0d"
green_color = "#33691E"
red_color = "#441A19"
red_color_hover = "#291111"

# ******************** ACCENT COLOR ********************
def get_accent_color():
    try:
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            value, _ = winreg.QueryValueEx(key, "AccentColorMenu")
            # Extract blue, green, and red components
            blue = (value >> 16) & 0xFF
            green = (value >> 8) & 0xFF
            red = value & 0xFF
            # Convert to hex color string in RGB format
            hex_color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
            return hex_color
    except Exception as e:
        print(f"⚠️ Error reading accent color: {e}")
        return "#441A19"  # Default color if reading fails

# ******************** TIME ********************
def get_last_run_datetime():
    try:
        with open("logs/last_run.txt", "r") as file:
            last_run_str = file.read().strip()
            return datetime.strptime(last_run_str, "%Y-%m-%d %H:%M:%S")
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"⚠️ Error reading last run date: {e}")
        return None

# Function to save current datetime to file
def save_last_run_datetime():
    try:
        current_datetime = datetime.now()
        with open("logs/last_run.txt", "w") as file:
            file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print(f"⚠️ Error saving last run date: {e}")

# Function to calculate time difference
def calculate_time_difference(last_run_datetime):
    if last_run_datetime:
        current_datetime = datetime.now()
        time_difference = current_datetime - last_run_datetime

        if time_difference < timedelta(minutes=1):
            return "Last seen less than a minute ago"
        elif time_difference < timedelta(hours=1):
            minutes = int(time_difference.total_seconds() // 60)
            return f"Last seen {minutes} minutes ago"
        elif time_difference < timedelta(days=1):
            hours = int(time_difference.total_seconds() // 3600)
            return f"Last seen {hours} hours ago"
        else:
            days = time_difference.days
            return f"Last seen {days} days ago"
    else:
        return None

# ******************** ALERT ********************
def result_message(results):
    success = all(result is True for result in results.values())
    if success:
        message = "✅ Functions executed successfully."
    else:
        message = "❌ Some functions encountered errors:\n"
        for func_name, result in results.items():
            if result is not True:
                message += f"❗{func_name}: {result}.\n"
    alert_window("Function Execution Results", message.strip())

def alert_window(title, message):
    alert_window = ctk.CTkToplevel()
    alert_window.title("Results")
    alert_window.resizable(False, False)
    alert_window.attributes('-topmost', True)
    font = ctk.CTkFont(family='Centaur', size=18)
    alert_window.after(250, lambda: alert_window.iconbitmap("icon.ico"))
    alert_window.grab_set()

    message_label = ctk.CTkLabel(alert_window, text=message, font=font, wraplength=300)
    message_label.pack(pady=10, padx=30)

    ok_button = ctk.CTkButton(alert_window, text="OK", command=alert_window.destroy, fg_color=button_color, hover_color=button_color_hover, font=font)
    ok_button.pack(pady=10)

# ******************** CONSOLE ********************
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(ctk.END, text)
        self.widget.see(ctk.END)

    def flush(self):
        pass

def create_console_output(root):
    output_text = ctk.CTkTextbox(root, width=250, height=350, wrap=ctk.WORD, font=ctk.CTkFont(family='Centaur', size=17), fg_color="#161616")
    output_text.pack(pady=5, padx=5)
    sys.stdout = StdoutRedirector(output_text)
    return output_text

# ******************** ALL ********************
__all__ = ['get_accent_color', 'get_last_run_datetime', 'save_last_run_datetime', 'calculate_time_difference', 'result_message', 'alert_window', 'create_console_output']