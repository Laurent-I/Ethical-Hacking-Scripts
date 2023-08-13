import subprocess

def list():
    subprocess.run(['iwconfig'])

def stop(interface):
    subprocess.run(['sudo', 'airmon-ng', 'stop', interface])

def start_network():
    subprocess.run(['sudo', 'service', 'NetworkManager', 'start'])


def main():
    list()
    interface = input('Enter the interface name: ')
    stop(interface)
    start_network()
    print(f'******************Interface {interface} is now in Managed mode************************')


if __name__ == '__main__':
    main()