import subprocess

def flush_dns():
    try:
        # Spustenie externeho cmd okna a vykonanie prikazu ipconfig /flushdns
        subprocess.run("cmd /c ipconfig /flushdns", shell=True)
        print("DNS cache bol úspešne vyčistený.")
    except Exception as e:
        print(f"Chyba pri vykonávaní príkazu ipconfig /flushdns: {e}")
