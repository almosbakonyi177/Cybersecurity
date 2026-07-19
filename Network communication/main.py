from Device import Device

device = Device("192.00.15","1A:2B:3C")
dataPacket=device.send("Tryout","00.198.00.11", "401", "102")

print(dataPacket.packet_read())