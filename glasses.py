import zmq
import msgpack
import numpy as np

class Glasses:
    def __init__(self) -> None:
        self.pupil_remote = None
        self.subscriber = None
        self.pupil_capture_process = None
    
    def get_packet(self) -> any:
        topic, payload = self.subscriber.recv_multipart()
        message = msgpack.loads(payload)
        return message['norm_pos']
    
    def initialize_connection(self) -> None:
        ctx = zmq.Context()
        self.pupil_remote = zmq.Socket(ctx, zmq.REQ)
        ip = 'localhost'
        port = 50020
        self.pupil_remote.connect(f'tcp://{ip}:{port}')
        self.pupil_remote.send_string('SUB_PORT')
        sub_port = self.pupil_remote.recv_string()

        self.pupil_remote.send_string('PUB_PORT')
        self.pupil_remote.recv_string()

        self.subscriber = ctx.socket(zmq.SUB)
        self.subscriber.connect(f'tcp://{ip}:{sub_port}')
        self.subscriber.subscribe('gaze.')