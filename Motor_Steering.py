#!/usr/bin/env python
import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo

def Sero_Motor_Initialization():
    
    # Libaries provide by Adafruit
    # https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
    # https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
    
    # Create busio i2C bus instance to communicate with driver.
    i2c_bus = busio.I2C(5,3)
    # Start Communicating with Driver
    pca =PCA9685(i2c_bus)
    # Set Frequency
    pca.frequency =  100
    #kit = ServoKit(channels=16)
   
    return pca
    

def Motor_Start(pca):
    # This function set the servo broad to min pwm to run.
    # Motor is always set to channel 7 of the broad.
    pca.channels[7].duty_cycle = 9830
    
def Motor_Speed(pca,percent):
    # Converts a -1 to 1 value to 16-bit duty cycle
    # 20% full forward
    # 15% corresponds to zero speed
    # 10% full reverse
    speed = (percent*3276) + 65535 * 0.15
    pca.channels[7].duty_cycle = math.floor(speed)


     
def Steering(pca,angle):
    # Limiting
    if angle >180:
        angle = 180
    if angle < 0:
        angle = 0
    # Converts to 16-bit duty between 10% and 20%    
    duty = ((angle/180)*6553)+6553
    pca.channels[6].duty_cycle= math.floor(duty)
    
def Pan(pca,angle):
    #Limits and center range
    offset =10
    if angle > 180:
        angle =180
    if angle < 20:
        angle =20
    # Apply offset and convert
    duty = (((angle+offset)/180)*6553)+6553
    pca.channels[4].duty_cycle= math.floor(duty)
       
def Tilt(pca,angle):
     #Limits and center range
    offset = 20
    if angle > 170:
        angle =170
    if angle < 30:
        angle =30
    # Apply offset and convert    
    duty = (((angle+offset)/180)*6553)+6553
    pca.channels[5].duty_cycle= math.floor(duty)
    

pca=Sero_Motor_Initialization()
Motor_Start(pca)
Motor_Speed(pca,0) 
Steering(pca,90)
Tilt(pca,90)
Pan(pca,90)
Motor_Speed_Backwards(pca,0)
i =0
while i <20:
    Motor_Speed(pca,i*0.01)
    time.sleep(1)
    i = i+1
Motor_Speed(pca,0)
kit.servo[6].angle = 90