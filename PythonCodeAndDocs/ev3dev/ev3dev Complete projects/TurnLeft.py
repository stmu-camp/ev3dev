#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep    

lw = LargeMotor('outB') 
#assert lw.connected
rw = LargeMotor('outC') 
#assert rw.connected

rw.run_to_rel_pos(position_sp = 360, speed_sp = 700, stop_action = "hold")
sleep(5)