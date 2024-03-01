import os

logfiles_path = r'AssetsScripts\Log Files Cleaner.bat'

def run_logfiles():
    try:
        os.startfile(logfiles_path)
        print("Opened Log Folder")
    except Exception as e:
        print("Error opening Log Files Cleaner Script:", str(e))
