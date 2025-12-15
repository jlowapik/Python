import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: client.connect(('127.0.0.1', 9000))
    print('connected')

    while True:
        message = input('>>>>>>>')
        if message.lower() == 'exit':
            break

        client.sendall(message.encode())
        response = client.recv(1024)
        print('Server:', response.decode)


start_client()