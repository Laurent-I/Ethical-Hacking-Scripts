import subprocess

def list():
    subprocess.run(['iwconfig'])

def sniff(interface, band=None):
    command = ['sudo', 'airodump-ng', interface]
    if band:
        command.extend(['--band', band.lower()])
    subprocess.run(command)

def main():
    print('***************************LISTING THE AVAILABLE INTERFACES**************************')
    list()
    print('***********************************************************************************************************************')
    interface = input("Enter the interface: ")
    band = input("On which band do you want to sniff? (2.4G or 5G or both, press Enter for default 2.4G): ").strip().lower()

    if band == '2.4g':
        band_arg = None
    elif band == '5g':
        band_arg = 'a'
    elif band == 'both':
        band_arg = 'abg'
    elif band == '':
        band_arg = None
    else:
        print("Invalid band selection. Please choose from: 2.4G, 5G, both.")
        return
    
    print(f'******************Sniffing on {band} band***************')
    sniff(interface, band_arg)

if __name__ == '__main__':
    main()
