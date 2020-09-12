import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 11

def ultrasonic_init(Trigger, Echo):
	GPIO.setup(Trigger, GPIO.OUT)
	GPIO.output(Trigger, False)
	GPIO.setup(Echo, GPIO.IN)
	time.sleep(.5)

def ultrasonic_read(Trigger, Echo):
	GPIO.output(Trigger, True)
	time.sleep(0.00001)
	GPIO.output(Trigger, False)
	while GPIO.input(Echo) == 0:
		start_time = time.time()
	while GPIO.input(Echo) == 1:
		end_time = time.time()
	total_distance = (end_time - start_time) * 34300
	return round(total_distance/2,1)

n = 1
startTime = time.time()
endTime = startTime + 20
distanceArray = [0]*1

ultrasonic_init(TRIG,ECHO)

while startTime < endTime:
	for i in range(0,n):
		distanceArray[i] = ultrasonic_read(TRIG, ECHO)
		time.sleep(0.001)
#		print(distanceArray[i])
	time.sleep(1);
	print("The distance is", distanceArray)
	startTime = startTime+1

