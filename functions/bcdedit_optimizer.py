import os

bcdedit_path = r'AssetsScripts\Bcdedit Optimizer.cmd'

def run_bcdedit():
    try:
        os.startfile(bcdedit_path)
        print("Successfully opened Bcdedit Optimizer script.")
        return True
    except Exception as e:
        print(f"Error opening Bcdedit Optimizer script: {e}")
        return False