import psutil
import subprocess

# Close Spotify
def close_spotify():
    try:
        for proc in psutil.process_iter():
            if "spotify" in proc.name().lower():
                proc.kill()
                print("Spotify closed successfully.")
                break
        else:
            print("Spotify is not running.")
    except Exception as e:
        print("An error occurred while closing Spotify:", str(e))

# Close browser
def close_browser():
    try:
        subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
        print("Browser closed successfully.")
    except Exception as e:
        print("An error occurred while closing the browser:", str(e))