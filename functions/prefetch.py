import os

prefetch_path = r'C:\Windows\Prefetch'

def open_prefetch():
    try:
        os.startfile(prefetch_path)
        print("Prefetch folder successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Prefetch Folder: {e}")
        return False
