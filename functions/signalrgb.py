import os
signalrgb_path = ("AssetsScripts\SignalRgb.lnk")

def open_signalrgb():
    try:
        os.startfile(signalrgb_path)
        print("Opened SignalRGB")
    except Exception as e:
        print("Error opening SignalRGB:", str(e))