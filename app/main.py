# app/main.py
import sys
from app.run_original import run_original

# ----- küçük yardımcılar -----
def ask_port(prompt: str, default: int) -> int:
    while True:
        raw = input(f"{prompt} [{default}]: ").strip()
        if raw == "":
            return default
        try:
            p = int(raw)
            if 1 <= p <= 65535:
                return p
            print("Port 1-65535 araliğinda olmali.")
        except ValueError:
            print("sadece sayi gir.")

def ask_str(prompt: str, default: str) -> str:
    raw = input(f"{prompt} [{default}]: ").strip()
    return raw or default


def menu_main() -> str:
    return input("""
=== ORIGINAL SCRIPTS ===
[1] Machine Information (01..08)
[2] Echo Tests (TCP / UDP)
[3] SNTP Time Check (11.py)
[4] Simple Chat (03a / 03b)
[0] Exit
Choice: """).strip()


def menu_machine_info():
    while True:
        choice = input("""
-- Machine Information (01..08) --
[1] 01.py
[2] 02.py
[3] 03.py
[4] 04.py
[5] 05.py
[6] 06.py
[7] 07.py
[8] 08.py
[0] Back
Choice: """).strip()

        if   choice == "1": run_original("01.py")
        elif choice == "2": run_original("02.py")
        elif choice == "3": run_original("03.py")
        elif choice == "4": run_original("04.py")
        elif choice == "5": run_original("05.py")
        elif choice == "6": run_original("06.py")
        elif choice == "7": run_original("07.py")
        elif choice == "8": run_original("08.py")
        elif choice == "0": break
        else: print("Invalid choice.")


def menu_echo():
    while True:
        choice = input("""
-- Echo Tests --
[1] TCP  (13-server-tcp.py / 13-client-tcp.py)
[2] UDP  (12-server-udp.py / 12-client-udp.py)
[0] Back
Choice: """).strip()

        if choice == "1":
            sub  = input("[1] Server  /  [2] Client: ").strip()
            port = ask_port("Port", 9900)
            if   sub == "1":
                run_original("13-server-tcp.py", [f"--port={port}"])
            elif sub == "2":
                run_original("13-client-tcp.py", [f"--port={port}"])
            else:
                print("Invalid choice.")
        elif choice == "2":
            sub  = input("[1] Server  /  [2] Client: ").strip()
            port = ask_port("Port", 9991)
            if   sub == "1":
                run_original("12-server-udp.py", [f"--port={port}"])
            elif sub == "2":
                run_original("12-client-udp.py", [f"--port={port}"])
            else:
                print("Invalid choice.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def menu_sntp():
    while True:
        choice = input("""
-- SNTP Time Check --
[1] 11.py  (Raw SNTP)
[0] Back
Choice: """).strip()

        if   choice == "1": run_original("11.py")
        elif choice == "0": break
        else: print("Invalid choice.")

# ----- chat -----
def menu_chat():
    while True:
        choice = input("""
-- Simple Chat (TCP) --
[1] Chat Server (03a-SimpleChatServer.py)
[2] Chat Client (03b-SimpleChatClient.py)
[0] Back
Choice: """).strip()

        if choice == "1":
            port = ask_port("Server port", 8800)
            run_original("03a-SimpleChatServer.py", [f"--port={port}"])
        elif choice == "2":
            name = ask_str("Your name", "client1")
            port = ask_port("Server port", 8800)
            run_original("03b-SimpleChatClient.py", [f"--name={name}", f"--port={port}"])
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        sel = menu_main()

        if   sel == "1": menu_machine_info()
        elif sel == "2": menu_echo()
        elif sel == "3": menu_sntp()
        elif sel == "4": menu_chat()
        elif sel == "0":
            print("Bye!"); sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
