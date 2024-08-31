from arduino import Arduino
import numpy as np

class Avatar():
    def __init__(self, height: int, width: int, color: str = 'blue', radius: int = 5) -> None:
        self.ino = Arduino()
        print('connected to ino')
        self.color = color
        self.height = height
        self.width = width
        self.location = np.array([width/2, height/2], int)
        self.radius = radius
    
    def update_location(self) -> None:
        x, y = self.ino.write_read()
        self.location = np.array([((int(x)-8)/989)*self.width, (1 - (int(y)-9)/1006)*self.height], int)