# Wi-Fi Scripts for Monitor Mode and Packet Sniffing

This repository contains Python scripts to manage Wi-Fi monitor mode and perform packet sniffing using aircrack-ng tools.

## Getting Started

### Prerequisites

- You need to have a Linux-based operating system (e.g., Kali Linux, Parrot OS) to run these scripts.
- Make sure you have `aircrack-ng` and `iwconfig` tools installed. You can install them using package managers like `apt` or `yum`.

### Cloning the Repository

```bash
git clone https://github.com/Laurent-I/Ethical-Hacking-Scripts.git
cd Ethical-Hacking-Scripts
```
## Starting Monitor Mode
Run the `start-monitor-mode.py` or `start-monitor-mode-airmon.py` to use the airmon command script to put your Wi-Fi adapter into monitor mode:

```bash
python3 start-monitor-mode.py
python3 start-monitor-mode-airmon.py
```

This script will start monitor mode and create a flag file monitor_mode.flag.

## Running Other Scripts
Use the `main.py` script to choose and run other available scripts. This script allows you to run different actions like stopping monitor mode and sniffing packets:

```bash
python3 main.py
```

Follow the prompts to select the action you want to perform.
Or you can run each script individually by `python3 {script_name}`

## Notes
  - These scripts are intended for educational and ethical use only. Ensure you have proper authorization before using them.
  - Modify the scripts as needed to match your system configuration and requirements.

**Happy Hacking**
