# PROJECT: SIMULATION ROBOT MOVEMENT IN 2D SPACE


## OBJECTIVE
This project simulates a simple robot moving in a 2D environment using Python. The robot is represented as a point with an orientation (facing angle) that can move forward, backward, turn left, and turn right based on commands. The program allows you to experiment with various movement scenarios and visualize the robot's path.

## ROBOT'S KINEMATICS
The robot's location in the 2D space is defined by its x and y coordinates. Since it can change its direction (orientation), we also consider its orientation angle alpha in radians. The relationship between the robot's orientation and its coordinates is determined using trigonometry:
`` x = d*cos(alpha)`` and ``y = d*sin(alpha)``.

Here, ``cos(alpha)`` and ``sin(alpha)`` represent the cosine and sine of the orientation angle, respectively. These functions are used to calculate the robot's new position based on the movement distance (``d``) and its current orientation.

## ENVIRONMENT DEFINITION
The robot operates within a designated area represented by the ``environment`` class. This class stores the environment's size as a list containing the width and height limits.
```
class environment:
    def __init__(self,size:list):
        self.size = size

```

## ROBOT OBJECT AND MOVEMENT
The core functionality lies within the ``robot`` class. This class represents the robot itself and keeps track of its position and orientation. When creating a ``robot`` object, you specify its initial coordinates and orientation angle. The class also maintains two lists, ``x_values_list`` and ``y_values_list``, to record the robot's trajectory (all visited x and y coordinates).

The ``robot`` class offers various methods to simulate movement and access information:

* ``show_coordinates(ground)`` :
This method checks if the robot's current position is within the environment's boundaries and prints the coordinates if valid.

* ``forward_move(dist, ground)``: 
This method simulates forward movement. It takes the movement distance (``dist``) and checks if the new position stays within the environment's limits. If valid, it updates the robot's coordinates and appends the new values to the trajectory lists.

* ``turn_left(angle)`` and ``turn_right(angle)``: 
These methods update the robot's orientation angle (``alpha``) by adding or subtracting the specified angle (in radians).

* ``trajectory(ground)``:
This method visualizes the robot's path using Matplotlib. It sets the plot boundaries according to the environment's size and plots the robot's trajectory stored in x_values_list and y_values_list.


## RUNNING THE SIMULATION
* Save the code in two separate files: objects.py and main.py.

* Open a terminal or command prompt and navigate to the directory containing these files.
Run the simulation using the command: python main.py.

* This will execute the code in main.py, simulate the robot's movements based on the defined commands, and display the robot's final trajectory on a graph. Feel free to modify the main.py script to experiment with different movement scenarios and observe the robot's path.