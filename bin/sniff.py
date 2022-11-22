#!/usr/bin/env python3

from scapy.all import *
import sqlite3
import datetime
import random

MACS = {}

def handler(packet):
    MACS[packet.src] = 1
    MACS[packet.dst] = 1

if __name__ == "__main__":
    sniff(iface="wlo1", prn=handler, store=0, timeout=10)
    conn = sqlite3.connect('./db/development.sqlite3')
    cur  = conn.cursor()
    now  = str(datetime.datetime.now())
    name = "scan-" + str(random.randrange(1000000))
    for mac, valud in MACS.items():
        try:
            cur.execute('INSERT INTO network_devices(mac_address, name, created_at, updated_at) VALUES(?,?,?,?)',
                       (mac, name, now, now))
        except sqlite3.IntegrityError as e:
            pass
    conn.commit()

