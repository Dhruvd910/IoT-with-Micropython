import socket, datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(1)
print("Server listening on port 5000...")

conn, addr = server.accept()
print("Connected by:", addr)

with open("log.txt", "a") as log:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | From {addr[0]} | {message}\n"
        print(entry.strip())
        log.write(entry)

conn.close()
server.close()
