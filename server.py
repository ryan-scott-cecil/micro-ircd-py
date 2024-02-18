# from client import Client
# from channel import Channel

import socket
import threading
from typing import Any, Collection, Dict, List, Optional, Sequence, Set
import sys

class Server:
    def __init__(self, host='localhost', port=6667):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def start(self):
        print(f"Server is listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Accepted connection from {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(2048)
                if not data:
                    break

                try:
                    message = data.decode('utf-8')
                except UnicodeDecodeError:
                    # Fallback to ISO-8859-1 if UTF-8 decoding fails
                    message = data.decode('ISO-8859-1')

                print(f"Received message: {message}")
                    
            except Exception as e:
                print(f"Error handling client: {e}")
                break

    def print_error(self, message):
        sys.stderr.write(f"{message}\n")
