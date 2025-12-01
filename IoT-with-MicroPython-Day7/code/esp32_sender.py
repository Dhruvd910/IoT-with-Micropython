import network
import time
import ujson
from umqtt.simple import MQTTClient
import random

# MQTT Broker (Raspberry Pi IP)
BROKER = "192.168.137.150"  # change to your Pi WiFi IP
TOPIC = b"edge/data"

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("YourHotspotSSID", "YourHotspotPassword")

print("Connecting WiFi...")
while not wifi.isconnected():
    time.sleep(1)

print("Connected:", wifi.ifconfig())

# MQTT client
client = MQTTClient("ESP32_Sender", BROKER)
client.connect()

while True:
    value = random.randint(10, 100)  # fake sensor value

    payload = {
        "timestamp": time.time(),
        "value": value
    }

    client.publish(TOPIC, ujson.dumps(payload))
    print("Sent:", payload)

    time.sleep(2)
