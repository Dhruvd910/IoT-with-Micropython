import paho.mqtt.client as mqtt
import json
from statistics import mean

# Store last 5 values for moving average
history = []

# MQTT Topic
TOPIC = "edge/data"

def is_outlier(value, avg):
    """Detect outlier: if value is 2× away from mean."""
    if avg == 0:
        return False
    return abs(value - avg) > 2 * avg

def on_message(client, userdata, message):
    global history

    data = json.loads(message.payload.decode())
    value = data["value"]
    timestamp = data["timestamp"]

    print("\nReceived:", value)

    # Compute current average
    curr_avg = mean(history) if history else 0

    # Outlier detection
    if is_outlier(value, curr_avg):
        print("⚠ OUTLIER DETECTED:", value, " (ignored)")
        return

    # Add to history (keep last 5)
    history.append(value)
    if len(history) > 5:
        history.pop(0)

    # Moving average
    mov_avg = round(mean(history), 2)

    print("Accepted:", value)
    print("History:", history)
    print("Moving Average:", mov_avg)

# MQTT client setup
client = mqtt.Client()
client.on_message = on_message

client.connect("localhost")
client.subscribe(TOPIC)

print("Listening for data...")
client.loop_forever()
