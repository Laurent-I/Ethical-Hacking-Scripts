import keyboard
import subprocess
import os

def is_mate_screensaver_running():
    # Check if the mate-screensaver process is running
    processes = subprocess.run(["pgrep", "mate-screensaver"], stdout=subprocess.PIPE, text=True)
    return processes.returncode == 0

def start_mate_screensaver():
    # Start mate-screensaver in the background
    subprocess.Popen(["mate-screensaver", "--no-daemon"])

def lock_screen(e):
    if not is_mate_screensaver_running():
        start_mate_screensaver()

    # Use the mate-screensaver-command to lock the screen
    subprocess.run(["mate-screensaver-command", "-l"])

def main():
    # Listen for the "Insert" key press event
    keyboard.on_press_key("insert", lock_screen)

    print("Press 'Insert' to lock the screen. Press 'Esc' to exit.")
    keyboard.wait("esc")  # Wait for the "Esc" key to exit

if __name__ == "__main__":
    main()
