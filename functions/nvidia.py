import os

nvidia_path = r'AssetsScripts\NVIDIA.lnk'

def open_nvidia():
    try:
        os.startfile(nvidia_path)
        print("Nvidia App successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Nvidia App: {e}")
        return False
