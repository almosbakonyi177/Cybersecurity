class ApplicationLayer:
    def __init__(self, message):
        self.message=message

    #Creates the body of the data packet
    def addData(self):
        return Packet()