#!/usr/bin/env python3

from scapy.all import *
import pdb


def handler(packet):
  if packet.haslayer(Dot11):
    if packet.type == 1 and packet.subtype == 11:
        print("HI")
        pdb.set_trace()
        print("BYE")

if __name__ == "__main__":
    sniff(iface="en0", prn=handler, store=0, timeout=10, monitor=True)

