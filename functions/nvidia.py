import os
nvidia_path = ("AssetsScripts\GeForce Experience.lnk")

def open_nvidia():
    try:
        os.startfile(nvidia_path, "r")
        print("Opened Nvidia Experience")
    except Exception as e:
        print("Error opening Nvidia Experience:", str(e))