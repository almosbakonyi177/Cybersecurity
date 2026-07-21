import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to server")
serverSocket.connect(('127.0.0.1', 6500))
print("Connected")

serverSocket.sendall(b"Hello")
print("Sent")
server_response = serverSocket.recv(2048)
print("Server Response:",server_response)
serverSocket.close()