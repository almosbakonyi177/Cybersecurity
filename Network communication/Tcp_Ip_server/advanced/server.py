import socket

dictionary=dict()
dictionary["Apple"]="Red, shiny"
dictionary["Window"]="Nice, clean"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 6500))

# Only 2 clients can connect to the server
serverSocket.listen(2)

while True:

    authenticated=False
    client_socket, address = serverSocket.accept()
    print("Client requested connection from", address)

    while True:
        incomingData=client_socket.recv(2048)
        incomingData=incomingData.decode('utf-8')

        if not incomingData or incomingData=='END':
            break
        

        if not authenticated:

            # If the client is not authenticated yet,
            # the client should send the password or connection gets closed

            if incomingData=="SECRET":
                authenticated=True
                client_socket.sendall(b"Successful authentication")
                print("Successful authentication")

            else:
                client_socket.sendall(b"Failed authentication")
                print("Failed authentication")
                client_socket.close()
                break

        else:
            print("Received request for:", incomingData)

            if incomingData in dictionary:
                client_socket.sendall((dictionary[incomingData]).encode('utf-8'))
            else:
                client_socket.sendall(b"No item found")

    print("Connection closed with client", address)
    client_socket.close()