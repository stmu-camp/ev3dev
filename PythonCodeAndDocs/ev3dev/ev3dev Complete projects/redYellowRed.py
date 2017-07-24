#!/usr/bin/env python3
from ev3dev.ev3 import*
from time import sleep
import ev3dev.fonts as fonts

lw = LargeMotor('outB')
rw = LargeMotor('outC')

cs = ColorSensor() ; assert cs.connected
cs.mode = 'COL-COLOR'

ts = TouchSensor() ; assert ts.connected

for i in range(3):
  while not cs.value() == 4:
#    lw.stop(stop_action = 'hold')
#    rw.stop(stop_action = 'hold')
#    sleep(0.5)
    lw.run_forever(speed_sp = 700)
    rw.run_forever(speed_sp = 700)
  while not cs.value() == 5:
#    lw.stop(stop_action = 'hold')
#    rw.stop(stop_action = 'hold')
#    sleep(0.5)
    lw.run_forever(speed_sp = 400)
    rw.run_forever(speed_sp = 400)
  while not cs.value() == 4:
#    lw.stop(stop_action = 'hold')
#    rw.stop(stop_action = 'hold')
#    sleep(0.5)
    lw.run_forever(speed_sp = -700)
    rw.run_forever(speed_sp = -700)
  while not cs.value() == 5:
#    lw.stop(stop_action = 'hold')
#    rw.stop(stop_action = 'hold')
#    sleep(0.5)
    lw.run_forever(speed_sp = -400)
    rw.run_forever(speed_sp = -400)