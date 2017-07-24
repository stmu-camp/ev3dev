#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts



cl = ColorSensor()
assert cl.connected, "Connect a single EV3 color sensor to any sensor port"
assert TouchSensor().connected
cl.mode = 'COL-COLOR'
colors=('unknown, 0','black, 1','blue, 2','green, 3','yellow, 4','red, 5','white, 6','brown, 7')
while not TouchSensor().value(): # Stop program by pressing touch sensor button
    lcd = Screen()
    lcd.draw.text((15,15), colors[cl.value()], font = fonts.load('luBS14'))
    lcd.update()
    #Sound.speak(colors[cl.value()]).wait()
    sleep(1)


