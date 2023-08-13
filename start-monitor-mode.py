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

# Put the Wi-Fi adapter into monitor mode
def enable_monitor_mode(interface):
    subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'monitor'])

# Check and kill interfering processes
def check_and_kill_processes():
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])

def main():
    list_wireless_networks()
    interface = input("Enter the Wi-Fi interface name: ")
    interface_down(interface)
    check_and_kill_processes()
    enable_monitor_mode(interface)
    interface_up(interface)
    print(f'*********************Putting {interface} into monitor mode**************************')
    list_wireless_networks()

if __name__ == '__main__':
    main()
