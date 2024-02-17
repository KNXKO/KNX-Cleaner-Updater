import os

ccleaner_path = 'AssetsScripts\CCleaner64.exe'

def open_ccleaner():
    try:
        os.startfile(ccleaner_path)
        print("Opened CCleaner")
    except Exception as e:
        print("Error opening CCleaner:", str(e))