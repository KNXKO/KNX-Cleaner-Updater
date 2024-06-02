import os

def ms_store_update():
    try:
        os.system("start ms-windows-store:home")
        print("Microsoft Store successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Microsoft Store: {e}")
        return False
