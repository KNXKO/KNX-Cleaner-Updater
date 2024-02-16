import subprocess

def defrag():
    try:
        subprocess.Popen('dfrgui.exe')
        print("Opened Disk Defragmenter")
    except Exception as e:
        print("Error opening Disk Defragmenter:", str(e))