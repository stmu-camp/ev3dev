#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep
import sys
ts = TouchSensor() ; assert ts.connected


def Screen1():
  lcd = Screen()
  lcd.draw.text((15,10), "Hello", font = fonts.load('luBS14'))
  lcd.update()
  sleep(2)
def Screen2():
  lcd = Screen()
  lcd.draw.text((15,20), "My name", font = fonts.load('luBS14'))
  lcd.update()
  sleep(2)
  
while not ts.value():
  Screen1()
  Screen2()
  sys.exit()
  