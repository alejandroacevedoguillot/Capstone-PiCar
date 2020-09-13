import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	print( GPIO.input(29))
	print( GPIO.input(31))
	print( GPIO.input(33))
	print( GPIO.input(35))
	print(GPIO.input(37))
	time.sleep(2)
