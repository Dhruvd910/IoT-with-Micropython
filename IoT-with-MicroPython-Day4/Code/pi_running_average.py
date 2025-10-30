import paho.mqtt.client as mqtt

numbers = []

def on_message(client, userdata, msg):
    global numbers
    val = int(msg.payload.decode())
    numbers.append(val)
    if len(numbers) > 10:
        numbers.pop(0)
    avg = sum(numbers) / len(numbers)
    print(f"Received: {val}, Running Average: {avg:.2f}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("iot/random")
client.on_message = on_message

print("Listening for random numbers...")
client.loop_forever()
