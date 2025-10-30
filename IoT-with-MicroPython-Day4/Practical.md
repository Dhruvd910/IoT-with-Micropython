# Day 4 – Hands-on Experiments

## 🧩 Experiment 1: Install Mosquitto Broker on Raspberry Pi

```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

Check if it’s running:
```bash
sudo systemctl status mosquitto
```

Test locally:
```bash
# Terminal 1 – subscriber
mosquitto_sub -t "test/topic"

# Terminal 2 – publisher
mosquitto_pub -t "test/topic" -m "Hello MQTT"
```

---

## 🧩 Experiment 2: ESP32 Publishes MQTT Data

```python
from umqtt.simple import MQTTClient
import network, time

ssid = "Your_SSID"
password = "Your_PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    time.sleep(1)
print("Connected to Wi-Fi")

broker = "192.168.1.10"  # Pi’s IP
client = MQTTClient("esp32_client", broker)
client.connect()

while True:
    msg = "Hello from ESP32!"
    client.publish("iot/demo", msg)
    print("Published:", msg)
    time.sleep(5)
```

---

## 🧩 Experiment 3: Raspberry Pi Subscribes and Displays Messages

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}, Message: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("iot/demo")
client.on_message = on_message

print("Listening for MQTT messages...")
client.loop_forever()
```
