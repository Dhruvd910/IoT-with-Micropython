# pi_json_parser.py
import json
import csv
import time
import sys

csv_file = "data_log.csv"

# Prepare CSV file with headers
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature", "humidity"])

print("Listening for JSON input...")

try:
    while True:
        # Simulate receiving JSON from ESP32 (in practice, read from serial)
        json_input = input("Enter JSON data: ")
        try:
            data = json.loads(json_input)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            temperature = data.get("temperature")
            humidity = data.get("humidity")

            with open(csv_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, temperature, humidity])

            print(f"Logged -> Temp: {temperature}°C, Humidity: {humidity}%")

        except json.JSONDecodeError:
            print("Invalid JSON received!")
except KeyboardInterrupt:
    print("\nExiting...")
