import subprocess

def run_aircrack(captured_file, wordlist_filename):
    command = ['aircrack-ng', captured_file, '-w', wordlist_filename]

    print("Running aircrack-ng...")
    try:
        subprocess.run(command, check=True)
        print("Aircrack-ng completed.")
    except subprocess.CalledProcessError:
        print("Aircrack-ng failed.")

def main():
    captured_file = input("Enter the path to the captured file: ")
    wordlist_filename = input("Enter the path to the wordlist file: ")

    run_aircrack(captured_file, wordlist_filename)

if __name__ == '__main__':
    main()
