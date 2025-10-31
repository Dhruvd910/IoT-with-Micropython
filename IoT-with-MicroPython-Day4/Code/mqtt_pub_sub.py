import network
import time
import random
from umqtt.simple import MQTTClient

# ====== Wi-Fi & MQTT Configuration ======
WIFI_SSID = 'akgiot'
WIFI_PASS = 'akgiot25'

MQTT_BROKER = '192.168.0.114'  # <-- Replace with your Raspberry Pi IP
CLIENT_ID = 'esp32_client'
TOPIC_PUB = b'sensors/temperature'
TOPIC_SUB = b'sensors/humidity'

# ====== Connect to Wi-Fi ======
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
    print('Connected to Wi-Fi:', wlan.ifconfig())

# ====== MQTT Callback ======
def sub_callback(topic, msg):
    print(f"Received message on {topic.decode()}: {msg.decode()}")

# ====== Main MQTT Logic ======
def main():
    connect_wifi()
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.set_callback(sub_callback)
    client.connect()
    print('Connected to MQTT broker')

    # Subscribe to humidity topic
    client.subscribe(TOPIC_SUB)
    print(f'Subscribed to topic: {TOPIC_SUB.decode()}')

    try:
        while True:
            # Publish random temperature value
            temperature = round(random.uniform(20.0, 30.0), 2)
            client.publish(TOPIC_PUB, str(temperature))
            print(f'Published temperature: {temperature} °C')

            # Check for incoming messages
            client.check_msg()

            time.sleep(5)  # Publish every 5 seconds
    except KeyboardInterrupt:
        print('Disconnected')
        client.disconnect()

# ====== Run the program ======
main()
