#!/usr/bin/env python3

from scapy.all import *
import pdb

conf.use_pcap = True
monitor       = True

def handler(packet):
    print(packet.type)
    if packet.haslayer(Dot11):
        if packet.type == 1 and packet.subtype == 11:
            pdb.set_trace()
            print("HI")

if __name__ == "__main__":
    sniff(iface="wlo1", prn=handler, monitor=True)

