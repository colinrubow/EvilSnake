import serial
import time

class Arduino:
    def __init__(self) -> None:
        self.arduino = serial.Serial(port='COM7', baudrate=115200, timeout=0.1)
        self.arduino.read_all()
    
    def write_read(self) -> list[int, int]:
        data = ['', '']
        while '' in data or 'nan' in data:
            self.arduino.write(bytes('1', 'utf-8'))
            time.sleep(0.01)

            data_x = self.arduino.readline().decode().strip()
            data_y = self.arduino.readline().decode().strip()

            data = [data_x, data_y]

        return data