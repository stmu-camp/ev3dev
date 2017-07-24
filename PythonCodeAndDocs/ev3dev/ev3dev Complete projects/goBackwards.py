#!/usr/bin/env python3 
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
from math import pi
import sys

# Red is 5, Yellow is 4
ts = TouchSensor() ; assert ts.connected
cs = ColorSensor() ; assert cs.connected
cs.mode = 'COL-COLOR'
lw = LargeMotor('outB')
rw = LargeMotor('outC')
x = 400
lw.run_to_rel_pos(position_sp = -x, speed_sp = 500, stop_action = 'coast')
sleep(6)
sys.exit()