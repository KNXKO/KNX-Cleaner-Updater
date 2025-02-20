import os

adobe_path = r'src\shortcuts\Adobe Creative Cloud.lnk'
word_path = r'src\shortcuts\Word.lnk'
signal_path = r'src\shortcuts\Signal.lnk'
nvidia_path = r'src\shortcuts\NVIDIA.lnk'
signalrgb_path = r'src\shortcuts\SignalRgb.lnk'
ccleaner_path = r'src\shortcuts\CCleaner64.exe'

def open_adobe():
    try:
        print("Opening Adobe Creative Cloud...")
        os.startfile(adobe_path)
        print("Adobe Creative Cloud successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Adobe Creative Cloud: {e}")
        return False

def open_word():
    try:
        print("Opening Microsoft Word...")
        os.startfile(word_path)
        print("Microsoft Word successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Microsoft Word: {e}")
        return False

def open_signal():
    try:
        print("Opening Signal...")
        os.startfile(signal_path)
        print("Signal successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Signal: {e}")
        return False

def open_nvidia():
    try:
        print("Opening NVIDIA App...")
        os.startfile(nvidia_path)
        print("NVIDIA App successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening NVIDIA App: {e}")
        return False

def open_signalrgb():
    try:
        print("Opening SignalRGB...")
        os.startfile(signalrgb_path)
        print("SignalRGB successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening SignalRGB: {e}")
        return False

def open_ccleaner():
    try:
        print("Opening CCleaner...")
        os.startfile(ccleaner_path)
        print("CCleaner successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening CCleaner: {e}")
        return False

def open_win_update():
    try:
        print("Opening Windows Update...")
        os.system("start ms-settings:windowsupdate")
        print("Windows Update successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Windows Update: {e}")
        return False

def open_ms_update():
    try:
        print("Opening Microsoft Store...")
        os.system("start ms-windows-store:home")
        print("Microsoft Store successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Microsoft Store: {e}")
        return False