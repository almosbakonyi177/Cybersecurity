class InternetLayer:
    def __init__(self, sourceIP):
        self.sourceIP=sourceIP
    
    #Adds the IP addresses to the package header
    def addData(self, packet, destinationIP):
        packet.addHeader(self.sourceIP)
        packet.addHeader(destinationIP)