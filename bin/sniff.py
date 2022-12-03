#!/usr/bin/env python3

from scapy.all import *
import sqlite3
import datetime
import random

MACS = {}

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
    conn = sqlite3.connect('./db/development.sqlite3')
    cur  = conn.cursor()
    now  = str(datetime.datetime.now())
    name = "scan-" + str(random.randrange(1000000))
    for mac, ip in MACS.items():
        try:
            cur.execute('INSERT INTO network_devices(mac_address, ip_address, name, created_at, updated_at, detected_at) VALUES(?,?,?,?,?,?)',
                       (mac, ip, name, now, now, now))
        except sqlite3.IntegrityError as e:
            print("Error: " + str(e))
            cur.execute('UPDATE network_devices SET detected_at=? WHERE mac_address=?', (now, mac))
    conn.commit()

