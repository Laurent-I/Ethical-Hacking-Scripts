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
    print("3. Wi-Fi Sniffer")
    print("4. Deauthentication Attack")
    print("5. Fake Authentication Attack")
    print("6. WEP Craking (busy network)")
    print("7. WEP Craking (non-busy network)")
    print("8. Launch ARP Replay Attack")

    print('***********************************************************************************************************************')

    choice = input("Enter the number of the script you want to run: ")

    if choice == '1':
        run_script("stop-monitor-mode.py")
    elif choice == '2':
        run_script("wifi-interface-sniffer.py")
    elif choice == '3':
        run_script("wifi-sniffer.py")
    elif choice == '4':
        run_script("deauth-attack.py")
    elif choice == '5':
        run_script("fake-auth.py")
    elif choice == '6':
        run_script("wep-busy.py")
    elif choice == '7':
        run_script("wep.py")
    elif choice == '8':
        run_script("arpreplay-attack.py")  
    else:
        print("Invalid choice. Please enter a valid number.")

if __name__ == '__main__':
    main()
