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
s.send(b"Hello Raspberry Pi!")
s.close()
print("Message sent successfully!")
