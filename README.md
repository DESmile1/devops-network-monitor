# Network & Service Monitor (Python)

A simple and effective Python script for monitoring server availability and checking the status of web services.

## Features
* **ICMP Check (Ping):** Checks for a network connection to the host.
* **TCP Port Check:** Checks whether port 80 (HTTP) is open to confirm that the web server (Nginx/Apache) is working.
* **Clean Output:** Uses stream redirection to `/dev/null` for clean console output.

## How to run
1. Clone the repository.
2. Run via Python 3:
```bash
python3 monitor.py
