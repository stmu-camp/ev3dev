#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep    
import ev3dev.fonts as fonts    #to access fonts.load() function 

cs = ColorSensor() ; assert cs.connected    #setup color sensor and automatically assert the sensor
cl.mode= 'COL-REFLECT'
ts = TouchSensor() ; assert ts.connected    #setup touch sensor and automatically assert the sensor

while not ts.value():
  lcd = Screen()    #initiate the screen  
  lcd.draw.text((15,15), str(cs.value()), font=fonts.load('luBS14')) # luBS14 font which is bold, sans serif and size 14
  #https://sites.google.com/site/ev3python/learn_ev3_python/screen
  lcd.update()      #upload on the screen
  sleep(1)          #wait for 1 second. sleep() function must be imported 
  
