class TransportLayer:
    def __init__(self, sourcePort, destinationPort):
        self.sourcePort=sourcePort
        self.destinationPort=destinationPort

    #Adds the port numbers to the package header
    def addData(self, packet):
        packet.addHeader(self.sourcePort)
        packet.addHeader(self.destinationPort)