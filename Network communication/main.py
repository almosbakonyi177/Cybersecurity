from Packet import Packet
data_packet=Packet("Try out!","192.168.0.0","10.0.0.5")
data_packet.addHeader("80")
data_packet.addHeader("00:1A:2H:3K:4D:5E")

print(data_packet.packet_read())