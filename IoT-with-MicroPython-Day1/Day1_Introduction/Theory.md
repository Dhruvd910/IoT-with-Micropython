# Day 1 – Introduction to IoT & MicroPython

## 📘 Topics Covered
- IoT Architecture  
- ESP32 vs Raspberry Pi  
- Installing MicroPython on ESP32  
- Installing Raspberry Pi OS  
- Running your first Python programs  

---

## 🌐 IoT Architecture

IoT (Internet of Things) connects physical devices to the internet for sensing, data exchange, and automation.

**4-Layer IoT Architecture:**

1. **Perception Layer (Sensing):** Sensors and actuators that collect data.  
2. **Network Layer:** Communication via Wi-Fi, Bluetooth, ZigBee, or Cellular.  
3. **Processing Layer:** Edge devices or servers that store and process data.  
4. **Application Layer:** User-facing applications for monitoring and control.

---

## ⚙️ ESP32 vs Raspberry Pi

| Feature | ESP32 | Raspberry Pi |
|----------|--------|---------------|
| Type | Microcontroller | Mini Computer |
| Processor | Dual-core Xtensa (240 MHz) | Quad-core ARM Cortex-A series |
| RAM | ~520 KB | 1–8 GB |
| OS | No OS (firmware only) | Full Linux OS (Raspberry Pi OS) |
| Programming | MicroPython, Arduino C | Python, Node.js, C/C++ |
| Connectivity | Wi-Fi + Bluetooth | Wi-Fi + Ethernet (depending on model) |
| Use Case | Real-time IoT sensors and control | Data processing, AI, web hosting |

---

## 🧩 Installing MicroPython on ESP32

### 🔸 Requirements
- ESP32 development board  
- USB cable  
- Thonny IDE or uPyCraft  
- MicroPython firmware (.bin file)

### 🔹 Steps
1. **Download MicroPython firmware:** Visit [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)
2. **Install Thonny IDE:** Download from [https://thonny.org](https://thonny.org)
3. **Connect ESP32 to your computer** via USB.  
4. **In Thonny:**  
   - Go to `Tools → Options → Interpreter`  
   - Choose **MicroPython (ESP32)** and correct **COM port**  
   - Click **Install or update MicroPython**  
   - Select the `.bin` file and flash it  
5. Once complete, open the **Thonny Shell** and type:
   ```python
   print("Hello, MicroPython on ESP32!")
   ```

✅ Your ESP32 is now ready to run MicroPython scripts!

---

## 💾 Installing Raspberry Pi OS

### 🔸 Requirements
- Raspberry Pi board (Pi 3, 4, or 5)
- 16 GB or larger microSD card
- Card reader and monitor (or headless setup)
- Raspberry Pi Imager software

### 🔹 Steps
1. **Download and install Raspberry Pi Imager** from [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
2. **Insert your microSD card** into the computer.
3. Open **Raspberry Pi Imager**, then:
   - Choose OS → *Raspberry Pi OS (32-bit)*  
   - Choose Storage → your SD card  
   - Click **Next → Edit Settings**
     - Set Hostname, Wi-Fi SSID & Password, Enable SSH (optional)
   - Click **Save → Write**
4. Once flashing completes, insert SD card into Raspberry Pi.
5. Power on the Raspberry Pi — it will boot automatically into the OS.

---

## 🐍 Setting Up Python

### On ESP32
After flashing, open Thonny and use:
```python
print("Hello from ESP32!")
```

### On Raspberry Pi
Python comes preinstalled. Verify with:
```bash
python3 --version
```
Create and run your first program:
```bash
nano hello.py
print("Hello from Raspberry Pi!")
```
Run:
```bash
python3 hello.py
```

---

## 🧠 Summary

By the end of Day 1, you should be able to:
- Explain IoT architecture and key layers  
- Differentiate ESP32 and Raspberry Pi  
- Flash MicroPython firmware on ESP32  
- Install Raspberry Pi OS using Raspberry Pi Imager  
- Run “Hello World” on both devices
