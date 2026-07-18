class Packet:
    def __init__(self, message, sourceIP, destinationIP):
        self.message=message
        self.sourceIP=sourceIP
        self.destinationIP=destinationIP
        self.header=[]

    def addHeader(self, newHeader):
        self.header.append(newHeader)
        print(f"Header added {newHeader}")
    
    def packet_read(self):
        return f"[{self.sourceIP} -> {self.destinationIP}] message:{self.message}"