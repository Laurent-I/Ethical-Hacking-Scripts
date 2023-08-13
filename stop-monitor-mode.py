import subprocess

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

def main():
    list_wireless_networks()
    interface = input("Enter the Wi-Fi interface name: ")
    interface_down(interface)
    stop_monitor_mode(interface)
    interface_up(interface)
    start_network()
    print(f'*****************Putting {interface} into managed mode*********************')
    list_wireless_networks()


if __name__ == '__main__':
    main()


