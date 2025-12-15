import socket
import threading

class ClientHandler(threading.Thread):

    def __init__(self, client_socket, client_address):
        super().__init__(daemon=True)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        print(f'client connected {self.client_address}')

        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    print(f'client disconected {self.client_address}')
                    break
                message = data.decode().strip()
                print(f'[{self.client_address}]: {message}')

                response = f'server recieved: {message}'
                self.client_socket.sendall(response.encode())
        except ConnectionResetError:
            print(f'conection lost: {self.client_address}')
        except Exception as e:
            print(f'error wit {self.client_address}" {e}')
        finally:
            self.client_socket.close()
            print(f'connection closed: {self.client_address}')

class MultiThread:
    def __init__(self, host='0.0.0.0', port=9000) -> None:
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f'server started on {self.host}:{self.port}')

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                handler = ClientHandler(client_socket, client_address)
                handler.start()
        except KeyboardInterrupt:
            print(f'server off')
        
        finally:
            self.server_socket.close

server = MultiThread(port=9000)
server.start()