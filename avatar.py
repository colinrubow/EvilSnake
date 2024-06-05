from glasses import Glasses
import numpy as np

class Avatar():
    def __init__(self, height: int, width: int, color: str = 'blue', radius: int = 5) -> None:
        self.glasses = Glasses()
        self.glasses.initialize_connection()
        print('connected to glasses')
        self.color = color
        self.height = height
        self.width = width
        self.location = np.array([width/2, height/2], int)
        self.radius = radius
    
    def update_location(self) -> None:
        x, y = self.glasses.get_packet()
        self.location = np.array([int(x*self.width), int((1-y)*self.height)])