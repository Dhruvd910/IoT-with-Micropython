# esp32_json_sender.py
import ujson
import time

# Simulated sensor data
temperature = 25.3
humidity = 60

while True:
    payload = {
        "device": "ESP32",
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.time()
    }
    print(ujson.dumps(payload))  # Send as JSON string
    time.sleep(5)
