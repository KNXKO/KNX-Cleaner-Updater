import subprocess

# Close Spotify
def close_spotify():
    try:
        subprocess.Popen('taskkill /F /IM Spotify.exe', shell=True)
        print("Spotify closed successfully.")
    except Exception as e:
        print("An error occurred while closing Spotify:", str(e))

''' No need to close
# Close browser
def close_browser():
    try:
        subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
        print("Browser closed successfully.")
    except Exception as e:
        print("An error occurred while closing the browser:", str(e))
'''