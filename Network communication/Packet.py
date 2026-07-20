class Packet:
    def __init__(self, message):
        self.message=message
        self.header=[]

    def addHeader(self, headerType, newHeader):
        self.header.append(newHeader)
        print(f"{headerType} added: {newHeader}")
    
    def packet_read(self):
        return f"Header: {self.header}\nBody:'{self.message}'"