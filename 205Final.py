### Import Libraries
import sys
import cv2
import numpy as np
import math
from picamera import PiCamera
import picamera.array
import time
import cv2
from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
from picar import PiCar
car = PiCar(mock_car=False, pins=None)
print(car)
camera = PiCamera()
camera.framerate = 30
stream = picamera.array.PiRGBArray(camera)
## ANGLE AND IMAGE PROCESSING FUNCTIONS ###
def angle_duty(angle):
	duty = 0.14*(20/180)*(angle)
	if -20<angle<-0.01:
		duty = duty -0.3
	if -40< angle < -20:
		duty = duty -0.4
	if -60 < angle < -40:
		duty = duty -0.5
	if -80 < angle < -60:
		duty = duty-0.6
	if angle < -80:
		duty = duty-0.7
	if 0.01<angle<20:
		duty = duty +0.4
	if 20< angle < 40:
		duty = duty +0.6
	if 40 < angle < 60:
		duty = duty + 0.8
	if angle>60:
		duty = duty + 1
	return duty
def blueimage_to_angle():
	file_name = "2Blue"
	camera.capture(stream, format='bgr', use_video_port=True)        # Save a picture directly to memeory
	image = stream.array
	stream.truncate(0)                          # required to retake another pic

	cv2.imwrite(file_name + '.png', image)          # Save the image from memory
	img = cv2.imread(file_name+'.png')

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (100, 150, 0), (135, 255, 255))
	mask = cv2.blur(mask,(5,5))
#	thresh2 = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)[1]
	cv2.imwrite(file_name+"mask.png", mask)
#	M = cv2.moments(thresh2)
	M = cv2.moments(mask)
	print(M["m00"])
	if M["m00"] == 0:
		if switching == 0:
			angle = 1
		if switching == 1:
			angle = -1
		print("not found")
		return angle

	else:
		cx = int(M["m10"]/M["m00"])
		cy = int(M["m01"]/M["m00"])
		angle = (np.arctan((img.shape[1]/2-cx)/(img.shape[0]-cy)))*180/math.pi
		img = cv2.circle(img, (cx, cy), 15, (255, 255, 103), thickness=3)
		cv2.imwrite(file_name+".png", img)
		return angle

def yellowimage_to_angle():
        file_name = "cam_track_test"
        camera.capture(stream, format='bgr', use_video_port=True)        # Save a picture directly to memeory
        image = stream.array
        stream.truncate(0)                          # required to retake another pic

        cv2.imwrite(file_name + '.png', image)          # Save the image from memory
        img = cv2.imread(file_name+'.png')

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (25, 150, 0), (35, 255, 255))
        mask = cv2.blur(mask,(5,5))
        thresh2 = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(file_name+"mask.png", mask)
        M = cv2.moments(thresh2)
#        print(M["m00"])
        if M["m00"] == 0:
                if switching == 0:
                        angle = 1
                if switching == 1:
                        angle  = -1
                print("not found")
                return angle
        else:
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                angle = (np.arctan((img.shape[1]/2-cx)/(img.shape[0]-cy)))*180/math.pi
                img = cv2.circle(img, (cx, cy), 15, (255, 255, 103), thickness=3)
                cv2.imwrite(file_name+"circle.png", img)
                return angle

def LEFTyellowimage_to_angle():
	file_name = "2Left"
	camera.capture(stream, format='bgr', use_video_port=True)        # Save a picture directly to memeory
	img = stream.array
	stream.truncate(0)                          # required to retake another pic

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (25, 150, 0), (35, 255, 255))
	leftMask  = mask[1:mask.shape[0], 1:mask.shape[1]//2]
	thresh2 = cv2.threshold(leftMask, 0, 255, cv2.THRESH_BINARY)[1]
	cv2.imwrite(file_name+"Leftmask.png", mask)
	M = cv2.moments(thresh2)
#	M = cv2.moments(mask)
#	print(M["m00"])
	if M["m00"] == 0:
		if switching == 0:
			angle = 1
		if switching == 1:
			angle  = -1
		print("not found")
		return angle
	else:
		cx = int(M["m10"]/M["m00"])
		cy = int(M["m01"]/M["m00"])
		angle = (np.arctan((img.shape[1]-cx)/(img.shape[0]-cy)))*180/math.pi
		img = cv2.circle(img, (cx, cy), 15, (255, 255, 103), thickness=3)
		cv2.imwrite(file_name+".png", img)
		return angle


def RIGHTyellowimage_to_angle():
	file_name = "2Right"
	camera.capture(stream, format='bgr', use_video_port=True)        # Save a picture directly to$
	img = stream.array
	cv2.imwrite(file_name+"original.png", img)
	stream.truncate(0)                          # required to retake another pic

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (25, 150, 0), (35, 255, 255))

	rightMask = mask[1:mask.shape[0], mask.shape[1]//2 +1:mask.shape[1]]
	thresh2 = cv2.threshold(rightMask, 0, 255, cv2.THRESH_BINARY)[1]
	cv2.imwrite(file_name+"mask.png", mask)
	M = cv2.moments(thresh2)
#	M  = cv2.moments(mask)
	print(M["m00"])
	if M["m00"] == 0:
		if switching == 0:
			angle = 1
		if switching == 1:
			angle  = -1
		print("not found")
		return angle
	else:
		cx = int(M["m10"]/M["m00"])
		cy = int(M["m01"]/M["m00"])
		angle = (np.arctan((thresh2.shape[1]-cx)/(thresh2.shape[0]-cy)))*180/math.pi
		angle = angle*-1
		img = cv2.circle(thresh2, (cx, cy), 15, (0, 255, 255), thickness=3)
		cv2.imwrite(file_name+"circle.png", img)
		return angle

###### ACTUAL RUN STUFF #########################################################
if (len(sys.argv) > 1):
        rightFirst = float(sys.argv[1])
else:
        rightFirst = 0
direction = rightFirst
#Initialization
car.set_nod_servo(1)
car.set_swivel_servo(-2)
start_time = time.time()
endTime = time.time() + 30
displaySpeed = 0.2
displayTime = 0
switching = 0
photoCounter = 0
on = 0
#-------------------------------- Yellow--------------------------------------- #
distance = car.read_distance()
counter = 0
while counter < 2:
#------------------------------RIGHT--------------------------------#
	on = car.adc.read_adc(7)
	if on > 500:
		car.set_motor(0)
	if on < 500:
		if rightFirst == 1:
			photoCounter = 0
			while photoCounter < 7:
				car.set_motor(70)
				if(displayTime - time.time() <= 0):
					angle = RIGHTyellowimage_to_angle()
#					print("rightyellowimage")
#					print("Angle: " + str(angle))
					duty = angle_duty(angle)
					car.set_steer_servo(duty)
					displayTime = time.time()+displaySpeed
					photoCounter = photoCounter + 1
			distance = car.read_distance()
			while distance > 27 :
				distance = car.read_distance()
				car.set_motor(70)
				if(displayTime - time.time() <= 0):
					angle = yellowimage_to_angle()
#					print("yellowimage")
#					print("Angle: " + str(angle))
					duty = angle_duty(angle)
					car.set_steer_servo(duty)
					displayTime = time.time()+displaySpeed
					rightFirst = 0


			endTime = time.time() + 4
			car.set_steer_servo(-2.5)
			while time.time() <= endTime:
				car.set_motor(70, False)
			car.set_motor(0)
			counter = counter + 1
			print("Finished Right")
#			print("Counter is " +str(counter))
#			print("Right First is " + str(rightFirst))
#------------------------------LEFT-------------------------------#
		if counter < 2:
			if rightFirst == 0:
				photoCounter = 0
				while photoCounter < 7:
                        		car.set_motor(60)
                        		if(displayTime - time.time() <= 0):
                                		angle = LEFTyellowimage_to_angle()
#                                		print("LEFTyellowimage")
#                               		print("Angle: " + str(angle))
                                		duty = angle_duty(angle)
                                		car.set_steer_servo(duty)
                                		displayTime = time.time()+displaySpeed
                                		photoCounter = photoCounter + 1
				distance = car.read_distance()
				while distance > 30 :
					distance = car.read_distance()
					if(distance<30):
						car.set_motor(0)
#					if(50<distance<60):
#						car.set_motor(-10)
					if(60<distance<75):
						car.set_motor(65)
					if(distance>75):
						car.set_motor(65)
					if(displayTime - time.time() <= 0):
						angle = yellowimage_to_angle()
						duty = angle_duty(angle)
#						print("Angle: " + str(angle))
#                       			print("Duty: " + str(duty))
						car.set_steer_servo(duty)
						displayTime = time.time()+displaySpeed
						rightFirst  = 1
#				endTime = time.time() + 3.2
				car.set_steer_servo(2.5)
				endTime = time.time()+3.8
				while time.time() <= endTime:
					car.set_motor(70, False)
				counter = counter + 1
				print("Finished Left")
#------------------------ BLUE -------------------------------------------------#

if direction == 1:
	car.set_steer_servo(2.5)
else:
	car.set_steer_servo(-2.5)

endTime = time.time() + 1.5
while time.time() <= endTime:
	car.set_motor(55, False)

print("Going back")
car.set_motor(0)
distance = car.read_distance()

while distance > 15:
	distance = car.read_distance()
	if(40<distance<50):
		car.set_motor(0)
	if(50<distance<60):
		car.set_motor(0)
	if(60<distance<75):
		car.set_motor(50)
	if(distance>75):
		car.set_motor(50)
#			print(distance)
##       	car.set_motor(50)
	if(displayTime - time.time() <= 0):
		angle = blueimage_to_angle()
		duty = angle_duty(angle)
#		print("Angle: " + str(angle))
#		print("Duty: " + str(duty))
		car.set_steer_servo(duty)
		displayTime = time.time()+displaySpeed
print("Finished Blue")
GPIO.cleanup()
