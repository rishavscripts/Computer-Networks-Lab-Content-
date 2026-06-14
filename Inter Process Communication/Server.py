import time
import os

SERVER_FILE = "server_request.txt"
CLIENT_FILE = "client_reply.txt"

print("Server is running... waiting for client request.")

while True:
    # Wait until client writes a request
    while not os.path.exists(SERVER_FILE):
        time.sleep(1)

    with open(SERVER_FILE, "r") as f:
        filename = f.read().strip()

    if filename == "exit":
        print("Server shutting down.")
        break

    print(f"Client requested file: {filename}")

    try:
        with open(filename, "r") as f:
            file_contents = f.read()
    except FileNotFoundError:
        file_contents = "Error: File not found."

    # Write reply for client
    with open(CLIENT_FILE, "w") as f:
        f.write(file_contents)

    # Remove request file so next request can come
    os.remove(SERVER_FILE)

    print("Reply sent to client.")
