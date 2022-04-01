# lec2.py

from cs1robots import *

create_world()

# create a robot with one beeper
hubo = Robot(beepers = 1)

hubo.move()
# hubo.turn_left()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def climb_up_four_stairs():
    climb_up_one_stairs()
    climb_up_one_stairs()
    climb_up_one_stairs()
    climb_up_one_stairs()

def clib_up_one_stairs():
    hubo.turn_left()
    hubo.move()
    hubo.turn_right()
    hubo.move()
    hubo.move()





