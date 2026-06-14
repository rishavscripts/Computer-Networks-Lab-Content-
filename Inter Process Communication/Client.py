import time
import os

SERVER_FILE = "server_request.txt"
CLIENT_FILE = "client_reply.txt"

filename = input("Enter the filename you want to read: ")

# Send request
with open(SERVER_FILE, "w") as f:
    f.write(filename)

# Wait for reply
while not os.path.exists(CLIENT_FILE):
    time.sleep(1)

with open(CLIENT_FILE, "r") as f:
    response = f.read()

print("\n--- File Contents ---")
print(response)
print("---------------------")

# Clean up
os.remove(CLIENT_FILE)
