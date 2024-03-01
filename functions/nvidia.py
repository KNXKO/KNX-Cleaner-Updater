import os

nvidia_path = r'AssetsScripts\NVIDIA.lnk'

def open_nvidia():
    try:
        os.startfile(nvidia_path)
        print("Opened Nvidia App")
    except Exception as e:
        print("Error opening Nvidia App:", str(e))