#!/usr/bin/env python3 
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
from math import pi
import sys

ts = TouchSensor() ; assert ts.connected

#We can write two commands on the same line using semicolon
#assert ts.connected will automatically set up the TouchSensor connection

for i in range(50):
  if ts.is_pressed == True:
    print("True")
    sleep(0.5)
  else:
    print("False")
    sleep(0.5)

sys.exit()






