import numpy as np

class Avatar():
    def __init__(self, height: int, width: int, color: str = 'blue', radius: int = 5) -> None:
        self.color = color
        self.height = height
        self.width = width
        self.location = np.array([width/2, height/2], int)
        self.radius = radius
    
    def update_location(self, direction: int) -> None:
        match direction:
            case 0:
                self.location = self.location + np.array([0, -1])
            case 1:
                self.location = self.location + np.array([1, 0])
            case 2:
                self.location = self.location + np.array([0, 1])
            case 3:
                self.location = self.location + np.array([-1, 0])
        self.location = self.location%np.array([self.width, self.height])