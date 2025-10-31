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
### Why JSON in IoT?
Human-readable — easy to inspect during debugging.
Lightweight — compact text (smaller than XML in many cases).
Language-agnostic — most languages have JSON libraries (Python, C, JS, MicroPython, etc.).
Structured — supports nested objects and arrays (unlike CSV).
Works well over networks — used in HTTP APIs, MQTT payloads, WebSockets.
# In IoT: JSON is perfect to send sensor readings, device metadata, configurations and small structured messages between devices and servers.

### JSON data types and structure
JSON supports 6 basic types:
Object — unordered key:value pairs enclosed in {}
Example: {"device":"ESP32","temp":22}
Array — ordered list in []
Example: ["a", "b", "c"]
String — double quoted text "hello" (must use double quotes)
Number — integers or floats (no separate int/float type)
Boolean — true or false
null — empty / missing value



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
