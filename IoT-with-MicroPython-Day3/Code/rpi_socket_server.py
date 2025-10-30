import socket

HOST = ''           # Listen on all interfaces
PORT = 12345        # Choose any free port

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server started... Listening on port {PORT}")

conn, addr = server.accept()
print("Connection from:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Message from ESP32:", data.decode())

conn.close()
server.close()
