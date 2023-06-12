import RPi.GPIO as GPIO
import time

signal_pin = 18

# GPIO.setmode(GPIO.BOARD) # 1 ~ 40
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT)


while (True):
    GPIO.output(signal_pin, True)
    time.sleep(2)
    GPIO.output(signal_pin, False)
    time.sleep(1)