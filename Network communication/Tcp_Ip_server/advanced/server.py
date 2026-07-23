import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 6500))

# Only 2 clients can connect to the server
serverSocket.listen(2)

while True:
    client_socket, address = serverSocket.accept()
    print("Client connected from", address)
    while True:
        incomingData=client_socket.recv(2048)
        if not incomingData or incomingData.decode('utf-8')=='END':
            break
        print("Received from client:", incomingData)
        client_socket.sendall(b"Hello back")
    client_socket.close()