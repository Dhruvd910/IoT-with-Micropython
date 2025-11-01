# pi_flask_api.py
from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)

DB = "iot_data.db"

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Store in SQLite
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, ?)",
                       (temperature, humidity, timestamp))
        conn.commit()
        conn.close()

        return jsonify({"status": "success", "message": "Data stored successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "time": time.strftime('%Y-%m-%d %H:%M:%S')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
