# Day 5 – Assignment

### 1️⃣ ESP32 Sends Nested JSON
Create a nested JSON payload such as:
```json
{
  "device": "ESP32",
  "sensors": {
    "temperature": 25.3,
    "humidity": 60
  },
  "timestamp": "2025-10-30T10:00"
}
```

### 2️⃣ Pi Extracts Selected Fields
- Parse the nested JSON.
- Extract only `"temperature"` and `"humidity"`.
- Save the values to `data_log.csv`.

---
**Bonus:**  
Add error handling if data is malformed or missing fields.
