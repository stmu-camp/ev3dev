#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
import sys  
  
#Sound.tone([(3000, 2000, 400),(800, 1800, 2000)]).wait()
def Sing():  
  Sound.tone([(523.25,500,0), (587.33,500,0),(659.25,500,0), (523.25,500,0), (523.25,500,0),(587.33,500,0),(659.25,500,0), (523.25,500,500),\
 (659.25,500,0), (698.46,500,0), (783.99, 500, 500), (659.25,500,0), (698.46,500,0), (783.99, 500, 500), \
 (783.99,250,0), (880.00,250,0),(783.99,250,0), (698.46,250,0), (659.25,500,0), (523.25,250,250),\
 (783.99,250,0), (880.00,250,0),(783.99,250,0), (698.46,250,0), (659.25,500,0), (523.25,250,250),\
 (523.25,500,0), (392.00, 500, 0), (523.25,500,500), \
 (523.25,500,0), (392.00, 500, 0), (523.25,500,500)]).wait()

Sing()