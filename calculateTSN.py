# coding=UTF-8
from scapy.all import *
def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0

    for x in range(1, 5):
        if preNum !=0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print('[+] TCP Seq Difference: ' + str(diffSeq))
    return seqNum + diffSeq

tgt = '123.56.99.154'#这个服务器是我在阿里云买的,暂时属于我.请朋友们多多推荐下演道网:http://go2live.cn
seqNum = calTSN(tgt)
print("[+] Next TCP Sequence Number to ACK is: " + str(seqNum+1))