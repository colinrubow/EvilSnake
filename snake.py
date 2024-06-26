import random
import numpy as np

class Snake():
    def __init__(self, height: int, width: int, color: str = 'red', radius: int = 5) -> None:
        self.color = color
        self.height = height
        self.width = width
        self.locations = [np.array([0, i], int) for i in range(25)]
        self.radius = radius
        self.i = 100
        self.direction = np.array([0, 1], int)
        self.directions = [np.array([0, 1], int), np.array([1, 1], int), np.array([1, 0], int), np.array([1, -1], int), np.array([0, -1], int), np.array([-1, -1], int), np.array([-1, 0], int), np.array([-1, 1], int)]
        self.speed = 2
    
    def update_locations(self) -> None:
        self.i = self.i - 1
        if self.i == 0:
            self.i = random.randint(0, 200)
            self.direction = random.choice(self.directions)
        self.locations.append(np.array([(self.locations[-1][0] + self.direction[0]*self.speed)%self.width, (self.locations[-1][1] + self.direction[1]*self.speed)%self.height], int))
        self.locations.pop(0)
    
    def grow(self) -> None:
        for _ in range(int(0.1*self.locations.__len__())):
            self.locations.append(np.array([(self.locations[-1][0] + self.direction[0]*self.speed)%self.width, (self.locations[-1][1] + self.direction[1]*self.speed)%self.height], int))