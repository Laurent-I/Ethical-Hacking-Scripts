#!/usr/bin/env python3

import subprocess

def sniff_packets():
    subprocess.run(['python3', 'wifi-sniffer.py'])

def deauth_attack():
    subprocess.run(['python3', 'deauth-attack.py'])

def main():
    print('*****Remember to run with admin privileges******')
    print("Select an option:")
    print("1. Sniff packets and write to cap file")
    print("2. Perform deauthentication attack")

    option = input()

    if option == '1':
        sniff_packets()
    elif option == '2':
        deauth_attack()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
