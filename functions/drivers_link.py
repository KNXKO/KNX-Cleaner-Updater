import webbrowser

link1 = 'https://rog.asus.com/motherboards/rog-strix/rog-strix-b550-f-gaming-model/helpdesk_download/'
link2 = 'https://www.amd.com/en/support/chipsets/amd-socket-am4/b550'

def open_drivers_link():
    try:
        webbrowser.open(link1)
        webbrowser.open_new_tab(link2)
        print("Web browser successfully opened with links.")
        return True
    except Exception as e:
        print(f"Error opening web browser with links: {e}")
        return False
