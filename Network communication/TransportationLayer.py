from Packet import Packet
from Layer import Layer

class TransportationLayer(Layer):
    def __init__(self, sourcePort, destinationPort):
        self.sourcePort=sourcePort
        self.destinationPort=destinationPort

    # Adds the port numbers to the package header
    def addData(self, packet) -> Packet:
        packet.addHeader("Source port", self.sourcePort)
        packet.addHeader("Destination port", self.destinationPort)

        return packet