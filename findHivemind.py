import dpkt
import socket

def findHivemind(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if dport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDoS Hivemind issued by: ' + src)
                    print('[+] Target CMD: ' + tcp.data)
            if sport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDoS Hivemind issued to: ' + src)
                    print ('[+] Target CMD: ' + tcp.data)
        except:
            pass

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)
findHivemind(pcap)