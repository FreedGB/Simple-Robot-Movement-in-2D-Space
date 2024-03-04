from objects import *
from math import sqrt


test_robot = robot([0,0],pi/3)
test_ground = environment([10,10])


test_robot.forward_move(6,test_ground)
test_robot.show_coordinates(test_ground)

test_robot.turn_right(pi/2)

test_robot.forward_move(-1,test_ground)
test_robot.show_coordinates(test_ground)

test_robot.turn_right(pi/6)

test_robot.forward_move(-10,test_ground)
test_robot.show_coordinates(test_ground)

test_robot.forward_move(11,test_ground)
test_robot.show_coordinates(test_ground)

print(test_robot.x_values_list)
print(test_robot.y_values_list)

test_robot.trajectory(test_ground)


#print(sqrt((test_robot.coordinates[0])**2 + (test_robot.coordinates[1])**2))