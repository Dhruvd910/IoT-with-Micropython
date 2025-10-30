# Day 4 – MQTT Fundamentals: Publish / Subscribe & Brokers

## 📘 Topics Covered
- What is MQTT?
- Publish/Subscribe model
- MQTT Brokers
- MQTT usage in IoT

---

## 🌐 What is MQTT?
**MQTT (Message Queuing Telemetry Transport)** is a lightweight protocol for IoT communication built on top of TCP/IP.  
It enables **devices to communicate efficiently with minimal bandwidth**.

---

## 🧩 MQTT Architecture

### Components:
1. **Publisher** – sends data (ESP32)
2. **Subscriber** – receives data (Raspberry Pi)
3. **Broker** – manages message routing (Mosquitto)

```
ESP32 (Publisher) → MQTT Broker ← Raspberry Pi (Subscriber)
```

---

## ⚙️ How It Works
- Devices **don’t send messages directly** to each other.
- Instead, they send messages to **topics** managed by the **broker**.

| Role | Function |
|------|-----------|
| Broker | Receives and distributes messages |
| Publisher | Sends data to a topic |
| Subscriber | Listens to a topic |

---

## 💡 Example
If ESP32 publishes on topic `sensor/data`:

- ESP32 → `sensor/data` → “Temperature: 25°C”
- Raspberry Pi subscribed to `sensor/data` receives the message instantly.

---

## 🧠 Key MQTT Terms

| Term | Description |
|------|--------------|
| **Topic** | Label for message channel (e.g., "iot/temp") |
| **QoS** | Quality of Service (0, 1, 2) defines delivery guarantee |
| **Retained Message** | Last message kept for new subscribers |
| **Last Will** | Message sent when client disconnects unexpectedly |

---

## 🔌 Why MQTT?
- Lightweight protocol for IoT devices
- Reliable over unstable networks
- Easy to integrate across multiple devices

---

## 🧠 Summary
By the end of Day 4, you’ll understand:
- How MQTT simplifies IoT communication  
- How to use Mosquitto broker  
- How ESP32 publishes and Raspberry Pi subscribes  
