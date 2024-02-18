import pygetwindow as gw

# Získanie zoznamu všetkých okien
all_windows = gw.getAllTitles()

# Výpis názvov okien
for window in all_windows:
    print(window)
