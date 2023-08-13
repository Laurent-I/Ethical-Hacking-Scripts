import subprocess

def list():
    subprocess.run(['iwconfig'])

def check():
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])

def start(interface):
    subprocess.run(['sudo', 'airmon-ng', 'start', interface])


def main():
    list()
    interface = input('Enter the interface name: ')
    check()
    start(interface)
    print(f'******************Interface {interface} is now in Monitor mode************************')


if __name__ == '__main__':
    main()