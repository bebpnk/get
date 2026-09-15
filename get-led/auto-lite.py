import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
sensor = 6
GPIO.setup(sensor, GPIO.IN)
while True:
    state = GPIO.input(sensor)
    if state == 1:
        GPIO.output(led, GPIO.LOW)
    else:
        GPIO.output(led,GPIO.HIGH)
    time.sleep(0.1)