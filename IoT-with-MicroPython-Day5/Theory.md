# Day 5 – Data Formats: JSON, CSV & Serialization

## 📘 Theory Overview
Data formats are crucial in IoT to **exchange, store, and process information** between devices and servers.

### 🔹 JSON (JavaScript Object Notation)
- Lightweight data format used for **structured data exchange**.
- Easy to read and supported by almost all languages.
- Represents data as **key-value pairs**.

**Example:**
```json
{
  "temperature": 25.3,
  "humidity": 60
}
```
### Nested Jason
```json
{
  "device_id": "ESP32_1",
  "location": {"room": "lab1", "floor": 2},
  "sensors": {"temp": 27.5, "humidity": 55}
}
```

### How this nested data will appear:-
``` python_output
data = json.loads(payload)
room = data["location"]["room"]
temp = data["sensors"]["temp"]
print(f"Room: {room} | Temperature: {temp}")
```

### Why JSON in IoT?
- Ideal for sending **sensor readings**.
- Compact and human-readable.
- Works seamlessly with MQTT and REST APIs.

### 🔹 CSV (Comma-Separated Values)
- Used for **storing large datasets** in table form.
- Each line is a data record, and each record consists of fields separated by commas.

**Example:**
```
timestamp,temperature,humidity
2025-10-30T10:00,25.3,60
```

### Why CSV in IoT?
- Excellent for **logging** and **data analysis**.
- Can be easily opened in Excel, Python, or data visualization tools.

### 🔹 Serialization
Serialization means converting data structures into a format that can be **saved or transmitted** and then **reconstructed** later.

- JSON is a form of serialization.
- Other formats include binary or MessagePack.

---
## 🔧 Summary
| Format | Purpose | Example Use |
|---------|----------|--------------|
| JSON | Data transfer | ESP32 → Cloud |
| CSV | Data logging | Pi → File |
| Serialized Object | Data backup | Save state of variables |

---
