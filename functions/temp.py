import os

temp_path = r'AssetsScripts\SPEEDUP.BAT'

def clean_temp():
    try:
        os.startfile(temp_path)
        print("Opened Temp Folder")
    except Exception as e:
        print("Error opening Clean Temp Script:", str(e))