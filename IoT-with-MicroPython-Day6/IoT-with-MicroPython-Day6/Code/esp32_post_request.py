# esp32_post_request.py
import network
import urequests
import ujson
import time

WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
SERVER_URL = "http://<raspberry-pi-ip>:5000/data"

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
print("Connecting to WiFi...", end="")
while not wlan.isconnected():
    time.sleep(0.5)
    print(".", end="")
print("\nConnected:", wlan.ifconfig())

# Function to send data with retry
def send_data(temp, hum):
    payload = {"temperature": temp, "humidity": hum}
    for attempt in range(3):
        try:
            response = urequests.post(SERVER_URL, json=payload)
            print("Response:", response.text)
            response.close()
            return True
        except Exception as e:
            print("Error:", e, "Retrying...")
            time.sleep(2)
    return False

# Main loop
while True:
    temperature = 25.5
    humidity = 60
    print("Sending data...")
    success = send_data(temperature, humidity)
    if success:
        print("Data sent successfully!")
    else:
        print("Failed to send after retries.")
    time.sleep(5)
