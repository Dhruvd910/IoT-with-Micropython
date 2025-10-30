# Day 3 – Hands-on Experiments

## 🧩 Experiment 1: Connect ESP32 to Wi-Fi

```python
import network
import time

ssid = "Your_SSID"
password = "Your_PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to Wi-Fi...", end="")
while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)

print("\nConnected!")
print("IP Config:", wifi.ifconfig())
```

---

## 🧩 Experiment 2: Create Socket Server on Raspberry Pi

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(1)

print("Server listening on port 5000...")

conn, addr = server.accept()
print("Connected by:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())

conn.close()
server.close()
```

---

## 🧩 Experiment 3: ESP32 Sends Message to Raspberry Pi

```python
import socket
import network
import time

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Your_SSID", "Your_PASSWORD")
while not wifi.isconnected():
    time.sleep(1)

# Send message to Raspberry Pi server
server_ip = "192.168.1.10"  # Replace with Pi IP
port = 5000

s = socket.socket()
s.connect((server_ip, port))
s.send(b"Hello from ESP32!")
s.close()
print("Message sent successfully!")
```
