import os

temp_path = r'AssetsScripts\SPEEDUP.BAT'

def clean_temp():
    try:
        os.startfile(temp_path)
        print("Cleaned Temp Folder")
    except Exception as e:
        print("Error running Clean Temp Script:", str(e))