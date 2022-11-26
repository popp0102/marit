#!/usr/bin/env python3

from scapy.all import *
import sqlite3
import datetime
import random
import argparse

MACS = {}

def cmd_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="the network interface to sniff on", type=str, required=True)
    parser.add_argument("-d", "--duration", help="the duration, in seconds, for scan", type=int, required=True)

    args = parser.parse_args()
    return args

def collect_packets(packet):
    MACS[packet.src] = 1
    MACS[packet.dst] = 1

def write_to_db():
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

def main():
    args      = cmd_parse()
    interface = args.interface
    duration  = args.duration

    sniff(iface=interface, prn=collect_packets, store=0, timeout=duration)
    write_to_db()

if __name__ == "__main__":
    main()

