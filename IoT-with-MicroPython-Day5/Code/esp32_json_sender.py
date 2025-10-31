# esp32_json_publisher.py
import network, time, random
from umqtt.simple import MQTTClient
import json

WIFI_SSID = "ALICE"
WIFI_PASSWORD = "9811255833"
BROKER = "192.168.137.134" #raspberry ip 
TOPIC = b"iot/jsondata" #your topic name

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("✅ WiFi connected:", wlan.ifconfig())

def main():
    connect_wifi()
    client = MQTTClient("ESP32_JSON", BROKER)
    client.connect()
    print("📡 Connected to MQTT Broker")

    while True:
        data = {
            "device_id": "ESP32_1",
            "temperature": round(random.uniform(25.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2),
            "timestamp": time.time()
        }
        json_data = json.dumps(data)
        client.publish(TOPIC, json_data)
        print("📤 Sent:", json_data)
        time.sleep(5)

main()

