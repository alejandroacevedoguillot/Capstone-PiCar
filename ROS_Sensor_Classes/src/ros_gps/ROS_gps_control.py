#!/usr/bin/env python
 
import serial
import time
import sys
import rospy
from std_msgs.msg import Float32


port = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=1)
port.write('AT'+'\r\n')            
time.sleep(.1)
port.write('AT+CGNSPWR=1'+'\r\n')            
time.sleep(0.1)
port.write('AT+CGNSURC=2'+'\r\n') 

print ('-----------------------------------------------------------------GPS start')

try :
    while True :
     	time.sleep(0.1)
	rcv = port.read(200)
	print (rcv)
except (KeyboardInterrupt, SystemExit):
    sys.exit(0)

   