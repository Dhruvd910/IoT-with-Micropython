# Day 1 – Hands-on Experiments

## 🧩 Experiment 1: Flash MicroPython on ESP32

**Steps:**
1. Download MicroPython firmware (`esp32-<version>.bin`) from [micropython.org](https://micropython.org/download/esp32/).
2. Open **Thonny IDE** → `Tools > Options > Interpreter`.
3. Select **MicroPython (ESP32)** and correct **COM port**.
4. Click **Install or update MicroPython** and select the `.bin` file.
5. Once flashed, open the REPL and test:
   ```python
   print("ESP32 MicroPython is ready!")
   ```

---

## 🧩 Experiment 2: Install Raspberry Pi OS

**Steps:**
1. Download **Raspberry Pi Imager** and install it.  
2. Insert a microSD card into your computer.  
3. Select OS → *Raspberry Pi OS (32-bit)*.  
4. Configure Wi-Fi, username, and password (optional).  
5. Click **Write** to flash the image.  
6. Insert SD card into the Raspberry Pi and power it on.

---

## 🧩 Experiment 3: Run “Hello World” on Both

### On ESP32 (MicroPython)
```python
print("Hello from ESP32 with MicroPython!")
```

### On Raspberry Pi (Python)
```python
print("Hello from Raspberry Pi with Python!")
```
