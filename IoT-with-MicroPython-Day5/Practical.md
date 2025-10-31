# Day 5 – Practical: JSON Communication & CSV Logging

## 🧪 Experiment Steps

### 1️⃣ ESP32 Sends JSON Payload
- ESP32 reads sensor or dummy data.
- Converts it into JSON format using `ujson`.
- Sends it over serial or Wi-Fi.

**Code:** `esp32_json_sender.py`

### 2️⃣ Raspberry Pi Parses JSON
- Pi receives JSON data from ESP32.
- Parses using Python’s `json` module.
- Extracts individual values.

**Code:** `pi_json_parser.py`

### 3️⃣ Pi Logs Data to CSV
- Parsed data is appended to a CSV file.
- Each new reading adds a new line.

**Output Example:**
```
timestamp,temperature,humidity
2025-10-30T10:00,25.3,60
```

---
## 🧰 Requirements
- MicroPython installed on ESP32
- Python 3 installed on Raspberry Pi
- Modules: `ujson`, `json`, `csv`

---
