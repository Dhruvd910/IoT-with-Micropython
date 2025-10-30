# Day 2 – Hands-on Experiments

## 🧩 Experiment 1: Write MicroPython Script with Loops & Functions

```python
# loop_function_demo.py
def blink_led(times):
    for i in range(times):
        print("Blink", i + 1)
        time.sleep(1)

import time
blink_led(5)
print("Done!")
```

---

## 🧩 Experiment 2: Save & Auto-run from Flash Memory

1. Open Thonny → `File > Save As`
2. Choose **MicroPython device**
3. Save your code as `main.py`
4. Reset ESP32 → It will auto-run the script automatically.

Example:
```python
print("Running main.py automatically!")
```

---

## 🧩 Experiment 3: Use `os` and `time` Modules

```python
import os, time

print("Files on device:", os.listdir())
print("Current time:", time.localtime())

for i in range(3, 0, -1):
    print("Starting in", i)
    time.sleep(1)
```
