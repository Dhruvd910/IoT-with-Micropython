import os, esp, gc

print("Device Information:")
print(os.uname())
print("Flash size:", esp.flash_size())
print("Free memory:", gc.mem_free(), "bytes")
