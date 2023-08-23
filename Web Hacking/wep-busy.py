import os
import subprocess

def find_captured_file(root_dir, filename):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

def decrypt_captured_data():
    print('Note: Remember to run airodump-ng to capture and write data')
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
    decrypt_captured_data()

if __name__ == '__main__':
    main()
