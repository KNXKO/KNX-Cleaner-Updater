import os

bcdedit_path = r'AssetsScripts\Bcdedit Optimizer.cmd'

def run_bcdedit():
    try:
        os.startfile(bcdedit_path)
        print("Opened Bcdedit Optimizer Script")
    except Exception as e:
        print("Error opening Bcdedit Optimizer Script:", str(e))