from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
i2c_bus = busio.I2C(SCL,SDA)

pca =PCA9685(i2c_bus)

pca.frequency =  100

pca.channels[4].duty_cycle = 9830

time.sleep(3)

pca.channels[4].duty_cycle = 11141
pca.channels[5].duty_cycle = 6554
pca.channels[6].duty_cycle =6554
pca.channels[7].duty_cycle = 6554

time.sleep(3)

pca.channels[5].duty_cycle = 13108
pca.channels[6].duty_cycle =13108
pca.channels[7].duty_cycle = 13108

time.sleep(3)

pca.channels[4].duty_cycle = 9830
pca.channels[5].duty_cycle = 9830
pca.channels[6].duty_cycle =9830
pca.channels[7].duty_cycle =9830


