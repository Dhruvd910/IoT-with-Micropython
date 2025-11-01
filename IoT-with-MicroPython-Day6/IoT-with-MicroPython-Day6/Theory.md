# Day 6 – REST APIs with Flask and HTTP Methods

## 🌐 What is a REST API?
A **REST API (Representational State Transfer)** allows communication between devices or applications using standard **HTTP methods** like GET, POST, PUT, and DELETE.

In IoT, REST APIs are often used for **device-to-server communication**, e.g., ESP32 sending sensor data to Raspberry Pi.

---

## 🧩 REST Architecture Overview

**Client-Server Model**
- **Client:** ESP32 (sends sensor data)
- **Server:** Raspberry Pi running Flask (receives and stores data)

```
ESP32 ----POST----> Flask Server ----> SQLite Database
          <----JSON Response----
```

---

## ⚙️ HTTP Methods Overview

| Method | Purpose | IoT Example |
|---------|----------|--------------|
| **GET** | Retrieve data | Get latest sensor data |
| **POST** | Send new data | ESP32 sends temperature reading |
| **PUT** | Update data | Update device settings |
| **DELETE** | Remove data | Delete old records |

---

## 🧱 Flask Framework (on Raspberry Pi)
Flask is a lightweight Python web framework used to build APIs easily.

**Install Flask:**
```bash
sudo apt update
pip install flask
```

**Basic Flask App Example:**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 🗄️ SQLite Database
SQLite is a small, file-based database ideal for Raspberry Pi projects.

**Install SQLite:**
```bash
sudo apt install sqlite3
pip install flask_sqlalchemy
```

**Create Database Table Example:**
```sql
CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    timestamp TEXT
);
```

---

## 🧩 REST API Flow in IoT
1. ESP32 collects sensor data.  
2. ESP32 sends data via **HTTP POST** to Flask server.  
3. Flask receives data and stores it in SQLite.  
4. Flask returns **JSON response** confirming success.  

---
