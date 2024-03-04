import subprocess

def run_sfc_scan():
    try:
        # Spustenie externeho cmd okna a vykonanie prikazu sfc /scannow
        subprocess.run("cmd /c sfc /scannow", shell=True)
        print("SFC skenovanie bolo úspešne spustené.")
    except Exception as e:
        print(f"Chyba pri vykonávaní príkazu sfc /scannow: {e}")
