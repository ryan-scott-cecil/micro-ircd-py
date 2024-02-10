import socket
import threading

def main():
    server = IRCServer()
    server.server.listen()


    return print('working')

class IRCServer:
    def __init__(self, host='localhost', port=6667):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        def handle_client(self, client):
            while True:
                try:
                    message = client.recv(2048).decode('utf-8')
                    if not message:
                        break
            
                    # Parse the message and extract the command and parameters
                    parts = message.strip().split(' ')
                    command = parts[0]
                    params = parts[1:]
            
                    if command == 'PRIVMSG':
                        target = params[0]
                        message = ' '.join(params[1:])
                        # Respond to the PRIVMSG command
                        client.send(f":{self.host} PRIVMSG {target} :{message}\n".encode('utf-8'))
                except Exception as e:
                    print(f"Error handling client: {e}")
                    break


main()
