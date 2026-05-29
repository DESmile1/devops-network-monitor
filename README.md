# Infrastructure & Network Service Monitor

A lightweight, secure Python-based automation tool designed to monitor server availability and verify web service statuses.

## Features
* **Safe ICMP Checks (Ping):** Utilizes secure `subprocess.run` architecture to safely verify host availability without shell injection risks.
* **TCP Port Inspection:** Leverages Python's native `socket` module to check if port 80 (HTTP) is open, confirming active web services (Nginx/Apache).
* **Automated Pipeline:** Wrapped in a `Makefile` for fast, standardized execution and testing.
* **Unit Tested:** Built-in test coverage using Python's `unittest` framework to guarantee configuration integrity.

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/DESmile1/Devops-Network-Monitor
cd devops-network-monitor
```

### 2. Run the Monitor
You don't need to type long commands:
```bash
make run
```

### 3. Run Unit Tests
Trigger the automated test runner:
```bash
make test