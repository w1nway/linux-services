#!/usr/bin/env python3

import socket
from datetime import datetime

def main():
    sock = socket.socket()
    sock.bind(("0.0.0.0", 1303))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        current_datetime = datetime.now().strftime("%d.%m.%Y %H:%M")
        conn.send(current_datetime.encode("UTF-8"))
        conn.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit
