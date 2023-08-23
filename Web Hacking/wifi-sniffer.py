import os
import subprocess

def create_data_folder():
    folder_name = "captured_data"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def run_airodump(bssid, channel, folder_name, interface):
    print("Running airodump-ng command...")
    command = ['airodump-ng', '--bssid', bssid, '--channel', channel, '--write', os.path.join(folder_name, 'captured'), interface]
    subprocess.run(command)
    print("airodump-ng command completed.")

def main():
    print("Wi-Fi Sniffer Script")
    print("--------------------")

    bssid = input("Enter the target BSSID (MAC address): ")
    channel = input("Enter the channel number: ")
    
    folder_name = create_data_folder()
    
    interface = input("Enter the Wi-Fi interface name: ")

    run_airodump(bssid, channel, folder_name, interface)

if __name__ == '__main__':
    main()

