import os
adobe_path = ("AssetsScripts\Adobe Creative Cloud.lnk")

def open_adobe():
    try:
        os.startfile(adobe_path)
        print("Opened Adobe Creative Cloud")
    except Exception as e:
        print("Error opening Adobe Creative Cloud:", str(e))