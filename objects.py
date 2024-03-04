from math import cos,sin,pi
from matplotlib.pyplot import plot,show,xlim,ylim
#from matplotlib.animation import Animation

class environment:
    def __init__(self,size:list):
        self.size = size

class robot:
    def __init__(self, coordinates:list, alpha:float):
        self.coordinates = coordinates
        self.alpha = alpha
        self.x_values_list = [coordinates[0]]
        self.y_values_list = [coordinates[1]]

    def show_coordinates(self,ground:environment):
        if self.coordinates[0] > ground.size[0] or self.coordinates[1] > ground.size[1]:
            print("Error! Position out of range.")
        else:
            print(self.coordinates)

    
    def forward_move(self,dist,ground:environment):
        x_new = self.coordinates[0] + dist*cos(self.alpha)
        y_new = self.coordinates[1] + dist*sin(self.alpha)
        if 0 <= x_new <= ground.size[0] and 0 <= y_new <= ground.size[1]:
            self.coordinates = [x_new,y_new]
            self.x_values_list.append(self.coordinates[0])
            self.y_values_list.append(self.coordinates[1])
        else:
            print("Error")
    
    def turn_left(self,angle):
        self.alpha += angle
    
    def turn_right(self,angle):
        self.alpha -= angle 

    def trajectory(self,ground:environment):
        #xlim(ground.size[0])
        #ylim(ground.size[1])
        xlim((0,ground.size[0]))
        ylim((0,ground.size[1]))
        plot(self.x_values_list,self.y_values_list)
        show()