#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep
import sys
ts = TouchSensor() ; assert ts.connected

  
#while not ts.value():
#  lcd = Screen()
#  lcd.draw.text((10,10), str(x), font = fonts.load('luBS14'))
#  lcd.update()
#  lcd.draw.text((10,23), str(y), font = fonts.load('luBS14'))
#  lcd.update()
#  sleep(5)
#  sys.exit()

while not ts.value():
  print("Hello")
  print("Goodjob")
  sleep(3)
#  sys.exit()
  break


while not ts.value():
  print("second line")
  print("Second Line")
  sleep(4)
  sys.exit()