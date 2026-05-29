import subprocess
import socket

servers = ["8.8.8.8", "127.0.0.1", "google.com"]

def check_infastructure():

    print("Starting infastructure check... \n")

    for ip in servers:
        responce_ping = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            )
        
        if responce_ping.returncode == 0:
            ping_status = "Online"

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result_port = sock.connect_ex((ip, 80))
            
            if result_port == 0:
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
    check_infastructure()