import subprocess

# Close Apps - Spotify, Browser
def close_apps():
    try:
        subprocess.Popen('taskkill /F /IM Spotify.exe', shell=True)
        print("Spotify successfully closed.")
        return True
    except Exception as e:
        print(f"An error occurred while closing Spotify: {e}")
        return False

    '''
    try:
        subprocess.Popen('taskkill /F /IM thorium.exe', shell=True)  # Ukážeme príklad pre Chrome, ale môžete zmeniť na svoj prehliadač
        print("Browser successfully closed.")
        return True
    except Exception as e:
        print(f"An error occurred while closing the browser: {e}")
        return False
    '''