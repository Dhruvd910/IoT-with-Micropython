import paho.mqtt.client as mqtt
import json, csv, time

BROKER = "localhost"
TOPIC = "iot/jsondata"
CSV_FILE = "sensor_log.csv"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker")
        client.subscribe(TOPIC)
        print(f"🔊 Subscribed to: {TOPIC}")
    else:
        print("❌ Failed to connect")

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    parsed = json.loads(data)
    
    # Extract fields
    ts = parsed["timestamp"]
    temp = parsed["temperature"]
    hum = parsed["humidity"]

    print(f"📩 Time: {ts} | Temp: {temp} | Humidity: {hum}")

    # Log to CSV
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, temp, hum])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)

print("🕓 Waiting for JSON data... (Ctrl+C to stop)")
client.loop_forever()
