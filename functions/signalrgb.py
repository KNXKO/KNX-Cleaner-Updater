import os

signalrgb_path = r'AssetsScripts\SignalRgb.lnk'

def open_signalrgb():
    try:
        os.startfile(signalrgb_path)
        print("SignalRGB successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening SignalRGB: {e}")
        return False
