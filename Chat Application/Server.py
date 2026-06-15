import socket

# Create a socket
server_socket = socket.socket()
server_socket.bind(('localhost', 12345))  # Bind to localhost and port 12345
server_socket.listen(1)  # Listen for 1 connection

print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print("Connected with:", addr)

while True:
    data = conn.recv(1024).decode()
    if data.lower() == 'bye':
        print("Client ended chat.")
        break
    print("Client:", data)
    msg = input("Server: ")
    conn.send(msg.encode())
    if msg.lower() == 'bye':
        break

conn.close()
server_socket.close()
