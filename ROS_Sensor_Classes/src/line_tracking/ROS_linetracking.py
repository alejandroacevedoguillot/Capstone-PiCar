#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import rospy
import numpy as np
from std_msgs.msg import Float32
GPIO.setmode(GPIO.BCM)


GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(1, GPIO.IN)

print ('-----------------------------------------------------------------linetracking start')
try :
    while True :
	L11 =GPIO.input(5)
        L12 =GPIO.input(6)
	L13 =GPIO.input(13)
	L14 =GPIO.input(19)
	L15 =GPIO.input(26)
	L21 =GPIO.input(24)
        L22 =GPIO.input(25)
	L23 =GPIO.input(8)
	L24 =GPIO.input(7)
	L25 =GPIO.input(1)
	L1 = np.array([1,L11,L12,L13,L14,L15]) 
	L2 = np.array([2,L21,L22,L23,L24,L25])
	print(L1)
	print(L2) 
	time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    sys.exit(0)
except:
    GPIO.cleanup()