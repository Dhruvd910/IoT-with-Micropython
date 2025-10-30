import os, time

print("Listing files on device:")
print(os.listdir())

print("Current local time:", time.localtime())

for i in range(3, 0, -1):
    print("Starting in", i)
    time.sleep(1)
