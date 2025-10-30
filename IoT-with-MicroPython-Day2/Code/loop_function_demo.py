import time

def blink_led(times):
    for i in range(times):
        print("Blink", i + 1)
        time.sleep(1)

blink_led(5)
print("Loop completed!")
