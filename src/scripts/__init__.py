# Importy z cleaners.py
from .cleaners import (
    run_logfiles,
    clean_prefetch,
    clean_temp,
    defrag_disk,
    disk_cleanup,
    learix_fps,
    flush_dns,
    empty_recycle_bin,
    clear_event_logs,
    clear_update_cache
)

# Importy z launchers.py
from .launchers import (
    open_adobe,
    open_word,
    open_nvidia,
    open_signalrgb,
    open_ccleaner,
    open_win_update,
    open_ms_update
)

# Importy z updaters.py
from .updaters import (
    run_winget,
    open_drivers_link
)

# Importy z optimizers.py
from .optimizers import (
    run_win_optimize,
    run_sfc,
    run_bcdedit,
    close_apps,
    set_high_performance,
    run_dism,
    reset_network,
    optimize_drives
)

functions_mapping = {
    "Run Learix FPS": learix_fps,
    "Open Disk Cleanup": disk_cleanup,
    "Clean Temp": clean_temp,
    "Bcdedit Optimizer": run_bcdedit,
    "Clean Log Files": run_logfiles,
    "Windows Optimize": run_win_optimize,
    "Flush DNS Cache": flush_dns,
    "Empty Recycle Bin": empty_recycle_bin,
    "Clear Event Logs": clear_event_logs,
    "Clear Windows Update Cache": clear_update_cache,
    "Reset Network Stack": reset_network,
    "Optimize Drives (SSD Trim)": optimize_drives,
    "Run SFC Scan": run_sfc,
    "Run DISM RestoreHealth": run_dism,
    "Set High Performance Plan": set_high_performance,
    "Run Winget Update": run_winget,
    "Clean Prefetch": clean_prefetch,
    "Open Disk Defragmentation": defrag_disk,
    "Open Windows Update": open_win_update,
    "Open MS Store": open_ms_update,
    "Open Adobe Creative Cloud": open_adobe,
    "Open Word": open_word,
    "Open SignalRGB": open_signalrgb,
    "Open Nvidia App": open_nvidia,
    "Open Web Browser with Links": open_drivers_link,
    "Close Apps (Spotify)": close_apps,
    "Open CCleaner": open_ccleaner,
}