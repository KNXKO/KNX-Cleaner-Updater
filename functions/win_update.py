import os

def win_update():
    try:
        os.system("start ms-settings:windowsupdate")
        print("Opened Windows Update")
    except Exception as e:
        print("Error opening Windows Update:", str(e))