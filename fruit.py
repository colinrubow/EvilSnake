import random

class Fruit():
    def __init__(self, height: int, width: int) -> None:
        self.color = 'green'
        self.height = height
        self.width = width
        self.location = [random.randint(0, height-1), random.randint(0, width-1)]

    def update_location(self) -> None:
        self.location = [random.randint(0, self.height-1), random.randint(0, self.width-1)]