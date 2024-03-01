import subprocess

# Close Apps - Spotify, Browser
def close_apps():
    try:
        subprocess.Popen('taskkill /F /IM Spotify.exe', shell=True)
        print("Spotify closed successfully.")
    except Exception as e:
        print("An error occurred while closing Spotify:", str(e))
'''
    try:
        subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
        print("Browser closed successfully.")
    except Exception as e:
        print("An error occurred while closing the browser:", str(e))
'''