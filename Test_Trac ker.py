import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin_1 = 35
pin_2 = 36
pin_3 = 38
GPIO.setup(pin_1,GPIO.IN)
GPIO.setup(pin_2,GPIO.IN)
GPIO.setup(pin_3,GPIO.IN)
while True:
    time.sleep(0.5)
    print("__________________")
    print(GPIO.input(pin_1))
    print(GPIO.input(pin_2))
    print(GPIO.input(pin_3))