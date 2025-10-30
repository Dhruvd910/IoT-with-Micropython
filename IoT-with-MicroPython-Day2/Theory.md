# Day 2 – MicroPython Syntax, REPL, Modules & File System

## 📘 Topics Covered
- Basic MicroPython syntax
- Using the REPL (Read-Eval-Print Loop)
- Modules and imports
- File system and auto-run scripts

---

## 🐍 MicroPython Syntax Basics

MicroPython follows most of Python’s syntax rules but is optimized for microcontrollers.

### Example:
```python
# Variables
led_pin = 2

# Conditional statement
if led_pin == 2:
    print("LED connected to GPIO 2")

# Loops
for i in range(5):
    print("Count:", i)
```

### Functions
```python
def greet(name):
    print("Hello", name)

greet("ESP32")
```

---

## 💻 REPL (Read-Eval-Print Loop)

REPL is an interactive prompt that lets you test commands line by line.

**How to open REPL:**
1. Open Thonny or serial terminal (115200 baud).
2. Press **Enter** and you’ll see:
   ```
   MicroPython v1.x.x on 202X-XX-XX; ESP32 module
   >>>
   ```
3. Try:
   ```python
   print("Welcome to REPL")
   import os
   os.listdir()
   ```

---

## 🧩 Modules

Modules are built-in libraries that extend functionality.

| Module | Purpose |
|---------|----------|
| `os` | File system, directory handling |
| `time` | Delays, timestamps |
| `machine` | Control pins, ADC, PWM, I2C, etc. |
| `network` | Wi-Fi, connections |

**Example:**
```python
import time
for i in range(5):
    print("Blink", i)
    time.sleep(1)
```

---

## 💾 File System in MicroPython

MicroPython provides a small internal flash file system where scripts are stored.

**Common files:**
- `boot.py` – runs once at startup  
- `main.py` – runs automatically after boot

**List files:**
```python
import os
print(os.listdir())
```

**Save a file from Thonny:**
1. Click **File → Save as → MicroPython device**
2. Save as `main.py` → It will auto-run on boot

---

## 🧠 Summary

By the end of Day 2, you should:
- Understand MicroPython syntax and REPL
- Use modules like `os` and `time`
- Store and execute code from flash memory
