from umqtt.simple import MQTTClient
import network, time, random

ssid = "Your_SSID"
password = "Your_PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    time.sleep(1)

broker = "192.168.1.10"
client = MQTTClient("esp32_random", broker)
client.connect()

while True:
    num = random.randint(0, 100)
    client.publish("iot/random", str(num))
    print("Published random number:", num)
    time.sleep(3)
