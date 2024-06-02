import os

def win_update():
    try:
        os.system("start ms-settings:windowsupdate")
        print("Windows Update successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Windows Update: {e}")
        return False
