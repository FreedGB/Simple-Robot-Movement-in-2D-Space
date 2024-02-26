from objects import *
from math import sqrt

test_robot = robot([0,0],pi/2)
test_ground = environment([10,10])

def show_coordinates(a_robot):
    if a_robot.coordinates[0] > test_ground.size[0] or a_robot.coordinates[1] > test_ground.size[1]:
        print("Error! Position out of range.")
    else:
        print(a_robot.coordinates)


test_robot.forward_move(11)
show_coordinates(test_robot)

#print(sqrt((test_robot.coordinates[0])**2 + (test_robot.coordinates[1])**2))