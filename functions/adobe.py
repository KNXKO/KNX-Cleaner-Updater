import os

adobe_path = r'AssetsScripts\Adobe Creative Cloud.lnk'

def open_adobe():
    try:
        os.startfile(adobe_path)
        print("Adobe Creative Cloud successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Adobe Creative Cloud: {e}")
        return False
