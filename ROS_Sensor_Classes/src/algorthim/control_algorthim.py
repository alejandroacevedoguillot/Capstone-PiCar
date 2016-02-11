#!/usr/bin/env python
import rospy
from i2cpwm_board.msg import Servo, ServoArray
from geometry_msgs.msg import Twist
import time



class motor():
    def __init__(self):
        rospy.init_node('motor', anonymous=True)
        self.speed_publisher = rospy.Publisher("/servos_absolute",ServoArray, queue_size=1)
        self.r = rospy.Rate(15)

        


car=motor()
time.sleep(0.5)
speed =605
print ('-----------------------------------------------------------------Algorthim')
try :
	while True :
		if speed > 720:
			speed = 605
		else:
			speed = speed +10
		car.speed_publisher(Servo[])
		car.r.sleep()
        
except (KeyboardInterrupt, SystemExit):
	sys.exit(0)