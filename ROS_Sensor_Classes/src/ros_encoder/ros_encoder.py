#!/usr/bin/env python

import RPi.GPIO as gpio
import time
import sys
import Encoder
import rospy
import signal
from std_msgs.msg import Float32


def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class encoder_data():
	def __init__(self):
		rospy.init_node('encoder', anonymous=True)
		self.count_publisher = rospy.Publisher('/encoder_count',Float32, queue_size=1)
		self.r = rospy.Rate(15)
	def count_sendor(self,ticks):
		data = Float32()
		data.data=ticks
		self.count_publisher.publish(data)
        
        

A= 21
B= 20 
CPR = 250

enc = Encoder.Encoder(A,B)
encoder=encoder_data()
time.sleep(0.5)
print ('-----------------------------------------------------------------encoder')
start =time.time()
CC=0
PC=enc.read()
sample_rate = 1
try :
	while True :
		current = time.time()
		delta = current-start
		count = enc.read()
		CC = count
		if delta >= sample_rate:
			#count =enc.read()
			print("PC", PC)
			print("CC", CC)
			Rev = (CC- PC)/float(CPR)*15.3
			print("REV",Rev)
			encoder.count_sendor(count)
			PC = CC
			start = time.time()
		#encoder.r.sleep()
        
except (KeyboardInterrupt, SystemExit):
	gpio.cleanup()
	sys.exit(0)
