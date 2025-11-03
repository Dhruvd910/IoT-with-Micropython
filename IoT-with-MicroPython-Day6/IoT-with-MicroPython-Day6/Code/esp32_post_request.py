import urequests
import network
import time
import random

WIFI_SSID = "ALICE"
WIFI_PASSWORD = "9811255833"
API_URL = "http://192.168.137.134:5000/sensor"  # Pi’s IP address

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("✅ Wi-Fi Connected:", wlan.ifconfig())

def send_data():
    data = {
        "device": "ESP32_1",
        "temperature": round(random.uniform(25, 30), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }

    try:
        response = urequests.post(API_URL, json=data)
        print("📤 Sent:", data)
        print("🧾 Server Response:", response.text)
        response.close()
    except Exception as e:
        print("❌ Error sending data:", e)

connect_wifi()

while True:
    send_data()
    time.sleep(5)
