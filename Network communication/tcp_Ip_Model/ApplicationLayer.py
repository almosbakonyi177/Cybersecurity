from Packet import Packet
from Layer import Layer

class ApplicationLayer(Layer):
    def addData(self, packet) -> Packet:
        packetBody = packet.message
        return packet