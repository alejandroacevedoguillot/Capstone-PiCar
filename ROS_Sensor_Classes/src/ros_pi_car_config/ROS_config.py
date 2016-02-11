#!/usr/bin/env python
import subprocess
subprocess.call(["rosservice call /raspicam_node/start_capture "], shell=True)
subprocess.call([ 'rosservice call /set_pwm_frequency "value: 100" '], shell=True)
subprocess.call([ 'rosservice call /config_servos "servos: [{servo: 4, center: 605, range: 200, direction: 1}, {servo: 5, center: 605, range: 200, direction: 1}, {servo: 6, center: 605, range: 200, direction: 1}, {servo: 7, center: 605, range: 200, direction: 1}]" '], shell=True)




