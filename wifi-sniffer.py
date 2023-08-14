import subprocess

def run_airodump(bssid, channel, file_to_write, interface):
    print("Running airodump-ng command...")
    command = ['airodump-ng', '--bssid', bssid, '--channel', channel, '--write', file_to_write, interface]
    subprocess.run(command)
    print("airodump-ng command completed.")

def main():
    print("Wi-Fi Sniffer Script")
    print("--------------------")

    bssid = input("Enter the target BSSID (MAC address): ")
    channel = input("Enter the channel number: ")
    file_to_write = input("Enter the name of the file to write captured data: ")
    interface = input("Enter the Wi-Fi interface name: ")

    run_airodump(bssid, channel, file_to_write, interface)

if __name__ == '__main__':
    main()
