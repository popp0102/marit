#!/usr/bin/env python3

from scapy.all import *
import sqlite3
import datetime
import random


def handler(packet):
    value_src = ""
    value_dst = ""
    if IP in packet:
        value_src = packet[IP].src
        value_dst = packet[IP].dst

    MACS[packet.src] = value_src
    MACS[packet.dst] = value_dst

if __name__ == "__main__":
    sniff(iface="wlo1", prn=handler, store=0, timeout=20)
    frame.show()

# addr1 is target
dot11 = Dot11(type=1, subtype=11, addr1='ba:02:fc:15:47:3b', addr2='aa:bb:cc:dd:ee:ff')
dot11 = Dot11(type=1, subtype=11, addr1='aa:bb:cc:dd:ee:11', addr2='ba:02:fc:15:47:3b')

frame = RadioTap()/Dot11(type=1, subtype=11, addr1='ba:02:fc:15:47:3b', addr2='aa:bb:cc:dd:ee:11', ID=123)/Dot11Elt(ID="SSID", info="")
frame = RadioTap()/Dot11(type=1, subtype=11, addr1='ba:02:fc:15:47:3b', addr2='f4:f5:d8:cb:37:34', addr3='f4:f5:d8:cb:37:34')
sendp(frame, iface='wlo1')

dot11 = Dot11(type=1, subtype=11, addr1='11:11:11:11:11:11', addr2='22:22:22:22:22:22')
frame = RadioTap()/dot11
sendp(frame, iface='wlo1')

def PacketHandler(packet):
    if packet.haslayer(Dot11):
        print("--------------")
        print(packet.summary())
        print("****************")
        print(packet.show())
        print("--------------")

sniff(iface='wlo1', prn=PacketHandler)
