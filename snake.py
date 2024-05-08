import random

class Snake():
    def __init__(self, height: int, width: int) -> None:
        self.color = 'red'
        self.height = height
        self.width = width
        self.locations = [[0, 0]]
    
    def update_locations(self) -> None:
        self.locations.append([self.locations[-1][0] + random.randint(-1, 1), self.locations[-1][1] + random.randint(-1, 1)])
        self.locations.pop(0)
    
    def grow(self) -> None:
        self.locations.append([self.locations[-1][0] + random.randint(-1, 1), self.locations[-1][1] + random.randint(-1, 1)])