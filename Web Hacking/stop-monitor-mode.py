import subprocess
import os

# List all wireless networks
def list_wireless_networks():
    subprocess.run(['iwconfig'])

# Put interface down
def interface_down(interface):
    subprocess.run(['sudo', 'ifconfig', interface, 'down'])

# Put interface up
def interface_up(interface):
    subprocess.run(['sudo', 'ifconfig', interface, 'up'])

# Put the Wi-Fi adapter into managed mode
def stop_monitor_mode(interface):
    subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'managed'])

def start_network():
    subprocess.run(['sudo', 'systemctl', 'start', 'NetworkManager'])

def remove_monitor_flag():
    if os.path.exists("monitor_mode.flag"):
        os.remove("monitor_mode.flag")
        print("Monitor mode flag has been removed.")
    else:
        print("Monitor mode flag not found.")

def main():
    print('***************************LISTING THE AVAILABLE INTERFACES**************************')
    list_wireless_networks()
    print('***********************************************************************************************************************')

    interface = input("Enter the Wi-Fi interface name: ")
    interface_down(interface)
    stop_monitor_mode(interface)
    interface_up(interface)
    start_network()
    remove_monitor_flag()
    print(f'******************INTERFACE {interface} IS NOW IN MANAGED MODE************************')
    list_wireless_networks()


if __name__ == '__main__':
    main()


