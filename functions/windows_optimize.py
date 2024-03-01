import os

win_optimize_path = r'AssetsScripts\Windows Optimization.bat'

def run_win_optimize():
    try:
        os.startfile(win_optimize_path)
        print("Opened Windows Optimize Script")
    except Exception as e:
        print("Error openning Windows Optimize Script:", str(e))
