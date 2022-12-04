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
    ip_src = ""
    ip_dst = ""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

    MACS[packet.src] = ip_src
    MACS[packet.dst] = ip_dst

def write_to_db(interface):
    conn = sqlite3.connect('./db/development.sqlite3')
    cur  = conn.cursor()
    now  = str(datetime.datetime.now())
    name = "scan-" + str(random.randrange(1000000))
    for mac, ip in MACS.items():
        try:
            cur.execute('INSERT INTO network_devices(mac_address, name, interface, ip_address, created_at, updated_at, detected_at) VALUES(?,?,?,?,?,?,?)',
                       (mac, name, interface, ip, now, now, now))
        except sqlite3.IntegrityError as e:
            pass
    conn.commit()

def main():
    args      = cmd_parse()
    interface = args.interface
    duration  = args.duration

    sniff(iface=interface, prn=collect_packets, store=0, timeout=duration)
    write_to_db(interface)

if __name__ == "__main__":
    main()

