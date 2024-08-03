import subprocess

def flush_dns():
    try:
        # Run an external command prompt window and execute the ipconfig /flushdns command
        result = subprocess.run("cmd /c ipconfig /flushdns", shell=True, check=True)
        print("DNS cache successfully flushed.")
        return True
    except subprocess.CalledProcessError:
        print("Failed to flush the DNS cache.")
        return False
