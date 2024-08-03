import os

win_optimize_path = r'AssetsScripts\Windows Optimization.bat'

def run_win_optimize():
    try:
        os.startfile(win_optimize_path)
        print("Windows Optimize successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Windows Optimize: {e}")
        return False
