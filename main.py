import os

def run_script(script_name):
    os.system(f"python3 {script_name}")

def check_monitor_mode():
    return os.path.exists("monitor_mode.flag")

def main():
    if not check_monitor_mode():
        print("Monitor mode must be started before running other scripts.")
        return

    print("Available scripts:")
    print("1. Stop Monitor Mode")
    print("2. Sniff Packets")

    print('***********************************************************************************************************************')

    choice = input("Enter the number of the script you want to run: ")

    if choice == '1':
        run_script("stop-monitor-mode.py")
    elif choice == '2':
        run_script("packet-sniff.py")
    else:
        print("Invalid choice. Please enter a valid number.")

if __name__ == '__main__':
    main()
