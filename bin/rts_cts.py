#!/usr/bin/env python3

from scapy.all import *
from datetime import *
import pytz
import argparse
import sqlite3

def cmd_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--spoofed", help="the spoofed source mac address", type=str, required=True)
    parser.add_argument("-t", "--target", help="the target mac address", type=str, required=True)
    parser.add_argument("-d", "--duration", help="the duration, in seconds to wait for cts reply", type=int, required=True)
    parser.add_argument("-i", "--interface", help="the network interface", type=str, required=True)

    args = parser.parse_args()
    return args

def send_rts_frame(interface, target, source):
    rts   = Dot11(type=1, subtype=11, addr1=target, addr2=source)
    frame = RadioTap()/rts
    sendp(frame, iface=interface, count=5, inter=0.1)

def listen_for_cts(target, spoofed):
    def packet_detected(packet):
        if packet.haslayer(Dot11) and packet.type == 1 and packet.subtype == 12 and packet.src == spoofed:
            # RTS/CTS attack successful - update the detcted_at timetamp for the target network device
            mark_target_device_detected(target)

    return packet_detected

def mark_target_device_detected(target):
    conn = sqlite3.connect('./db/development.sqlite3')
    cur  = conn.cursor()
    now  = datetime.now(tz=pytz.UTC)
    cur.execute('UPDATE network_devices SET detected_at=? WHERE mac_address=?', (now, target))
    conn.commit()

def main():
    args      = cmd_parse()
    spoofed   = args.spoofed
    target    = args.target
    duration  = args.duration
    interface = args.interface

    print("\nSending RTS packet to " + target)
    send_rts_frame(interface, target, spoofed)

    print("\nListening for CTS packet to " + spoofed)

    sniff(iface=interface, prn=listen_for_cts(target, spoofed), store=0, timeout=duration)

if __name__ == "__main__":
    main()

