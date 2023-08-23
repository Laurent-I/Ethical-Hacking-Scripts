import subprocess
import os

def list():
    subprocess.run(['iwconfig'])

def stop(interface):
    subprocess.run(['sudo', 'airmon-ng', 'stop', interface])

def start_network():
    subprocess.run(['sudo', 'service', 'NetworkManager', 'start'])

def remove_monitor_flag():
    if os.path.exists("monitor_mode.flag"):
        os.remove("monitor_mode.flag")
        print("Monitor mode flag has been removed.")
    else:
        print("Monitor mode flag not found.")


def main():
    print('***************************LISTING THE AVAILABLE INTERFACES**************************')
    list()
    print('***********************************************************************************************************************')

    interface = input('Enter the interface name: ')
    stop(interface)
    start_network()
    remove_monitor_flag()
    print(f'******************INTERFACE {interface} IS NOW IN MANAGED MODE************************')


if __name__ == '__main__':
    main()