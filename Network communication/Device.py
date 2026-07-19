from Packet import Packet
from ApplicationLayer import ApplicationLayer
from TransportLayer import TransportLayer
from InternetLayer import InternetLayer
from NetworkAccessLayer import NetworkAccessLayer

class Device:
    def __init__(self, IPaddess, macAddress):
        self.IPaddess=IPaddess
        self.macAddress=macAddress

    def send(self, message, destinationIP, sourcePort, destinationPort):
        packet = Packet(message)

        layers=[ApplicationLayer(),
                TransportLayer(sourcePort, destinationPort),
                InternetLayer(self.IPaddess, destinationIP),
                NetworkAccessLayer(self.macAddress)]
        
        for layer in layers:
            packet=layer.addData(packet)

        return packet