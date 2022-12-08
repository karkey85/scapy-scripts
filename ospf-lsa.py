#!/usr/bin/env python

from scapy.all import *
load_contrib("ospf")


LsId='1.1.1.1'
AdvRtr='1.1.1.1'
sequence=0x80000500

IPsrc = '1.1.1.1'
OSPFsrc = '1.1.1.1'

#Router Links
link1 = OSPF_Link(id='2.2.2.2',data='0.0.0.40',type=1,toscount=0,metric=1)
link2 = OSPF_Link(id='1.1.1.1',data='255.255.255.255',type=3,toscount=0,metric=10)

#OSPF LSA Update Pkt having Router LSA
IPHdr=IP(src=IPsrc,dst='224.0.0.5')
OSPFHdr=OSPF_Hdr(src=OSPFsrc,area='0.0.0.3')
packet=Ether()/IPHdr/OSPFHdr/OSPF_LSUpd(lsacount=1,\
                                            lsalist=[OSPF_Router_LSA(id=LsId,adrouter=AdvRtr,seq=sequence,\
                                            linkcount=2,\
                                            linklist=[link1,link2])])
sendp(packet,iface='eth0') 
