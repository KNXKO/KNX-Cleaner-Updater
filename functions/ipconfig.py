import subprocess

def flush_dns():
    try:
        # Run an external command prompt window and execute the ipconfig /flushdns command
        result = subprocess.run("cmd /c ipconfig /flushdns", shell=True, check=True)
        print("Successfully flushed the DNS cache.")
        return True
    except subprocess.CalledProcessError:
        print("Error occurred while flushing the DNS cache.")
        return False
