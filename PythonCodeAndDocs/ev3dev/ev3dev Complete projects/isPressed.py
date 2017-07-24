#!/usr/bin/env python3 
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
from math import pi
import sys

ts = TouchSensor() ; assert ts.connected
#cs = ColorSensor() ; assert cs.connected
#cs.mode = 'COL-COLOR'
lw = LargeMotor('outB')
rw = LargeMotor('outC')
us = UltrasonicSensor()
assert us.connected
us.mode = 'US-DIST-CM'

for i in range(50):
  if ts.is_pressed == True:
    print("True")
    sleep(0.5)
  else:
    print("False")
    sleep(0.5)