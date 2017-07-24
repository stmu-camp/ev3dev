#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts    #to access fonts.load() function
from PIL import Image, ImageDraw, ImageFont  #just for fun
lw = LargeMotor('outB')
#assert lw.connected
rw = LargeMotor('outC')
#assert rw.connected
cs = ColorSensor()
assert cs.connected
#ts = TouchSensor()

lcd = Screen()    #initiate the screen
lcd.draw.text((15,15), "Project 1", font=fonts.load('luBS14'))    # luBS14 font which is bold, sans serif and size 14
  #https://sites.google.com/site/ev3python/learn_ev3_python/screen
lcd.update()      #upload on the screen
sleep(2)          #wait for 1 second. sleep() function must be imported
x = 0
while x < 4:
  if cs.value() > 20:
    lw.run_forever(speed_sp = 700)
    rw.run_forever(speed_sp = 700)
  if cs.value() < 20:
    lw.stop(stop_action = "hold")
    rw.stop(stop_action = "hold")
    sleep(2)
    rw.run_to_rel_pos(position_sp = 360, speed_sp = 700, stop_action = "hold")
    sleep(5)
    x += 1

sleep(2)
