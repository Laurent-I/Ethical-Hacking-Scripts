import subprocess

def list():
    subprocess.run(['iwconfig'])

def check():
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])

def start(interface):
    subprocess.run(['sudo', 'airmon-ng', 'start', interface])


def main():
    print('***************************LISTING THE AVAILABLE INTERFACES**************************')
    list()
    print('***********************************************************************************************************************')

    interface = input('Enter the interface name: ')
    check()
    start(interface)
    print(f'******************INTERFACE {interface} IS NOW IN MONITOR MODE WITH A FLAG************************')
    # Create the flag file
    with open("monitor_mode.flag", "w") as flag_file:
        flag_file.write("Monitor mode has been started.")


if __name__ == '__main__':
    main()