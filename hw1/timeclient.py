import socket

def main():
    ip_from_user = input("Enter IP address of server: ")
    app_socket = socket.socket()
    app_socket.connect((ip_from_user, 1303))

    current_datetime = app_socket.recv(1024)
    print(current_datetime.decode("UTF-8"))
    app_socket.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit
