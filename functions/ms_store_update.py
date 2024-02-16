import os

def ms_store_update():
    try:
        os.system("start ms-windows-store:home")
        print("Opened Microsoft Store")
    except Exception as e:
        print("Error opening Microsoft Store:", str(e))