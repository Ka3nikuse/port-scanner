import socket

target = input("Enter the IP address to scan: ")
ports = range(1, 1025)

print(f"Scanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open.")
    s.close()