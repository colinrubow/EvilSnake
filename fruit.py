import random
import numpy as np

class Fruit():
    def __init__(self, height: int, width: int, color: str = 'green', radius: int = 7) -> None:
        self.color = color
        self.height = height
        self.width = width
        self.location = np.array([random.randint(0, width-20), random.randint(0, height-20)])
        self.radius = radius

    def update_location(self) -> None:
        self.location = np.array([random.randint(0, self.width-10), random.randint(0, self.height-10)])