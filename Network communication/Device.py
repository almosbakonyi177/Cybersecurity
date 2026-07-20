from Packet import Packet
from ApplicationLayer import ApplicationLayer
from TransportationLayer import TransportationLayer
from InternetLayer import InternetLayer
from NetworkAccessLayer import NetworkAccessLayer

class Device:
    def __init__(self, IPaddess, macAddress):
        self.IPaddess=IPaddess
        self.macAddress=macAddress

    def send(self, message, destinationIP, sourcePort, destinationPort):
        packet = Packet(message)

        layers=[ApplicationLayer(),
                TransportationLayer(sourcePort, destinationPort),
                InternetLayer(self.IPaddess, destinationIP),
                NetworkAccessLayer(self.macAddress)]
        
        # Goes through on all layers and each layer adds its own part
        # to the data packet
        for layer in layers:
            packet=layer.addData(packet)

        return packet