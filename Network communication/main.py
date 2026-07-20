from Device import Device

device = Device("192.00.15","1A:2B:3C")
secureInternetConnectionDataPacket=device.send("Tryout","00.198.00.11", "443", "443")
print("\n")
emailDataPacket=device.send("Tryout","00.198.00.11", "25", "25")

print(secureInternetConnectionDataPacket.packet_read(),"\n")
print(emailDataPacket.packet_read())