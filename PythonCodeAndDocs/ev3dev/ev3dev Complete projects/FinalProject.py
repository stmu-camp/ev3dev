#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
import sys

ts = TouchSensor() ; assert ts.connected
lw = LargeMotor('outB')
rw = LargeMotor('outC')
us = UltrasonicSensor() ; assert us.connected
us.mode = "US-DIST-CM"
units = us.units

def Dance():
  Sound.tone([(523.25,500,0), (587.33,500,0),(659.25,500,0), (523.25,500,0), (523.25,500,0),(587.33,500,0),(659.25,500,0), (523.25,500,500),\
 (659.25,500,0), (698.46,500,0), (783.99, 500, 500), (659.25,500,0), (698.46,500,0), (783.99, 500, 500), \
 (783.99,250,0), (880.00,250,0),(783.99,250,0), (698.46,250,0), (659.25,500,0), (523.25,250,250),\
 (783.99,250,0), (880.00,250,0),(783.99,250,0), (698.46,250,0), (659.25,500,0), (523.25,250,250),\
 (523.25,500,0), (392.00, 500, 0), (523.25,500,500), \
 (523.25,500,0), (392.00, 500, 0), (523.25,500,500)]).wait()

while ts.value() == 0:
  lw.run_forever(speed_sp = 700)
  rw.run_forever(speed_sp = 700)
  sleep(0.01)
  if ts.value() == 1:
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    sleep(1)
    break

lw.run_to_rel_pos(position_sp = -360, speed_sp = 700, stop_action = 'hold')
rw.run_to_rel_pos(position_sp = -360, speed_sp = 700, stop_action = 'hold')
lw.wait_while('running')
rw.wait_while('running')
sleep(1)

#turn left
rw.run_to_rel_pos(position_sp = 360, speed_sp = 600, stop_action = 'hold')
rw.wait_while('running')
sleep(1)
while us.value() < 600:
  lw.run_forever(speed_sp = 700)
  rw.run_forever(speed_sp = 700)
  sleep(0.01)
  if us.value() > 600:
    sleep(0.2)
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')    
    break
        
lw.run_to_rel_pos(position_sp = 380, speed_sp = 600, stop_action = 'hold')
lw.wait_while('running')
rw.run_to_rel_pos(position_sp = -70, speed_sp = 600, stop_action = 'hold')
rw.wait_while('running')
sleep(2)

while ts.value() == 0:
  lw.run_forever(speed_sp = 700)
  rw.run_forever(speed_sp = 700)
  sleep(0.1)
  if ts.value() == 1:
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    sleep(1)
    break

while us.value() > 600:
  lw.run_forever(speed_sp = -720)
  rw.run_forever(speed_sp = -700)
  sleep(0.1)
  if us.value() < 600:
    lw.run_to_rel_pos(position_sp = -1600, speed_sp = 700, stop_action = 'hold')
    rw.run_to_rel_pos(position_sp = -1600, speed_sp = 700, stop_action = 'hold')    
    lw.wait_while('running')
    rw.wait_while('running')
    sleep(2)
    Dance()  
    sys.exit()
