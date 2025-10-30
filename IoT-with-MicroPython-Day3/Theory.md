# Day 3 – Networking Basics (Wi-Fi, IP, Socket Programming)

## 📘 Topics Covered
- Introduction to networking in IoT
- Understanding Wi-Fi and IP addresses
- Basics of socket communication

---

## 🌐 Wi-Fi Basics
Wi-Fi allows IoT devices (like ESP32) to connect wirelessly to a local network.

**Terms:**
- **SSID:** Wi-Fi network name  
- **Password:** Network key  
- **Access Point (AP):** Router or hotspot  
- **Station (STA):** Device connecting to Wi-Fi  

ESP32 works in **Station mode** to connect to an existing Wi-Fi network.

---

## 🧩 IP Address
Each device on a network has a **unique IP address**.

| Type | Example | Description |
|------|----------|-------------|
| Private | 192.168.x.x | Used inside local networks |
| Public | 8.8.8.8 | Used on the Internet |
| Localhost | 127.0.0.1 | Refers to the same device |

Use `ifconfig` on Pi or `wlan.ifconfig()` on ESP32 to check IPs.

---

## 🔌 Sockets in IoT
Sockets allow devices to **communicate** via TCP or UDP.

- **Server:** Listens for connections (Raspberry Pi)
- **Client:** Sends messages (ESP32)

### Example Flow:
```
ESP32 (Client) → Wi-Fi → Raspberry Pi (Server)
```

---

## 🧠 Summary
By the end of Day 3, you’ll understand:
- How ESP32 connects to Wi-Fi  
- How sockets enable two-way communication  
- How to send and receive data between ESP32 and Raspberry Pi
