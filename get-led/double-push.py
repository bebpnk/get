import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
num = 0
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
all = False
while True:
    if GPIO.input(up) and GPIO.input(down):
        all = True
        time.sleep(sleep_time)
    elif GPIO.input(up):
        all = False
        if num < 255:
            num += 1
        time.sleep(sleep_time)
        GPIO.output(leds,dec2bin(num))
    elif GPIO.input(down):
        all = False
        if num > 0:
            num = num - 1
        time.sleep(sleep_time)
        GPIO.output(leds,dec2bin(num))
    if all:
        GPIO.output(leds,[1,1,1,1,1,1,1,1])