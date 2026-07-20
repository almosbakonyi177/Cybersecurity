from Packet import Packet
from Layer import Layer

class NetworkAccessLayer(Layer):
    def __init__(self, MAC_address):
        self.MAC_address=MAC_address

    # Adds the MAC address to the package header
    def addData(self, packet) ->Packet:
        packet.addHeader("MAC address", self.MAC_address)

        return packet