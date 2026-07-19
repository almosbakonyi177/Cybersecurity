class Packet:
    def __init__(self, message):
        self.message=message
        self.header=[]

    def addHeader(self, newHeader):
        self.header.append(newHeader)
        print(f"Header added {newHeader}")
    
    def packet_read(self):
        return f"Header:[{self.header}\nBody:{self.message}"