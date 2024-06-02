import os

word_path = r'AssetsScripts\Word.lnk'

def open_word():
    try:
        os.startfile(word_path)
        print("Word successfully opened.")
        return True
    except Exception as e:
        print(f"Error opening Word: {e}")
        return False
