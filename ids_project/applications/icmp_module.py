#!/usr/bin/python

import datetime
import time
import sys
from scapy.all import *

def identify_icmp(ip_src, ip_dst, msg_type):
    packet


pkts = sniff(filter="icmp", timeout = 15, count = 15)

if pkts and str(pkts[0].getlayer(ICMP).type) == "8":
        print('Adresa IP sursa este:')
        print(pkts[0][IP].src)
        print('Adresa IP destinatie este:')
        print(pkts[0][IP].dst)
        print('Tipul mesajului:')
        print(pkts[0][ICMP].type)
        print(pkts[0][ICMP].id)

if pkts and str(pkts[1].getlayer(ICMP).type) == "0":
        print('Adresa IP sursa este:')
        print(pkts[1][IP].src)
        print('Adresa IP destinatie este:')
        print(pkts[1][IP].dst)
        print('Tipul mesajului:')
        print(pkts[1][ICMP].type)
        print(pkts[1][ICMP].id)

