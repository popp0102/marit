#!/usr/bin/env python3

from scapy.all import *
import sqlite3

MACS = {}

def handler(packet):
    MACS[packet.src] = 1
    MACS[packet.dst] = 1

if __name__ == "__main__":
    sniff(iface="wlo1", prn=handler, store=0, timeout=10)
    conn = sqlite3.connect('./db/development.sqlite3')
    cur  = conn.cursor()
    for mac, valud in MACS.items():
        cur.execute('INSERT INTO network_devices(mac_address, name, created_at, updated_at) VALUES(?,?,?,?)', (mac,'hi', '2022-11-22', '2022-11-22'))
    conn.commit()

