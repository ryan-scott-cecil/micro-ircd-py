from server import Server


import socket
import threading

def main():
    server = Server()
    fqdn = socket.getfqdn()
    print(f" fqdn is: {fqdn}")
    try:
        server.start()
    except KeyboardInterrupt:
        server.print_error("Server Interrupted by sysadmin")

    return print('working')

if __name__ == "__main__":
    main()
