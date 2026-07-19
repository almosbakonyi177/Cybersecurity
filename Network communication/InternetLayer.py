from Packet import Packet
from Layer import Layer

class InternetLayer(Layer):
    def __init__(self, sourceIP, destinationIP):
        self.sourceIP=sourceIP
        self.destinationIP=destinationIP
    
    #Adds the IP addresses to the package header
    def addData(self, packet) -> Packet:
        packet.addHeader(self.sourceIP)
        packet.addHeader(self.destinationIP)

        return packet