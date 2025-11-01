# Day 6 – Practical: REST API Communication

## 🧪 Experiments

### 1️⃣ Build REST API on Raspberry Pi

**Steps:**
1. Install Flask and SQLite
2. Create database using `create_db.py`
3. Run Flask API using `pi_flask_api.py`

API Endpoints:
- `POST /data` → Receives sensor data
- `GET /status` → Returns server status

---

### 2️⃣ ESP32 Sends POST Request
- ESP32 collects sensor data (or dummy data)
- Converts it to JSON
- Sends it to Flask API using `urequests` library

**Code:** `esp32_post_request.py`

---

### 3️⃣ Store in SQLite
- Flask server parses incoming JSON
- Inserts the data into `sensor_data` table

You can verify by opening SQLite shell:
```bash
sqlite3 iot_data.db
sqlite> SELECT * FROM sensor_data;
```

---
