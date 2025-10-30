import socket, network, time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Your_SSID", "Your_PASSWORD")
while not wifi.isconnected():
    time.sleep(1)

server_ip = "192.168.1.10"  # Replace with your Pi IP
port = 5000

s = socket.socket()
s.connect((server_ip, port))

while True:
    t = time.localtime()
    msg = f"ESP32 Timestamp: {t[3]:02d}:{t[4]:02d}:{t[5]:02d}"
    s.send(msg.encode())
    print("Sent:", msg)
    time.sleep(5)
