import subprocess

def defrag():
    try:
        subprocess.Popen('dfrgui.exe')
        print("Disk Defragmenter successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Disk Defragmenter: {e}")
        return False