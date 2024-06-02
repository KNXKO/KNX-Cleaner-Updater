import os

ticktick_path = r'AssetsScripts\TickTick.lnk'

def open_ticktick():
    try:
        os.startfile(ticktick_path)
        print("TickTick successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening TickTick: {e}")
        return False
