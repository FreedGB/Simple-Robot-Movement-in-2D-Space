from math import cos,sin,pi

class environment:
    def __init__(self,size:tuple):
        self.size = size

class robot:
    def __init__(self, coordinates:list, alpha:float):
        self.coordinates = coordinates
        self.alpha = alpha

    
    def forward_move(self,dist):
        self.coordinates[0] += dist*cos(self.alpha)
        self.coordinates[1] += dist*sin(self.alpha)
    
    def turn_left(self,angle):
        self.alpha += angle
    
    def turn_right(self,angle):
        self.alpha -= angle