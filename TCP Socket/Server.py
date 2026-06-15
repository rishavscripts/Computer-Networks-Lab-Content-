import socket

# Create socket
server = socket.socket()
server.bind(('localhost', 12345))   # Bind to localhost and port 12345
server.listen(1)                    # Listen for 1 connection

print("Server is waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)

# Receive filename
filename = conn.recv(1024).decode()

try:
    with open(filename, 'r') as f:
        data = f.read()
    conn.send(data.encode())        # Send file contents
except FileNotFoundError:
    conn.send(b"File not found!")   # Send error message

conn.close()
server.close()
