with open("/proc/uptime", "r") as f:
    uptime_seconds = float(f.readline().split()[0])
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60

print(f"System Uptime: {int(hours)} hours, {int(minutes)} minutes")
