from umqtt.simple import MQTTClient
import network, time

ssid = "Your_SSID"
password = "Your_PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    time.sleep(1)

broker = "192.168.1.10"  # Replace with your Pi IP
client = MQTTClient("esp32_pub", broker)
client.connect()

while True:
    msg = "Hello from ESP32!"
    client.publish("iot/demo", msg)
    print("Published:", msg)
    time.sleep(5)
