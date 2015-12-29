#!/usr/bin/env python


import socket
import fcntl
import struct

def get_ip_address(ifname):
    skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    pktString = fcntl.ioctl(skt.fileno(),0x8915,struct.pack('256s',ifname[:15]))
    ipString = socket.inet_ntoa(pktString[20:24])
    return ipString

if __name__ == "__main__":
    print get_ip_address("lo")
    print get_ip_address("eth0")

