import os

ccleaner_path = 'AssetsScripts\CCleaner64.exe'

def open_ccleaner():
    try:
        os.startfile(ccleaner_path)
        print("Successfully opened CCleaner.")
        return True
    except Exception as e:
        print(f"Error opening CCleaner: {e}")
        return False