#!/usr/bin/env python

import dpkt
import sys
import pcapy

class PcapIntegration(object):
    """docstring for PcapIntegration."""
    def __init__(self, iface):
        # super PcapIntegration, self).__init__()
        self.iface = iface

    def start(self):
        # iface = self.iface
        # print iface
        # pc = pcapy.open_live(iface, 65535, False, 1)
        # pc.loop(-1, self.packprocess)

        # list all the network devices
        pcapy.findalldevs()

        max_bytes = 1024
        promiscuous = False
        read_timeout = 100 # in milliseconds
        pc = pcapy.open_live("eth0", max_bytes,
            promiscuous, read_timeout)
        packet_limit = -1 # infinite
        pc.loop(packet_limit, self.packprocess) # capture packets

    def packprocess(self, header, data):
        # print header
        eth = dpkt.ethernet.Ethernet (data)
#        print "%04X" % eth.type
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            print header
            ip = eth.data
            ip_data = ip.data
            if isinstance (ip_data, dpkt.udp.UDP):
                udp = ip_data
                print "sport: %s -> dport: %s" %(udp.sport, udp.dport)


if __name__ == "__main__":
    iface = "en1"
    iface = sys.argv[1]
    # todo: check if interface is provided
    # roadmap - load local file from shared directory
    PcapIntegration(iface).start()
