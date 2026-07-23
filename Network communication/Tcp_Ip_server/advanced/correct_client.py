import socket


def isConnected(sock:socket.socket)->bool:
    try:
        clientSocket.sendall(b'hello')
    except:
        return False
    
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to server, type END to exit\n")
clientSocket.connect(('127.0.0.1', 6500))

clientSocket.sendall(b"SECRET")

server_response = clientSocket.recv(2048).decode('utf-8')
print(server_response)

if server_response=="Successful authentication":

    while True:
        message = input("Message to the server:")
        clientSocket.sendall(message.encode("utf-8"))

        if message=="END":
            break
        print("Sent")
        server_response = clientSocket.recv(2048)
        server_response=server_response.decode('utf-8')
        print("Server Response:",server_response)
    clientSocket.close()