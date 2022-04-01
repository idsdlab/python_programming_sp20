# lec2.py

from cs1robots import *

create_world()

# create a robot with one beeper
hubo = Robot(beepers = 1)

# move one step forward
for _ in range(8):
    hubo.move()
hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

turn_right()













