import socket

# Create socket
client = socket.socket()
client.connect(('localhost', 12345))   # Connect to server

# Ask user for filename
filename = input("Enter filename: ")
client.send(filename.encode())

# Receive and print file contents
data = client.recv(4096).decode()
print("From Server:\n", data)

client.close()
