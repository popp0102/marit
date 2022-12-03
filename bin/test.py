#!/usr/bin/env python3

from scapy.all import *
pixel4_global     = 'f0:5c:77:b9:a8:6a'
pixel7_randomized = 'ba:02:fc:15:47:3b'
pixel7_global     = 'd4:3a:2c:9a:41:15'
gateway           = 'cc:f4:11:38:15:a0'
ubuntu            = '40:ec:99:0f:9a:65'
grimlock          = '88:e9:fe:5e:3d:1e'
irobot            = '50:14:79:4a:71:15'
spoofed           = '11:22:33:15:25:35'
samsung_global    = 'd8:68:c3:ba:49:ef'
samsung_random    = 'd8:68:c3:ba:49:ef'
rando             = 'd0:73:d5:23:99:e8'

sender        = spoofed
receiver      = irobot
conf.use_pcap = True
monitor       = True
iface         = 'wlo1'
duration      = Dot11(raw(Dot11(ID=struct.unpack(">H", struct.pack("<H", 100))[0]))).ID
#duration      = Dot11(raw(Dot11(ID=struct.unpack(">H", struct.pack("<H", 35595))[0]))).ID
dot11         = Dot11(type=1, subtype=11, addr1=receiver, addr2=sender, ID=duration)

frame = RadioTap()/dot11
frame.show()
print("\nHexdump of frame:")
hexdump(frame)
input("\nPress enter to start\n")
sendp(frame, iface=iface, inter=1.0, loop=1)


