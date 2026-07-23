import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to server, type END to exit\n")
clientSocket.connect(('127.0.0.1', 6500))
print("Connected")

while True:
    message = input("Message to the server:")
    clientSocket.sendall(message.encode("utf-8"))

    if message=="END":
        break
    print("Sent")
    server_response = clientSocket.recv(2048)
    print("Server Response:",server_response)
clientSocket.close()