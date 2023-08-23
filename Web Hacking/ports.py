import socket

def check_ports(host, port_list):
    open_ports = []
    
    for port in port_list:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((host, port))
                open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass
    
    return open_ports

def main():
    host = input("Enter the target host: ")
    port_range = input("Enter the port range (e.g., 80-443): ")
    start_port, end_port = map(int, port_range.split('-'))
    port_list = list(range(start_port, end_port + 1))
    
    open_ports = check_ports(host, port_list)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

if __name__ == '__main__':
    main()
