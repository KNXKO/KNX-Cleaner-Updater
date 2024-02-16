import os
word_path = ("AssetsScripts\Word.lnk")

def open_word():
    try:
        os.startfile(word_path)
        print("Opened Word")
    except Exception as e:
        print("Error opening Word:", str(e))