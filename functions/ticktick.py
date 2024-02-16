import os
ticktick_path = ("AssetsScripts\TickTick.lnk")

def open_ticktick():
    try:
        os.startfile(ticktick_path)
        print("Opened TickTick")
    except Exception as e:
        print("Error opening TickTick:", str(e))