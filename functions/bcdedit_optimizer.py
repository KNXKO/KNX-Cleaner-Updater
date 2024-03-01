import os

bcdedit_path = r'AssetsScripts\Bcdedit Optimizer.cmd'

def run_bcdedit():
    try:
        os.startfile(bcdedit_path)
        print("Bcdedit Optimizer Script executed successfully.")
    except Exception as e:
        print("Error running Bcdedit Optimizer Script:", str(e))