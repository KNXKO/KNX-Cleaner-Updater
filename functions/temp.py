import os

temp_path = r'AssetsScripts\SPEEDUP.BAT'

def clean_temp():
    try:
        os.startfile(temp_path)
        print("Temp folder successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Clean Temp Script: {e}")
        return False
