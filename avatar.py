from arduino import Arduino

class Avatar():
    def __init__(self, height: int, width: int) -> None:
        self.ino = Arduino()
        self.color = 'blue'
        self.height = height
        self.width = width
        self.location = [int(height/2), int(width)/2]
    
    def update_location(self) -> None:
        self.location = self.ino.write_read()