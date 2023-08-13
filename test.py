import subprocess

# List all wireless networks
def list_wireless_networks():
    subprocess.run(['iwconfig'])

def main():
    list_wireless_networks()

if __name__ == '__main__':
    main()