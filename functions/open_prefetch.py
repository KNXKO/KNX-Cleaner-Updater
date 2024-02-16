import os
prefetch_path = 'C:\Windows\Prefetch'

def open_prefetch():
    try:
        os.startfile(prefetch_path)
        print("Opened Prefetch Folder")
    except Exception as e:
        print("Error opening Prefetch Folder:", str(e))