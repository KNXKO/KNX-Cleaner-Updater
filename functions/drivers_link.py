import webbrowser

def open_drivers_link():
    try:
        webbrowser.open('https://rog.asus.com/motherboards/rog-strix/rog-strix-b550-f-gaming-model/helpdesk_download/')
        webbrowser.open_new_tab('https://www.amd.com/en/support/chipsets/amd-socket-am4/b550')
        print("Opened web browser with links")
    except Exception as e:
        print("Error opening web browser with links:", str(e))