#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep    
import ev3dev.fonts as fonts    #to access fonts.load() function 

cs = ColorSensor() ; assert cs.connected    #setup color sensor and automatically assert the sensor
ts = TouchSensor() ; assert ts.connected    #setup touch sensor and automatically assert the sensor

lw = LargeMotor('outB')
lw.position = 0
while not ts.value():
  lcd = Screen()
  lcd.draw.text((15,15), str(lw.position),font=fonts.load('luBS14'))
  lcd.update()
  