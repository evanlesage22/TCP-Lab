from socket import *
from datetime import datetime

# Server setup
serverPort = 8008
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)  # Single-threaded, accepts one client at a time

print(f"Server listening on port {serverPort}...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}") # Client's IP address

    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break

        print(f"Received: {data}")

        if data.startswith("HELO"):
            client_name = data.split(" ")[1] if len(data.split(" ")) > 1 else "Unknown"
            response = f"Hello pleased to meet you."
        elif data == "REQTIME":
            response = datetime.now().strftime("%H:%M:%S")
        elif data == "REQDATE":
            response = datetime.now().strftime("%Y-%m-%d")
        elif data.startswith("ECHO"):
            response = data[5:]  # Everything after "ECHO "
        elif data == "REQIP":
            response = addr[0]  # Client's IP address
        elif data == "BYE":
            response = "See ya later!"
            connectionSocket.send(response.encode())
            connectionSocket.close()
            print("Connection closed.")
            break
        else:
            response = "Unknown command."

        connectionSocket.send(response.encode())
