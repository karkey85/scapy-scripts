
from scapy.all import *
load_contrib("ospf")


IPsrc = '1.1.1.1'
OSPFsrc = '1.1.1.1'

#OSPF Hello Pkt
IPHdr=IP(src=IPsrc,dst='224.0.0.5')
OSPFHdr=OSPF_Hdr(src=OSPFsrc,area='0.0.0.3')
packet=Ether()/IPHdr/OSPFHdr/OSPF_Hello(options=2)
sendp(packet,iface='eth0')
