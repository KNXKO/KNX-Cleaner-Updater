import os

logfiles_path = r'AssetsScripts\Log Files Cleaner.bat'

def run_logfiles():
    try:
        os.startfile(logfiles_path)
        print("Log folder successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Log Files Cleaner Script: {e}")
        return False
