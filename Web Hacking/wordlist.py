import subprocess

def generate_passwords(min_length, max_length, characters, pattern, output_filename):
    command = ['crunch', str(min_length), str(max_length), characters]
    
    if pattern:
        command.extend(['-t', pattern])
    
    command.extend(['-o', output_filename])

    print("Generating passwords using Crunch...")
    try:
        subprocess.run(command, check=True)
        print("Password generation completed.")
    except subprocess.CalledProcessError:
        print("Password generation failed.")

def main():
    min_length = int(input("Enter minimum password length: "))
    max_length = int(input("Enter maximum password length: "))
    characters = input("Enter characters to include in passwords: ")
    pattern = input("Enter pattern for passwords (use @ to indicate characters, press Enter if none): ")
    output_filename = input("Enter output filename: ")

    generate_passwords(min_length, max_length, characters, pattern, output_filename)

if __name__ == '__main__':
    main()
