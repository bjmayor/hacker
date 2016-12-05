from scapy.all import *
def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            print('[+] Pkt Received From:'+ ipsrc+' with TTL:' + ttl)
    except:
        pass

def main():
    sniff(prn=testTTL, store=0,count=10)

if __name__ == '__main__':
    main()