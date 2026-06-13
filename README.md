# KNX Cleaner & Updater

KNX Cleaner & Updater is a Windows desktop utility that automates system maintenance — cleanup, optimization, and app management — through a clean CustomTkinter GUI.

## Features

- **Tab navigation** — Main tab for system functions, Todo tab for personal task tracking
- **Todo panel** — Add tasks, check off to move to Done, delete completed items (persisted to `logs/todo.json`)
- **Run All / Run Selected / Stop All** — full control over which functions execute
- **Real-time console output** — streaming stdout from every function into the in-app console
- **Last run timestamp** — greeting shows how long since the last maintenance run

## Functions

### Cleanup
| Function | Description |
|---|---|
| Clean Temp | Runs temp cleanup batch script |
| Clean Prefetch | Clears `C:\Windows\Prefetch` |
| Clean Log Files | Runs log folder cleaner script |
| Empty Recycle Bin | Empties recycle bin via PowerShell |
| Clear Event Logs | Clears Application, System, Security event logs |
| Clear Windows Update Cache | Stops WU service, clears `SoftwareDistribution\Download`, restarts service |
| Flush DNS Cache | `ipconfig /flushdns` |
| Open Disk Cleanup | Opens `cleanmgr.exe` |
| Open Disk Defragmentation | Opens `dfrgui.exe` |

### Optimization
| Function | Description |
|---|---|
| Set High Performance Plan | Switches power plan to High Performance |
| Reset Network Stack | Winsock reset + IP stack reset + release/renew/flushdns |
| Optimize Drives (SSD Trim) | `defrag /C /L` — retrim on all SSD drives |
| Windows Optimize | Runs Windows Optimization batch script |
| Bcdedit Optimizer | Runs Bcdedit optimization script |
| Run SFC Scan | `sfc /scannow` with streamed output |
| Run DISM RestoreHealth | `DISM /Online /Cleanup-Image /RestoreHealth` with streamed output |
| Close Apps (Spotify) | Force-kills Spotify |

### Updates
| Function | Description |
|---|---|
| Run Winget Update | Opens CMD and runs `winget upgrade --all` |
| Open Windows Update | Opens `ms-settings:windowsupdate` |
| Open MS Store | Opens Microsoft Store |
| Open Web Browser with Links | Opens ASUS + AMD driver download pages |

### Launchers
| Function | Description |
|---|---|
| Run Learix FPS | Runs Learix FPS optimization script |
| Open Adobe Creative Cloud | Opens Adobe CC |
| Open Word | Opens Microsoft Word |
| Open Nvidia App | Opens NVIDIA App |
| Open SignalRGB | Opens SignalRGB |
| Open CCleaner | Opens CCleaner |

## Installation

1. Clone this repository
2. Install Python 3.10+
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

> **Note:** The app must be run as Administrator. It will prompt for elevation automatically on launch.

## Usage

- **Run All** — executes all functions sequentially
- **Run Selected** — check boxes next to desired functions, then click Run Selected
- **Stop All** — sets a stop event; functions that check it will halt
- **Todo tab** — manage a personal task list alongside your maintenance routine

## Requirements

- Windows 10/11
- Python 3.10+
- `customtkinter`, `pygetwindow`, `pyautogui` (see `requirements.txt`)

## Version History

| Version | Date | Highlights |
|---|---|---|
| 6.0 | June 2026 | Todo panel, tab navigation, 7 new system functions, UI fixes |
| 5.0 | August 2024 | GUI overhaul, CustomTkinter, background threading |

## License

MIT License
