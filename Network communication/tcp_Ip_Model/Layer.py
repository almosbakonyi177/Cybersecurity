from Packet import Packet
from abc import ABC

class Layer(ABC):
    # Interface for all layers

    def addData(self, packet) -> Packet:
        raise NotImplementedError