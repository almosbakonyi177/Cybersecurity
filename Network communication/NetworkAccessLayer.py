class NetworkAccessLayer:
    def __init__(self, MAC_address):
        self.MAC_address=MAC_address

    #Adds the MAC address to the package header
    def addData(self, packet):
        packet.addHeader(self.MAC_address)