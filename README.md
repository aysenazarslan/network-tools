# 🛰️ Network Tools Project (Python)

This project demonstrates core network programming concepts using Python sockets.  
It was developed as part of a university assignment for the **Network Programming** course.

The project includes multiple modules such as TCP/UDP echo communication, machine network information, SNTP time synchronization, and a multi-client chat application.

---

## 📁 Project Structure

network-tools/
│
├── app/
│ ├── main.py → Main menu (modular execution)
│ ├── run_original.py → Helper script to run modules
│ ├── init.py
│ └── original/
│ ├── 01.py → Machine Info
│ ├── 02.py → DNS Resolve
│ ├── 03.py → IPv4 Pack/Unpack
│ ├── 03a-SimpleChatServer.py → TCP Chat Server
│ ├── 03b-SimpleChatClient.py → TCP Chat Client
│ ├── 04.py → TCP/UDP Common Service Ports
│ ├── 05.py → Socket Timeout Demo
│ ├── 06.py → Socket Error Handling
│ ├── 07.py → SO_REUSEADDR & Socket Options
│ ├── 08.py → Network Interface Listing
│ ├── 11.py → SNTP Time Check (UDP)
│ ├── 12-server-udp.py → UDP Echo Server
│ ├── 12-client-udp.py → UDP Echo Client
│ ├── 13-server-tcp.py → TCP Echo Server
│ ├── 13-client-tcp.py → TCP Echo Client
│
├── screenshots/ → Screenshots for test results
└── requirements.txt

---

## ⚙️ Setup Instructions

### ✅ 1) Install Python 3.10+
Verify installation:
```bash
python --version

python -m venv .venv
.venv\Scripts\Activate.ps1
python -m app.main

🖥️ Machine Information (01–08)

Displays:

Hostname

IP Address

Network Interfaces

DNS resolving

Socket options

Blocking / non-blocking behavior
