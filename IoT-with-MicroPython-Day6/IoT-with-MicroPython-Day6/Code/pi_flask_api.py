from flask import Flask, request, jsonify
import sqlite3, time

app = Flask(__name__)

# ---- Create Database if not exist ----
def init_db():
    conn = sqlite3.connect("iot_data.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT,
            temperature REAL,
            humidity REAL,
            timestamp REAL
        )
    """)
    conn.commit()
    conn.close()

# ---- Home route ----
@app.route('/')
def home():
    return "🌐 Flask REST API is running!"

# ---- API Endpoint to receive sensor data ----
@app.route('/sensor', methods=['POST'])
def receive_data():
    data = request.get_json()  # Parse JSON from client
    device = data.get("device")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    timestamp = time.time()

    # Save into SQLite
    conn = sqlite3.connect("iot_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO sensor_data (device, temperature, humidity, timestamp) VALUES (?, ?, ?, ?)",
              (device, temperature, humidity, timestamp))
    conn.commit()
    conn.close()

    print(f"📩 Received from {device}: Temp={temperature}, Humidity={humidity}")

    # Return a JSON response
    return jsonify({"status": "success", "device": device, "stored_at": timestamp}), 200

# ---- Run server ----
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
