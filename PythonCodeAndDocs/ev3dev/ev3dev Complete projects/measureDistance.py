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
lw.position = 0
while not cs.value() == 5:
  lw.run_forever(speed_sp = 500)
  rw.run_forever(speed_sp = 500)
  if cs.value() == 5:
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    x = lw.position*pi*5.6/360
    lcd = Screen()
    lcd.draw.text((15,10), str(round(x,2)) + " cm", font = fonts.load('luBS14'))
    lcd.update()
    sleep(2)
    break

while not cs.value() == 4:
  lw.run_forever(speed_sp = 500)
  rw.run_forever(speed_sp = 500)
  if cs.value() == 4:
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    y = lw.position*pi*5.6/360
    lcd.draw.text((15, 20), str(round(y,2)) + " cm", font = fonts.load('luBS14'))
    lcd.update()
    sleep(2)
    break
    
while not cs.value() == 5:
  lw.run_forever(speed_sp = 500)
  rw.run_forever(speed_sp = 500)
  if cs.value() == 5:
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    z = lw.position*pi*5.6/360
    lcd.draw.text((15,30), str(round(z,2)) + " cm", font = fonts.load('luBS14'))
    lcd.update()
    sleep(2)
    break

while not cs.value() == 1: 
  lw.run_forever(speed_sp = -500)
  rw.run_forever(speed_sp = -500)
  if cs.value() == 1: 
    lw.stop(stop_action = 'hold')
    rw.stop(stop_action = 'hold')
    sys.exit()
#lw.run_to_rel_pos(position_sp = -z, speed_sp = 700, stop_action = 'coast')
#rw.run_to_rel_pos(position_sp = -z, speed_sp = 700, stop_action = 'coast')    
#sleep(6)


