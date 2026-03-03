import os
import socket

servers = ["8.8.8.8", "127.0.0.1", "google.com"]

print("Starting infastructure check... \n")

for ip in servers:
    responce = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    if responce == 0:
        ping_status = "Online"

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 80))
        
        if result == 0:
            port_status = "web-servise (port 80) is open"
        else:
            port_status = "web-servise (port 80) is closed"
        sock.close()
    else:
        ping_status = "Server error"
        port_status = "N/A"

    print(f"Server: {ip} - {ping_status} - {port_status}")
    print("-" * 30)

print("\n Infastructure check completed.")
