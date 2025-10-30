import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("iot/demo")
client.on_message = on_message

print("Subscribed to iot/demo")
client.loop_forever()
