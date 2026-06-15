import socket

# Create a socket
client_socket = socket.socket()
client_socket.connect(('localhost', 12345))  # Connect to server

print("Connected to server. Type 'bye' to exit.")

while True:
    msg = input("Client: ")
    client_socket.send(msg.encode())
    if msg.lower() == 'bye':
        break
    data = client_socket.recv(1024).decode()
    print("Server:", data)
    if data.lower() == 'bye':
        break

client_socket.close()
