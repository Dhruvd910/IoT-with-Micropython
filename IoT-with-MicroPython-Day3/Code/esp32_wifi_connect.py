import network
import time

# Wi-Fi credentials
ssid = 'ALICE'
password = '9811255833'

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to Wi-Fi...")
while not wifi.isconnected():
    time.sleep(1)
    print(".", end="")

print("\nConnected successfully!")
print("ESP32 IP Address:", wifi.ifconfig()[0])
