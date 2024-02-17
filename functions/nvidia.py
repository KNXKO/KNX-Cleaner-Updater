import os

nvidia_path = r'AssetsScripts\GeForce Experience.lnk'

def open_nvidia():
    try:
        os.startfile(nvidia_path)
        print("Opened Nvidia Experience")
    except Exception as e:
        print("Error opening Nvidia Experience:", str(e))