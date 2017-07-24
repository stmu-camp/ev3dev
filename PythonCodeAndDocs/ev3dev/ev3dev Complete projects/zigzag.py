#!/usr/bin/env python3

from ev3dev.ev3 import * 
from time import sleep

lw = LargeMotor('outB')
rw = LargeMotor('outC')

ts = TouchSensor()
assert ts.connected
cs = ColorSensor()
assert cs.connected
cs.mode = 'COL-REFLECT'

def turnLeft():
  lw.run_forever(speed_sp = 400)
  rw.run_forever(speed_sp = 700)
  
def turnRight():
  lw.run_forever(speed_sp = 700)
  rw.run_forever(speed_sp = 400)
  
while not ts.value():
  if cs.value() > 30:
    turnLeft()
  if cs.value() < 30:
    turnRight()